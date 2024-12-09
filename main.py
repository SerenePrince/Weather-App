import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor, QFont
from PyQt5.QtCore import Qt
import weather_app

def create_window_icon() -> QIcon:
    """Create and return a custom window icon with a cloud emoji."""
    pixmap = QPixmap(32, 32)
    pixmap.fill(Qt.transparent)

    painter = QPainter(pixmap)
    painter.setPen(QColor(0, 0, 0))
    painter.setFont(QFont("Arial", 12))
    painter.drawText(pixmap.rect(), Qt.AlignCenter, "⛅")
    painter.end()

    return QIcon(pixmap)

def main():
    """Initialize the application and show the main window."""
    app = QApplication(sys.argv)
    window = weather_app.WeatherApp()

    window.setWindowIcon(create_window_icon())
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
