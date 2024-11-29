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
        self.city_label = QLabel("Enter city name", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)

        # Initialize labels for temperature and weather description
        self.temperature_value_labels = {
            'kelvin': QLabel("", self),
            'celsius': QLabel("", self),
            'fahrenheit': QLabel("", self)
        }
        self.temperature_labels = {
            'kelvin': QLabel("Kelvin", self),
            'celsius': QLabel("Celsius", self),
            'fahrenheit': QLabel("Fahrenheit", self)
        }
        self.icon_label = QLabel("❓", self)
        self.description_label = QLabel("How's the weather today?", self)

        # Set up the user interface
        self.initializeUI()

    def initializeUI(self):
        """Set up the UI layout, window size, and font sizes."""
        screen = QGuiApplication.primaryScreen().availableGeometry()
        screen_width, screen_height = screen.width(), screen.height()

        # Set window title and size
        self.setWindowTitle("Weather App")
        self.setMaximumSize(1024, 1440)
        self.resize(int(screen_width * 0.8), int(screen_height * 0.8))

        # Dynamic font size based on screen width
        base_font_size = screen_width // 50

        # Main layout container
        main_layout = QVBoxLayout()

        # Weather input section
        main_layout.addWidget(self.city_label)
        main_layout.addWidget(self.city_input)
        main_layout.addWidget(self.get_weather_button)

        # Temperature display section
        temperature_layout = self.createTemperatureLayout()
        main_layout.addLayout(temperature_layout)

        # Weather icon and description labels
        main_layout.addWidget(self.icon_label)
        main_layout.addWidget(self.description_label)

        # Set the main layout for the window
        self.setLayout(main_layout)

        # Center align labels
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.icon_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Connect button click to fetch weather data
        self.get_weather_button.clicked.connect(self.getWeather)

        # Apply font sizes
        self.applyFontSizes(base_font_size)

        # Center the window on the screen
        self.centerWindow()

    def createLabelBox(self, temperature_value_label, temperature_label):
        """Creates a temperature box with the value and corresponding unit label."""
        box = QWidget(self)
        box_layout = QVBoxLayout()
        box_layout.addWidget(temperature_value_label)
        box_layout.addWidget(temperature_label)
        
        # Apply styling to the box
        box.setLayout(box_layout)
        box.setStyleSheet("""
            background-color: #ffffff;
            border: 2px solid black;
            border-radius: 5px;
            padding: 10px;
        """)

        # Align labels in the box
        temperature_value_label.setAlignment(Qt.AlignCenter)
        temperature_label.setAlignment(Qt.AlignCenter)

        return box

    def createTemperatureLayout(self):
        """Creates and arranges the temperature labels in a horizontal layout."""
        temperature_layout = QHBoxLayout()

        # Create and add temperature boxes for Kelvin, Celsius, and Fahrenheit
        for temp in ['kelvin', 'celsius', 'fahrenheit']:
            temperature_layout.addWidget(self.createLabelBox(self.temperature_value_labels[temp], self.temperature_labels[temp]))

        temperature_layout.setAlignment(Qt.AlignCenter)
        temperature_layout.setStretch(0, 1)
        temperature_layout.setStretch(1, 2)  # Add stretch to the middle box (today)
        temperature_layout.setStretch(2, 1)

        return temperature_layout

    def centerWindow(self):
        """Centers the application window on the screen."""
        screen = QGuiApplication.primaryScreen().availableGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def applyFontSizes(self, base_font_size):
        """Applies dynamic font sizes to UI elements."""
        fontSizes = {
            self.city_label: base_font_size,
            self.city_input: base_font_size * 0.8,
            self.get_weather_button: base_font_size * 0.8,
            self.temperature_value_labels['kelvin']: base_font_size * 0.5,
            self.temperature_value_labels['celsius']: base_font_size * 0.8,
            self.temperature_value_labels['fahrenheit']: base_font_size * 0.5,
            self.temperature_labels['kelvin']: base_font_size * 0.5,
            self.temperature_labels['celsius']: base_font_size * 0.8,
            self.temperature_labels['fahrenheit']: base_font_size * 0.5,
            self.icon_label: base_font_size,
            self.description_label: base_font_size * 0.8
        }

        for widget, size in fontSizes.items():
            widget.setFont(QFont("Segoe UI", int(size)))
            
        self.icon_label.setFont(QFont("Segoe UI Emoji", int(base_font_size)))

    @staticmethod
    def setBackgroundImage(self, file_name):
        """Sets the background image of the window."""
        if file_name == "n/a":
            return
        
        # Resolve the full path of the file
        filePath = os.path.join(os.path.dirname(__file__), file_name)
        
        self.setAutoFillBackground(True)
        palette = self.palette()
        background_image = QPixmap(filePath)

        if background_image.isNull():
            print(f"Error: Background image not found or failed to load. Path: {filePath}")
            return

        brush = QBrush(background_image)
        palette.setBrush(QPalette.Window, brush)
        self.setPalette(palette)

    def getWeather(self):
        """Fetches weather data from the API and updates the UI."""
<<<<<<< HEAD
        apiKey = "7825b0b37b3d31666b6a00e5a55b5532"
        city = self.city_input.text()
=======
        apiKey = "enterApiKeyHere"
        city = self.cityInput.text()
>>>>>>> a85baa5f1adda99086cc29db1206d7a09c3b9752
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            if data["cod"] == 200:
                self.displayWeather(data)
                
        except requests.exceptions.HTTPError as http_error:
            self.handleHTTPError(response.status_code, http_error)
        except requests.exceptions.RequestException as req_error:
            self.displayError(f"Request Error: {req_error}")

    def handleHTTPError(self, status_code, error):
        """Handles different HTTP errors based on the status code."""
        ERROR_MESSAGES = {
            400: "400 Bad Request: Please check your input",
            401: "401 Unauthorized: Invalid API key",
            403: "403 Forbidden: Access denied",
            404: "404 Not Found: City not found",
            500: "500 Internal Server Error: Please try again later",
            502: "502 Bad Gateway: Invalid response from server",
            503: "503 Service Unavailable: Server is down",
            504: "504 Gateway Timeout: Server unresponsive"
        }
        
        message = ERROR_MESSAGES.get(status_code, f"HTTP error occurred: {error}")
        self.displayError(message)

    def displayError(self, message):
        """Displays an error message in the description label."""
        self.description_label.setText(message)
    
    def displayWeather(self, data):
        """Updates the UI with weather data."""
        temperature_kelvin = data["main"]["temp"]
        temperature_celsius = temperature_kelvin - 273.15
        temperature_fahrenheit = (temperature_kelvin * 9/5) - 459.67
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        # Update temperature labels
        self.temperature_value_labels['kelvin'].setText(f"{temperature_kelvin:.0f}°")
        self.temperature_value_labels['celsius'].setText(f"{temperature_celsius:.0f}°")
        self.temperature_value_labels['fahrenheit'].setText(f"{temperature_fahrenheit:.0f}°")
        
        # Update weather icon and description
        self.icon_label.setText(self.getIcon(weather_id))
        self.description_label.setText(weather_description.title())
        
    def getIcon(self, weather_id):
        """Returns the weather icon based on the weather ID."""
        icon = ""
        background = "n/a"
        
        # Assign icons and background based on weather conditions
        if 200 <= weather_id <= 232:
            icon = "⛈️"
            # background = "thunderstorm.jpg"
        elif 300 <= weather_id <= 321:
            icon = "🌦️"
            # background = "drizzle.jpg"           
        elif 500 <= weather_id <= 531:
            icon = "🌧️"
            # background = "rain.jpg"
        elif 600 <= weather_id <= 622:
            icon = "🌨️"
            # background = "snow.jpg"
        elif 701 <= weather_id <= 741:
            icon = "🌫️"
            # background = "smoke.jpg"
        elif 751 <= weather_id <= 761:
            icon = "💨"
            # background = "dust.jpg"
        elif weather_id == 762:
            icon = "🌋"
            # background = "ash.jpg"
        elif weather_id == 771:
            icon = "🍃"
            # background = "squall.jpg"
        elif weather_id == 781:
            icon = "🌪️"
            # background = "tornado.jpg"
        elif weather_id == 800:
            icon = "☀️"
            background = "clear.jpg"
        elif 801 <= weather_id <= 804:
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
