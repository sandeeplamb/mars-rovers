# Mars Rover Photo Fetcher

A Python script that fetches random photos from NASA's Mars Rover API. This tool randomly selects one of three Mars rovers (Curiosity, Opportunity, or Spirit) and retrieves photos from their missions.

## 🚀 Features

- **Random Rover Selection**: Automatically selects one of three Mars rovers for each execution
- **Smart Date Selection**: Uses appropriate date ranges for each rover's operational period
- **Fallback Mechanism**: Falls back to sol-based queries if earth_date queries return no results
- **Multiple Camera Support**: Supports various camera types used by the rovers
- **Simple Output**: Prints direct image URLs to stdout for easy integration

## 📋 Prerequisites

- Python 3.7 or higher
- `requests` library
- NASA API key (optional but recommended for higher rate limits)

## 🛠️ Installation

1. Clone this repository:
```bash
git clone git@github.com:sandeeplamb/mars-rovers.git
cd mars-rovers
```

2. Install required dependencies:
```bash
pip install requests
```

3. (Optional) Get a NASA API key:
   - Visit [NASA API Portal](https://api.nasa.gov/)
   - Sign up for a free API key
   - Add your API key to the `API_KEY` variable in `get_mars_rover_pics.py`

## 🚀 Usage

### Basic Usage
```bash
python get_mars_rover_pics.py
```

### Example Output
```
https://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/01000/opgs/edr/fcam/FLB_486265257EDR_F0481570FHAZ00323M_.JPG
```

### As a Module
```python
from get_mars_rover_pics import get_mars_rover_photos

# Get a random Mars rover photo
get_mars_rover_photos()
```

## 🛰️ Mars Rovers

### Curiosity
- **Mission**: Mars Science Laboratory (MSL)
- **Launch Date**: November 26, 2011
- **Landing Date**: August 6, 2012
- **Status**: Active (Still operating on Mars)
- **Location**: Gale Crater
- **Mission Duration**: 11+ years and counting
- **Sol Range**: 0 to 5107+ (Martian days)
- **Cameras**: 17 total cameras including Mastcam, ChemCam, MAHLI, and more

**NASA Resources:**
- [Curiosity Mission Page](https://mars.nasa.gov/msl/)
- [Curiosity Raw Images](https://mars.nasa.gov/msl/multimedia/raw-images/)
- [Curiosity Mission Updates](https://mars.nasa.gov/msl/mission/status/)

### Opportunity & Spirit

| Property | Opportunity | Spirit |
|----------|-------------|---------|
| **Mission** | Mars Exploration Rover (MER-B) | Mars Exploration Rover (MER-A) |
| **Launch Date** | July 7, 2003 | June 10, 2003 |
| **Landing Date** | January 25, 2004 | January 4, 2004 |
| **Status** | Mission ended (February 13, 2019) | Mission ended (March 22, 2010) |
| **Location** | Meridiani Planum | Gusev Crater |
| **Mission Duration** | 15 years, 1 month, 19 days | 6 years, 2 months, 18 days |
| **Sol Range** | 0 to 5111 (Martian days) | 0 to 2208 (Martian days) |
| **Distance Traveled** | 45.16 km (28.06 miles) | 7.73 km (4.8 miles) |

**NASA Resources:**

| Resource Type | Opportunity | Spirit |
|---------------|-------------|---------|
| **Mission Page** | [Opportunity Mission](https://mars.nasa.gov/mer/) | [Spirit Mission](https://mars.nasa.gov/mer/) |
| **Raw Images** | [Opportunity Images](https://mars.nasa.gov/mer/gallery/all/opportunity_n.html) | [Spirit Images](https://mars.nasa.gov/mer/gallery/all/spirit_n.html) |
| **Mission Updates** | [Opportunity Updates](https://mars.nasa.gov/mer/mission/status.html) | [Spirit Updates](https://mars.nasa.gov/mer/mission/status.html) |

## 🔧 API Information

### NASA Mars Rover API

| Property | Value |
|----------|-------|
| **Base URL** | `https://api.nasa.gov/mars-photos/api/v1/rovers/` |
| **Documentation** | [NASA Mars Rover API](https://api.nasa.gov/api.html#MarsPhotos) |
| **Rate Limits (No API Key)** | 1,000 requests per hour |
| **Rate Limits (With API Key)** | 1,000 requests per hour (higher limits available) |
| **Response Format** | JSON |

### Example API Queries
```
# Get photos by sol (Martian day)
https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY

# Get photos by earth date
https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2015-6-3&api_key=DEMO_KEY

# Get photos by camera
https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=DEMO_KEY
```

## 📸 Camera Types

The script supports various camera types used by the Mars rovers:

| Camera | Full Name | Description |
|--------|-----------|-------------|
| **FHAZ** | Front Hazard Avoidance Camera | Front-facing camera for obstacle detection |
| **RHAZ** | Rear Hazard Avoidance Camera | Rear-facing camera for obstacle detection |
| **MAST** | Mast Camera | High-resolution camera mounted on the mast |
| **CHEMCAM** | Chemistry and Camera Complex | Laser spectrometer and camera for chemical analysis |
| **MAHLI** | Mars Hand Lens Imager | Close-up camera for detailed surface examination |
| **MARDI** | Mars Descent Imager | Camera that recorded the landing sequence |
| **NAVCAM** | Navigation Camera | Stereo cameras for navigation and driving |
| **PANCAM** | Panoramic Camera | High-resolution panoramic camera system |
| **MINITES** | Miniature Thermal Emission Spectrometer | Infrared spectrometer for mineral identification |

## 🔍 How It Works

1. **Rover Selection**: Randomly selects one of three Mars rovers
2. **Date Strategy**: 
   - Uses earth_date queries for recent photos (Curiosity)
   - Uses historical date ranges for completed missions (Opportunity, Spirit)
3. **Fallback Mechanism**: If no photos found, switches to sol-based queries
4. **Photo Selection**: Randomly selects one photo from available results
5. **Output**: Prints the direct image URL to stdout

## 🛠️ Configuration

### Environment Variables
You can set your NASA API key as an environment variable:
```bash
export NASA_API_KEY="your_api_key_here"
```

### Script Variables
Key variables you can modify in the script:
- `EARTH_DELTA`: Days to subtract from current date (default: 15)
- `MARS_ROVERS`: Available rovers to choose from
- `CAMERA`: Available camera types

## 📊 Mission Statistics

| Rover | Launch Date | Landing Date | Status | Sols | Distance |
|-------|-------------|--------------|---------|------|----------|
| Curiosity | 2011-11-26 | 2012-08-06 | Active | 5107+ | 29.2 km |
| Opportunity | 2003-07-07 | 2004-01-25 | Ended | 5111 | 45.16 km |
| Spirit | 2003-06-10 | 2004-01-04 | Ended | 2208 | 7.73 km |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **NASA**: For providing the Mars Rover API and mission data
- **JPL**: Jet Propulsion Laboratory for managing the Mars rover missions
- **Mars Exploration Program**: For the incredible scientific discoveries

## 📚 Additional Resources

- [NASA Mars Exploration Program](https://mars.nasa.gov/)
- [Mars Rover API Documentation](https://api.nasa.gov/api.html#MarsPhotos)
- [Mars Weather](https://mars.nasa.gov/msl/weather/)
- [Mars Missions Timeline](https://mars.nasa.gov/mars-exploration/missions/)
- [Mars Rover Images Gallery](https://mars.nasa.gov/gallery/)

## 🐛 Troubleshooting

### Common Issues

1. **No photos returned**: Try running the script multiple times as it uses random dates
2. **API rate limiting**: Get a NASA API key for higher limits
3. **Network errors**: Check your internet connection and NASA API status

### Getting Help

If you encounter issues:
1. Check the [NASA API status](https://api.nasa.gov/)
2. Verify your API key is correct
3. Check the script's error messages
4. Open an issue on GitHub

---

*This project is not affiliated with NASA or JPL. It's an independent tool for accessing NASA's public Mars Rover API.*
