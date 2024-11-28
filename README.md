# Weather App README

## Overview

The Weather App is a Python application that provides real-time weather information for any city using the OpenWeatherMap API. Built with the PyQt5 framework, it features an intuitive graphical user interface (GUI) where users can input a city name and view detailed weather data, including temperature in Kelvin, Celsius, and Fahrenheit, as well as weather conditions represented by icons and descriptions.

## Features

- **City-Based Weather Search**: Enter a city name to fetch current weather data.
- **Temperature Display**: Shows temperatures in Kelvin, Celsius, and Fahrenheit.
- **Dynamic Weather Icons**: Displays relevant icons for various weather conditions (e.g., ☀️ for clear skies).
- **Error Handling**: Displays user-friendly error messages for invalid input, network errors, or unsupported city names.
- **Responsive Design**: Dynamically adjusts font sizes and layout based on the screen resolution.
- **Customizable Background**: Potential for dynamic background images based on weather conditions.

## Installation

### Prerequisites
- Python 3.8 or higher
- `PyQt5` library
- `requests` library

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(If `requirements.txt` is not provided, install manually):*
   ```bash
   pip install PyQt5 requests
   ```

3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/). Replace the placeholder API key in the `getWeather` method with your key:
   ```python
   apiKey = "your_api_key_here"
   ```

4. Run the application:
   ```bash
   python weather_app.py
   ```

## Usage

1. Launch the app.
2. Enter the name of a city (e.g., "Ottawa").
3. Click the **Get Weather** button.
4. View the displayed weather details:
   - Temperatures (Kelvin, Celsius, Fahrenheit)
   - Weather description (e.g., "Clear sky")
   - Weather icon (e.g., ☀️ for sunny weather)

## File Structure

```
project/
│-- weather_app.py      # Main application file
│-- assets/             # Folder for images (optional for backgrounds)
│   └-- clear.jpg       # Example background image
│-- README.md           # Project documentation
│-- requirements.txt    # Python dependencies
```

## Key Components

### User Interface
- Built using **PyQt5**.
- Layouts are designed with `QVBoxLayout` and `QHBoxLayout` for responsiveness.
- Font sizes and widget dimensions adapt based on the user's screen resolution.

### Weather Data Fetching
- Uses the **OpenWeatherMap API** to retrieve weather data in JSON format.
- Error handling for:
  - Invalid city names
  - Network errors
  - API issues (e.g., unauthorized access)

### Dynamic Elements
- Weather icons adapt based on the `weatherId` from the API response.
- Planned support for custom background images for each weather type.

## Error Handling

The app provides clear feedback for common issues:
- **City Not Found**: Displays "404 Not Found: City not found."
- **Invalid API Key**: Displays "401 Unauthorized: Invalid API key."
- **Network Issues**: Handles general request errors gracefully.

## Planned Improvements
- Add background images for different weather conditions.
- Implement multi-day weather forecasting.
- Enhance UI with additional styling and animations.
