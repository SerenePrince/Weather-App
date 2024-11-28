import sys
import os
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QGuiApplication, QPalette, QPixmap, QBrush

class WeatherApp(QWidget):
    """Weather App that fetches weather data for a specified city."""

    def __init__(self):
        """Initialize the weather app and its components."""
        super().__init__()

        # Initialize widgets for city input and weather display
        self.cityLabel = QLabel("Enter city name", self)
        self.cityInput = QLineEdit(self)
        self.getWeatherButton = QPushButton("Get Weather", self)

        # Initialize labels for temperature and weather description
        self.temperatureValueLabels = {
            'kelvin': QLabel("", self),
            'celsius': QLabel("", self),
            'fahrenheit': QLabel("", self)
        }
        self.temperatureLabels = {
            'kelvin': QLabel("Kelvin", self),
            'celsius': QLabel("Celsius", self),
            'fahrenheit': QLabel("Fahrenheit", self)
        }
        self.iconLabel = QLabel("❓", self)
        self.descriptionLabel = QLabel("How's the weather today?", self)

        # Set up the user interface
        self.initializeUI()

    def initializeUI(self):
        """Set up the UI layout, window size, and font sizes."""
        screen = QGuiApplication.primaryScreen().availableGeometry()
        screenWidth, screenHeight = screen.width(), screen.height()

        # Set window title and size
        self.setWindowTitle("Weather App")
        self.setMaximumSize(1024, 1440)
        self.resize(int(screenWidth * 0.8), int(screenHeight * 0.8))

        # Dynamic font size based on screen width
        baseFontSize = screenWidth // 50

        # Main layout container
        mainLayout = QVBoxLayout()

        # Weather input section
        mainLayout.addWidget(self.cityLabel)
        mainLayout.addWidget(self.cityInput)
        mainLayout.addWidget(self.getWeatherButton)

        # Temperature display section
        temperatureLayout = self.createTemperatureLayout()
        mainLayout.addLayout(temperatureLayout)

        # Weather icon and description labels
        mainLayout.addWidget(self.iconLabel)
        mainLayout.addWidget(self.descriptionLabel)

        # Set the main layout for the window
        self.setLayout(mainLayout)

        # Center align labels
        self.cityLabel.setAlignment(Qt.AlignCenter)
        self.cityInput.setAlignment(Qt.AlignCenter)
        self.iconLabel.setAlignment(Qt.AlignCenter)
        self.descriptionLabel.setAlignment(Qt.AlignCenter)

        # Connect button click to fetch weather data
        self.getWeatherButton.clicked.connect(self.getWeather)

        # Apply font sizes
        self.applyFontSizes(baseFontSize)

        # Center the window on the screen
        self.centerWindow()

    def createLabelBox(self, temperatureValueLabel, temperatureLabel):
        """Creates a temperature box with the value and corresponding unit label."""
        box = QWidget(self)
        boxLayout = QVBoxLayout()
        boxLayout.addWidget(temperatureValueLabel)
        boxLayout.addWidget(temperatureLabel)
        
        # Apply styling to the box
        box.setLayout(boxLayout)
        box.setStyleSheet("""
            background-color: #ffffff;
            border: 2px solid black;
            border-radius: 5px;
            padding: 10px;
        """)

        # Align labels in the box
        temperatureValueLabel.setAlignment(Qt.AlignCenter)
        temperatureLabel.setAlignment(Qt.AlignCenter)

        return box

    def createTemperatureLayout(self):
        """Creates and arranges the temperature labels in a horizontal layout."""
        temperatureLayout = QHBoxLayout()

        # Create and add temperature boxes for Kelvin, Celsius, and Fahrenheit
        for temp in ['kelvin', 'celsius', 'fahrenheit']:
            temperatureLayout.addWidget(self.createLabelBox(self.temperatureValueLabels[temp], self.temperatureLabels[temp]))

        temperatureLayout.setAlignment(Qt.AlignCenter)
        temperatureLayout.setStretch(0, 1)
        temperatureLayout.setStretch(1, 2)  # Add stretch to the middle box (today)
        temperatureLayout.setStretch(2, 1)

        return temperatureLayout

    def centerWindow(self):
        """Centers the application window on the screen."""
        screen = QGuiApplication.primaryScreen().availableGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def applyFontSizes(self, baseFontSize):
        """Applies dynamic font sizes to UI elements."""
        fontSizes = {
            self.cityLabel: baseFontSize,
            self.cityInput: baseFontSize * 0.8,
            self.getWeatherButton: baseFontSize * 0.8,
            self.temperatureValueLabels['kelvin']: baseFontSize * 0.5,
            self.temperatureValueLabels['celsius']: baseFontSize * 0.8,
            self.temperatureValueLabels['fahrenheit']: baseFontSize * 0.5,
            self.temperatureLabels['kelvin']: baseFontSize * 0.5,
            self.temperatureLabels['celsius']: baseFontSize * 0.8,
            self.temperatureLabels['fahrenheit']: baseFontSize * 0.5,
            self.iconLabel: baseFontSize,
            self.descriptionLabel: baseFontSize * 0.8
        }

        for widget, size in fontSizes.items():
            widget.setFont(QFont("Segoe UI", int(size)))
            
        self.iconLabel.setFont(QFont("Segoe UI Emoji", int(baseFontSize)))

    @staticmethod
    def setBackgroundImage(self, fileName):
        """Sets the background image of the window."""
        if fileName == "n/a":
            return
        
        # Resolve the full path of the file
        filePath = os.path.join(os.path.dirname(__file__), fileName)
        
        self.setAutoFillBackground(True)
        palette = self.palette()
        backgroundImage = QPixmap(filePath)

        if backgroundImage.isNull():
            print(f"Error: Background image not found or failed to load. Path: {filePath}")
            return

        brush = QBrush(backgroundImage)
        palette.setBrush(QPalette.Window, brush)
        self.setPalette(palette)

    def getWeather(self):
        """Fetches weather data from the API and updates the UI."""
        apiKey = "enterApiKeyHere"
        city = self.cityInput.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data["cod"] == 200:
                self.displayWeather(data)
                
        except requests.exceptions.HTTPError as httpError:
            self.handleHTTPError(response.status_code, httpError)
        except requests.exceptions.RequestException as req_error:
            self.displayError(f"Request Error: {req_error}")

    def handleHTTPError(self, status_code, error):
        """Handles different HTTP errors based on the status code."""
        error_messages = {
            400: "400 Bad Request: Please check your input",
            401: "401 Unauthorized: Invalid API key",
            403: "403 Forbidden: Access denied",
            404: "404 Not Found: City not found",
            500: "500 Internal Server Error: Please try again later",
            502: "502 Bad Gateway: Invalid response from server",
            503: "503 Service Unavailable: Server is down",
            504: "504 Gateway Timeout: Server unresponsive"
        }
        
        message = error_messages.get(status_code, f"HTTP error occurred: {error}")
        self.displayError(message)

    def displayError(self, message):
        """Displays an error message in the description label."""
        self.descriptionLabel.setText(message)
    
    def displayWeather(self, data):
        """Updates the UI with weather data."""
        temperatureKelvin = data["main"]["temp"]
        temperatureCelsius = temperatureKelvin - 273.15
        temperatureFahrenheit = (temperatureKelvin * 9/5) - 459.67
        weatherId = data["weather"][0]["id"]
        weatherDescription = data["weather"][0]["description"]

        # Update temperature labels
        self.temperatureValueLabels['kelvin'].setText(f"{temperatureKelvin:.0f}°")
        self.temperatureValueLabels['celsius'].setText(f"{temperatureCelsius:.0f}°")
        self.temperatureValueLabels['fahrenheit'].setText(f"{temperatureFahrenheit:.0f}°")
        
        # Update weather icon and description
        self.iconLabel.setText(self.getIcon(weatherId))
        self.descriptionLabel.setText(weatherDescription.title())
        
    def getIcon(self, weatherId):
        """Returns the weather icon based on the weather ID."""
        icon = ""
        background = "n/a"
        
        # Assign icons and background based on weather conditions
        if 200 <= weatherId <= 232:
            icon = "⛈️"
            # background = "thunderstorm.jpg"
        elif 300 <= weatherId <= 321:
            icon = "🌦️"
            # background = "drizzle.jpg"           
        elif 500 <= weatherId <= 531:
            icon = "🌧️"
            # background = "rain.jpg"
        elif 600 <= weatherId <= 622:
            icon = "🌨️"
            # background = "snow.jpg"
        elif 701 <= weatherId <= 741:
            icon = "🌫️"
            # background = "smoke.jpg"
        elif 751 <= weatherId <= 761:
            icon = "💨"
            # background = "dust.jpg"
        elif weatherId == 762:
            icon = "🌋"
            # background = "ash.jpg"
        elif weatherId == 771:
            icon = "🍃"
            # background = "squall.jpg"
        elif weatherId == 781:
            icon = "🌪️"
            # background = "tornado.jpg"
        elif weatherId == 800:
            icon = "☀️"
            background = "clear.jpg"
        elif 801 <= weatherId <= 804:
            icon = "☁️"
            # background = "clouds.jpg"
        else:
            icon = "❓"
        
        # Set background image based on the weather condition
        self.setBackgroundImage(self, background)

        return icon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
