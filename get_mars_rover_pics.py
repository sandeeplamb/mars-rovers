#!/usr/bin/env python3.7
# coding: utf-8
"""
Mars Rover Photo Fetcher

This script fetches random photos from NASA's Mars Rover API.
It supports three rovers: Curiosity, Opportunity, and Spirit.

API Documentation: https://api.nasa.gov/api.html#MarsPhotos

Features:
- Randomly selects one of three Mars rovers
- Fetches photos from random dates within each rover's operational period
- Falls back to sol-based queries if earth_date queries return no results
- Prints image URLs to stdout

Usage:
    python get_mars_rover_pics.py

Returns:
    Prints Mars rover photo URLs to stdout
"""

import requests
import json
from datetime import datetime, timedelta, date
import os
import sys
import random

#############################################
### Global Variables
#############################################

# Available Mars rovers
MARS_ROVERS = ("curiosity", "opportunity", "spirit")

# Randomly select a rover for this execution
ROVER = random.choice(MARS_ROVERS)

# API URL components
ROVER_PRE = "https://api.nasa.gov/mars-photos/api/v1/rovers/"
ROVER_POST = "/photos?"

# Complete rover URL prefix
ROVER_INI = ROVER_PRE + ROVER + ROVER_POST

# API key (currently empty - requires NASA API key)
API_KEY = ""
API_QS = "api_key=" + API_KEY

# Available camera types for each rover
CAMERA = ("FHAZ", "RHAZ", "MAST", 
          "CHEMCAM", "MAHLI", "MARDI", 
          "NAVCAM", "PANCAM", "MINITES")

# Days to subtract from current date for earth_date queries
EARTH_DELTA = 15
EARTH_DATE = str(datetime.now().date() - timedelta(days=EARTH_DELTA))

# URL parameter delimiter
DELIMITER = "&"

#############################################
### Example API Queries
#############################################
# API_URL + sol=1000&api_key=API_KEY
# API_URL + sol=1000&camera=fhaz&api_key=API_KEY
# API_URL + sol=1000&page=2&api_key=API_KEY
# API_URL + earth_date=2015-6-3&api_key=API_KEY

#############################################
### Custom Exceptions
#############################################

class MarsRoverAPIError(Exception):
    """Custom exception for Mars Rover API errors."""
    pass

class NoPhotosFoundError(Exception):
    """Custom exception when no photos are found."""
    pass

class NetworkError(Exception):
    """Custom exception for network-related errors."""
    pass

#############################################
### Utility Functions
#############################################

def get_random_date(start_date, end_date):
    """
    Generate a random date between two given dates.
    
    Args:
        start_date (date): Start date for the range
        end_date (date): End date for the range
        
    Returns:
        date: Random date within the specified range
    """
    try:
        return start_date + timedelta(
            seconds=random.randint(0, int((end_date - start_date).total_seconds())),
        )
    except (ValueError, TypeError) as e:
        raise MarsRoverAPIError(f"Invalid date range: {e}")

def make_api_request(url, timeout=30):
    """
    Make a safe API request with proper error handling.
    
    Args:
        url (str): The URL to request
        timeout (int): Request timeout in seconds
        
    Returns:
        dict: JSON response from the API
        
    Raises:
        NetworkError: If network request fails
        MarsRoverAPIError: If API returns an error
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()  # Raises HTTPError for bad status codes
        
        data = response.json()
        
        # Check if API returned an error message
        if 'error' in data:
            raise MarsRoverAPIError(f"API Error: {data['error']}")
            
        return data
        
    except requests.exceptions.Timeout:
        raise NetworkError(f"Request timeout after {timeout} seconds")
    except requests.exceptions.ConnectionError:
        raise NetworkError("Failed to connect to NASA API. Check your internet connection.")
    except requests.exceptions.HTTPError as e:
        if response.status_code == 429:
            raise MarsRoverAPIError("API rate limit exceeded. Please try again later.")
        elif response.status_code == 404:
            raise MarsRoverAPIError("Rover or endpoint not found.")
        else:
            raise MarsRoverAPIError(f"HTTP Error {response.status_code}: {e}")
    except requests.exceptions.RequestException as e:
        raise NetworkError(f"Request failed: {e}")
    except json.JSONDecodeError as e:
        raise MarsRoverAPIError(f"Invalid JSON response: {e}")

def make_rover_sol_url(rover):
    """
    Make a rover sol-based URL and fetch a random photo.
    
    This function is called as a fallback when earth_date queries
    return no results. It uses sol (Martian day) instead of earth_date.
    
    Args:
        rover (str): Name of the rover (curiosity, opportunity, spirit)
        
    Returns:
        None: Prints photo URL to stdout
        
    Raises:
        MarsRoverAPIError: If API request fails
        NoPhotosFoundError: If no photos are found
    """
    try:
        if rover == "opportunity":
            # Opportunity operated for 5111 sols (2004-2019)
            sol_days = random.randint(1, 5108)
            sol_qs = "sol=" + str(sol_days)
            rover_qs = str(sol_qs) + DELIMITER + API_QS
            rover_url = ROVER_INI + rover_qs

            data = make_api_request(rover_url)

            for i in data:
                if len(data[i]) == 0:
                    raise NoPhotosFoundError(f"No photos found for Opportunity sol {sol_days}")
                random_range = random.randint(0, len(data[i]))
                jpg_photo = data[i][random_range]['img_src']
                print(jpg_photo)
                return
                
        elif rover == "spirit":
            # Spirit operated for 2208 sols (2004-2010)
            sol_days = random.randint(1, 2208)
            sol_qs = "sol=" + str(sol_days)
            rover_qs = str(sol_qs) + DELIMITER + API_QS
            rover_url = ROVER_INI + rover_qs

            data = make_api_request(rover_url)

            for i in data:
                if len(data[i]) == 0:
                    raise NoPhotosFoundError(f"No photos found for Spirit sol {sol_days}")
                random_range = random.randint(0, len(data[i]))
                jpg_photo = data[i][random_range]['img_src']
                print(jpg_photo)
                return
        else:
            raise MarsRoverAPIError(f"Unknown rover: {rover}")
            
    except (MarsRoverAPIError, NoPhotosFoundError) as e:
        # Try one more time with a different sol
        try:
            if rover == "opportunity":
                sol_days = random.randint(1, 5108)
            elif rover == "spirit":
                sol_days = random.randint(1, 2208)
            else:
                raise e
                
            sol_qs = "sol=" + str(sol_days)
            rover_qs = str(sol_qs) + DELIMITER + API_QS
            rover_url = ROVER_INI + rover_qs

            data = make_api_request(rover_url)

            for i in data:
                if len(data[i]) > 0:
                    random_range = random.randint(0, len(data[i]))
                    jpg_photo = data[i][random_range]['img_src']
                    print(jpg_photo)
                    return
                    
            raise NoPhotosFoundError(f"No photos found for {rover} after retry")
            
        except Exception as retry_error:
            raise MarsRoverAPIError(f"Failed to get photos for {rover}: {e}. Retry failed: {retry_error}")

#############################################
### Rover-Specific Photo Functions
#############################################

def get_opportunity_photos():
    """
    Get photos from Opportunity rover.
    
    Opportunity operated from 2004-01-25 to 2019-02-13.
    This function uses earth_date queries for the period 2013-12-29 to 2015-12-28.
    Falls back to sol-based queries if no photos are found.
    
    Returns:
        None: Prints photo URL to stdout
        
    Raises:
        MarsRoverAPIError: If API request fails
        NoPhotosFoundError: If no photos are found after all attempts
    """
    try:
        start_date = date(year=2013, month=12, day=29)
        end_date = date(year=2015, month=12, day=28)
        earth_qs = get_random_date(start_date, end_date)
        rover_qs = str(earth_qs) + DELIMITER + API_QS

        rover_url = ROVER_INI + rover_qs

        data = make_api_request(rover_url)
        
        for i in data:
            if len(data[i]) == 0:
                # Fallback to sol-based query if no photos found
                make_rover_sol_url(ROVER)
                return
            else:
                random_range = random.randint(0, len(data[i]))
                jpg_photo = data[i][random_range]['img_src']
                print(jpg_photo)
                return
                
        raise NoPhotosFoundError("No photos found for Opportunity")
        
    except Exception as e:
        raise MarsRoverAPIError(f"Failed to get Opportunity photos: {e}")

def get_spirit_photos():
    """
    Get photos from Spirit rover.
    
    Spirit operated from 2004-01-04 to 2010-03-22.
    This function uses earth_date queries for the period 2004-06-02 to 2010-03-21.
    Falls back to sol-based queries if no photos are found.
    
    Returns:
        None: Prints photo URL to stdout
        
    Raises:
        MarsRoverAPIError: If API request fails
        NoPhotosFoundError: If no photos are found after all attempts
    """
    try:
        start_date = date(year=2004, month=6, day=2)
        end_date = date(year=2010, month=3, day=21)
        earth_qs = get_random_date(start_date, end_date)
        rover_qs = str(earth_qs) + DELIMITER + API_QS

        rover_url = ROVER_INI + rover_qs

        data = make_api_request(rover_url)

        for i in data:
            if len(data[i]) == 0:
                # Fallback to sol-based query if no photos found
                make_rover_sol_url(ROVER)
                return
            else:
                random_range = random.randint(0, len(data[i]))
                jpg_photo = data[i][random_range]['img_src']
                print(jpg_photo)
                return
                
        raise NoPhotosFoundError("No photos found for Spirit")
        
    except Exception as e:
        raise MarsRoverAPIError(f"Failed to get Spirit photos: {e}")

def get_curiosity_photos():
    """
    Get photos from Curiosity rover.
    
    Curiosity has been operating since 2012-08-06 and is still active.
    This function uses earth_date queries for a date EARTH_DELTA days ago.
    
    Returns:
        None: Prints photo URL to stdout
        
    Raises:
        MarsRoverAPIError: If API request fails
        NoPhotosFoundError: If no photos are found
    """
    try:
        earth_qs = "earth_date=" + EARTH_DATE
        rover_qs = earth_qs + DELIMITER + API_QS

        rover_url = ROVER_INI + rover_qs

        data = make_api_request(rover_url)

        for i in data:
            if len(data[i]) == 0:
                raise NoPhotosFoundError(f"No photos found for Curiosity on {EARTH_DATE}")
            random_range = random.randint(0, len(data[i]))
            jpg_photo = data[i][random_range]['img_src']
            print(jpg_photo)
            return
            
        raise NoPhotosFoundError("No photos found for Curiosity")
        
    except Exception as e:
        raise MarsRoverAPIError(f"Failed to get Curiosity photos: {e}")

#############################################
### Main Function
#############################################

def get_mars_rover_photos():
    """
    Main function to get Mars rover photos.
    
    Randomly selects one of the three Mars rovers and calls
    the appropriate function to fetch photos from that rover.
    
    Returns:
        None: Prints photo URL to stdout
        
    Raises:
        MarsRoverAPIError: If API request fails
        NoPhotosFoundError: If no photos are found
        NetworkError: If network request fails
    """
    try:
        if ROVER == "curiosity":
            get_curiosity_photos()
        elif ROVER == "opportunity":
            get_opportunity_photos()
        elif ROVER == "spirit":
            get_spirit_photos()
        else:
            raise MarsRoverAPIError(f"Unknown Rover: {ROVER}")
            
    except (MarsRoverAPIError, NoPhotosFoundError, NetworkError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

#############################################
### Main Program Entry Point
#############################################

if __name__ == "__main__":
    try:
        get_mars_rover_photos()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(0)
    except Exception as e:
        print(f"Fatal error: {e}", file=sys.stderr)
        sys.exit(1)
else:
    print("Not a Script. Exiting now...")
    sys.exit(2)
