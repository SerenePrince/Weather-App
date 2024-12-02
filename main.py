import sys
import weather_app
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QColor, QFont
from PyQt5.QtCore import Qt

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = weather_app.WeatherApp()

    pixmap = QPixmap(32, 32)  
    pixmap.fill(Qt.transparent) 

    painter = QPainter(pixmap)
    painter.setPen(QColor(0, 0, 0)) 
    painter.setFont(QFont("Arial", 12))
    painter.drawText(pixmap.rect(), Qt.AlignCenter, "⛅") 
    painter.end()

    window.setWindowIcon(QIcon(pixmap))

    window.show()
    sys.exit(app.exec_())
