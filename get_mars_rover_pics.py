#!/usr/bin/env python3.7
# coding: utf-8
"""
    Takes input from NASA Mars-Rover API
    And get latest Mars Photo
"""

import requests
import json
from datetime import datetime, timedelta, date
import os
import sys
import random

#############################################
### Global Variables
### https://api.nasa.gov/api.html#MarsPhotos
MARS_ROVERS = ("curiosity", "opportunity", "spirit")
ROVER       = random.choice(MARS_ROVERS)

ROVER_PRE   = "https://api.nasa.gov/mars-photos/api/v1/rovers/"
ROVER_POST  = "/photos?"

ROVER_INI   = ROVER_PRE + ROVER + ROVER_POST

API_KEY     = ""
API_QS      = "api_key=" + API_KEY

CAMERA      = ("FHAZ", "RHAZ", "MAST", 
               "CHEMCAM", "MAHLI", "MARDI", 
               "NAVCAM", "PANCAM", "MINITES")

EARTH_DELTA = 15
EARTH_DATE  = str(datetime.now().date() - timedelta(days=EARTH_DELTA))

DELIMITER   = "&"

#############################################
###EXAMPLE QUERIES
#API_URL + sol=1000&api_key=API_KEY
#API_URL + sol=1000&camera=fhaz&api_key=API_KEY
#API_URL + sol=1000&page=2&api_key=API_KEY
#API_URL + earth_date=2015-6-3&api_key=API_KEY

#############################################

#############################################
### Get Random Date between two dates
def get_random_date(start_date, end_date):
    """
    """
    return start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())),
    )

#############################################

#############################################
### Make Rover Sol UR
def make_rover_sol_url(ROVER):
    """
    Make Rover Sol URL
    """
    if ROVER == "opportunity":
        SOL_DAYS    = random.randint(1,5108)
        SOL_QS      = "sol=" + str(SOL_DAYS)
        ROVER_QS    = str(SOL_QS) + DELIMITER + API_QS
        ROVER_URL   = ROVER_INI + ROVER_QS

        response    = requests.get(ROVER_URL)
        data        = response.json()

        for i in data:
            random_range = random.randint(0,len(data[i]))
            JPG_PHOTO = data[i][random.randint(0,len(data[i]))]['img_src']
            print(JPG_PHOTO)
    elif ROVER == "spirit":
        SOL_DAYS    = random.randint(1,2208)
        SOL_QS      = "sol=" + str(SOL_DAYS)
        ROVER_QS    = str(SOL_QS) + DELIMITER + API_QS
        ROVER_URL   = ROVER_INI + ROVER_QS

        response    = requests.get(ROVER_URL)
        data        = response.json()

        for i in data:
            random_range = random.randint(0,len(data[i]))
            JPG_PHOTO = data[i][random.randint(0,len(data[i]))]['img_src']
            print(JPG_PHOTO)
    else:
        print("Unknown Rover. Exiting now...")
        sys.exit()
#############################################

#############################################
### Get Photos from Opportunity Rover
def get_opportunity_photos():
    """
    Get Photos from Opportunity Rover
    Photos only earth_date from 2013-12-29 to 2015-12-28
    """
    #print("get_opportunity_photos")
    start_date  = date(year=2013, month=12, day=29)
    end_date    = date(year=2015, month=12, day=28)
    EARTH_QS    = get_random_date(start_date, end_date)
    ROVER_QS    = str(EARTH_QS) + DELIMITER + API_QS

    ROVER_URL   = ROVER_INI + ROVER_QS

    response    = requests.get(ROVER_URL)
    data        = response.json()
    
    for i in data:
        if len(data[i]) == 0:
            make_rover_sol_url(ROVER)
        else:
            random_range = random.randint(0,len(data[i]))
            JPG_PHOTO = data[i][random.randint(0,len(data[i]))]['img_src']
            print(JPG_PHOTO)
#############################################
    
#############################################
### Get Photos from Spirit Rover
def get_spirit_photos():
    """
    Get Photos from Spirit Rover
    Photos only earth_date from 2004-06-02 to 2010-03-21
    sol_days 0 to 2208
    """
    #print("get_spirit_photos")
    start_date  = date(year=2004, month=6, day=2)
    end_date    = date(year=2010, month=3, day=21)
    EARTH_QS    = get_random_date(start_date, end_date)
    ROVER_QS    = str(EARTH_QS) + DELIMITER + API_QS

    ROVER_URL   = ROVER_INI + ROVER_QS

    response    = requests.get(ROVER_URL)
    data        = response.json()

    for i in data:
        if len(data[i]) == 0:
            make_rover_sol_url(ROVER)
        else:
            random_range = random.randint(0,len(data[i]))
            JPG_PHOTO = data[i][random.randint(0,len(data[i]))]['img_src']
            print(JPG_PHOTO)


#############################################

#############################################
### Get Photos from Curiosity Rover
def get_curiosity_photos():
    """
    Get Photos from Curiosity Rover
    Photos only earth_date from 2012-08-18 to current
    Sol_days 0 to 5107
    """
    #print("get_curiosity_photos")
    
    EARTH_QS    = "earth_date=" + EARTH_DATE
    ROVER_QS    =  EARTH_QS + DELIMITER + API_QS

    ROVER_URL   = ROVER_INI + ROVER_QS

    response    = requests.get(ROVER_URL)
    data        = response.json()

    for i in data:
        random_range = random.randint(0,len(data[i]))
        JPG_PHOTO = data[i][random.randint(0,len(data[i]))]['img_src']
        print(JPG_PHOTO)

#############################################

#############################################
### Get all jpg files from EPIC EP
def get_mars_rover_photos():
    """
    Get all jpg files from Mars-Rover EP
    Only 3 Rovers will be selected.
    """
    if ROVER == "curiosity":
        get_curiosity_photos()
    elif ROVER == "opportunity":
        get_opportunity_photos()
    elif ROVER == "spirit":
        get_spirit_photos()
    else:
        print("Unknown Rover. Exiting now...")
        sys.exit()

#############################################


#############################################
### Main Program starts here
if __name__ == "__main__":
    get_mars_rover_photos()
else:
    print("Not a Script. Exiting now...")
    sys.exit(2)
