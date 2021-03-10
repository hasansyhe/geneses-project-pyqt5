# import libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class App(QWidget):
	def __init__(self):
		super().__init__()
		# set window title (unlix project)
		self.setWindowTitle("Unlix Project")
		# create main layout
		main_layout = QHBoxLayout()
		# set main_layout inside (window = self)
		self.setLayout(main_layout)


		# create left and right layout
		# left and right layouts most be (QVBoxLayout)
		left_layout = QVBoxLayout()
		right_layout = QVBoxLayout()
		# push layouts inside main_layout
		main_layout.addLayout(left_layout)
		main_layout.addLayout(right_layout)

		# create three layouts inside left layout
		top_layout = QVBoxLayout()
		center_layout = QHBoxLayout()
		bottom_layout = QHBoxLayout()

		# push this layouts inside left_layout
		left_layout.addLayout(top_layout)
		left_layout.addLayout(center_layout)
		left_layout.addLayout(bottom_layout)

if __name__ == '__main__':
	projram = QApplication(sys.argv)
	unlix = App()
	unlix.show()
	sys.exit(projram.exec_())