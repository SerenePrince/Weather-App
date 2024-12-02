import sys
import weather_app
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = weather_app.WeatherApp()
    window.show()
    sys.exit(app.exec_())
