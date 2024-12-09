---
# Weather App

![weather-app-showcase1](https://github.com/user-attachments/assets/078b5a4b-160d-4784-be1c-d72f2c2ddaf8)

## 🌤️ Overview
The **Weather App** is a Python-based application that provides real-time weather updates for any city using the **OpenWeatherMap API**. Developed with **PyQt5**, it features a clean and responsive GUI, offering detailed weather data, including temperature in Kelvin, Celsius, and Fahrenheit, along with dynamic weather icons and descriptions.
---

## ✨ Features

- **City Search**: Fetch real-time weather data by entering a city name.
- **Temperature Conversion**: Displays temperatures in Kelvin, Celsius, and Fahrenheit.
- **Dynamic Icons**: Visually represents weather conditions (e.g., ☀️ for sunny skies).
- **Error Handling**: Provides clear feedback for invalid input or network issues.
- **Responsive UI**: Adapts layout and font sizes for different screen resolutions.

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- `PyQt5` and `requests` libraries

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/SerenePrince/Weather-App.git
   cd weather-app
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   _(If missing, manually install)_:
   ```bash
   pip install PyQt5 requests
   ```
3. **Obtain an OpenWeatherMap API Key**:

   - Visit [OpenWeatherMap](https://openweathermap.org/api).
   - Sign up or log in to your account.
   - Generate a free API key from the API keys section.
   - Copy the API key.

4. Add your API key in `weather_app.py`:
   ```python
   apiKey = "your_api_key_here"
   ```
5. Run the app:
   ```bash
   python main.py
   ```

---

## 🛠️ Development Highlights

### Technologies Used

- **PyQt5**: For creating the interactive graphical user interface.
- **OpenWeatherMap API**: To retrieve and display real-time weather data.

### Key Features

- **Error Handling**: Covers invalid cities, network issues, and API errors.
- **Dynamic Elements**: Weather icons adapt to conditions; planned support for background images.

---

## 📂 File Structure

```
project/
│-- main.py             # Application entry point
│-- weather_app.py       # GUI and app logic
│-- weather_services.py  # API calls and data processing
│-- requirements.txt     # Dependencies
│-- assets/              # (Optional) Images for backgrounds/icons
```

---

## 📜 Planned Enhancements

- Add dynamic backgrounds for weather conditions.
- Introduce multi-day weather forecasting.
- Improve UI with animations and advanced styling.

---
