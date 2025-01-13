---

# 🌤️ Weather App  

![weather-app-showcase1](https://github.com/user-attachments/assets/078b5a4b-160d-4784-be1c-d72f2c2ddaf8)

## 🎯 Overview  
The **Weather App** is a simple Python project built to fetch and display real-time weather information for any city. Using the **OpenWeatherMap API** and **PyQt5** for the graphical user interface (GUI), this app allows users to search for a city and see the current temperature and weather conditions, including the weather type (e.g., sunny, cloudy, rainy).

This was my first project in Python, where I learned the basics of the language, API integration, and building a GUI application with PyQt5. The project helped me get comfortable with handling APIs, processing data, and creating a simple but functional interface.

---

## ✨ Features  
- **City Search**: Fetch current weather data by entering a city name.  
- **Temperature Display**: Shows the temperature in **Kelvin**, **Celsius**, and **Fahrenheit**.  
- **Weather Type**: Displays weather conditions, such as **sunny**, **cloudy**, or **rainy**.  
- **Dynamic Weather Icons**: Uses icons to visually represent weather conditions (e.g., ☀️ for sunny, 🌧️ for rainy).  
- **Error Handling**: Provides feedback for invalid city names, network errors, or API failures.  
- **Responsive GUI**: The interface adapts to different screen resolutions and window sizes.  

---

## 🛠️ Technologies Used  
- **Python 3.8+**: Core programming language.  
- **PyQt5**: For building the graphical user interface (GUI).  
- **OpenWeatherMap API**: To fetch live weather data.  
- **Requests**: For making API calls.  

---

## 🚀 Getting Started  

### Prerequisites  
- **Python 3.8** or higher is required.  
- Install the following libraries:
  - **PyQt5**
  - **Requests**

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
   _(If the above doesn’t work, install dependencies manually)_:
   ```bash  
   pip install PyQt5 requests  
   ```

3. **Get an OpenWeatherMap API Key**:  
   - Visit [OpenWeatherMap](https://openweathermap.org/api).  
   - Sign up or log in, and generate a free API key.  
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

## 🧠 Skills Demonstrated  
- **Python Basics**: Learned the fundamentals of Python, including working with libraries and making API calls.  
- **API Integration**: Integrated the **OpenWeatherMap API** to fetch real-time data and display it in the app.  
- **GUI Development**: Used **PyQt5** to design the application's user interface, making it interactive and user-friendly.  
- **Error Handling**: Implemented checks for invalid inputs, API issues, and network connectivity problems.  

---

## 📂 File Structure  

```
project/
│-- main.py             # Main entry point for the application
│-- weather_app.py       # Logic for handling weather data and UI
│-- weather_services.py  # Contains functions for API calls and data processing
│-- requirements.txt     # Lists all dependencies for the project
│-- assets/              # (Optional) Contains icons and background images for the app
```

---

## 📜 Planned Enhancements  
- Add dynamic background images that change based on the weather conditions (e.g., a sunny background for sunny weather).  
- Implement a **multi-day weather forecast** feature.  
- Improve the **user interface** with animations and more advanced styling.  

---
