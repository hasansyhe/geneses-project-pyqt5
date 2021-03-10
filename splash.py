# import libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import os

class main:
	def __init__(self):
		pathScreen = os.getcwd()
		self.app_spash = QApplication(sys.argv)
		screenImg = QPixmap(f"{pathScreen}/splash/spash.jpg")
		screenSplash = screenImg.scaled(500, 300)
		# create label
		label_screen_splash = QLabel("")
		# set img splash inside label
		label_screen_splash.setPixmap(screenSplash)
		# setting window
		label_screen_splash.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
		label_screen_splash.show()
		QTimer.singleShot(2000, self.app_spash.quit)
		sys.exit(self.app_spash.exec_())

if __name__ == '__main__':
	main()
