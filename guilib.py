# import libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from tablib import *
import os

class App(QWidget):
	def __init__(self):
		super().__init__()
		# path project
		self.pathProject = os.getcwd()
		# display text inside logs area to help
		text_display = open(f"{self.pathProject}/display.txt")
		self.display_notes = text_display.read()
		text_display.close()


		# set window title (unlix project)
		self.setWindowTitle("GENESES Beta 1.17")
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

		# add functions
		self.event_list(parent=top_layout)
		self.logs_area(parent=right_layout)
		self.tab_functions(parent=center_layout)
		self.progress_line(parent=bottom_layout)

		# end
	def event_list(self, parent):
		self.keyevent_list = ["Home", "Back", "All Apps"]
		# create labelframe
		event_box_port = QGroupBox("Events Code : does not Work")
		# add this labelframe to his parent
		parent.addWidget(event_box_port)
		# create layout inside com_box_port
		layout_list_event = QVBoxLayout()
		event_box_port.setLayout(layout_list_event)

		# create combobox (2 items)
		event_combobox = QComboBox()
		event_combobox.setStyleSheet("height:25px;outline:none;")
		event_combobox.addItem("select event to send")
		for keyevent_element in self.keyevent_list:
			event_combobox.addItem(keyevent_element)

		send_button = QPushButton("Send")
		send_button.setStyleSheet("width:20px;")
		# add combobox and button to layout_list_event
		layout_list_event.addWidget(event_combobox)
		layout_list_event.addWidget(send_button)

	def tab_functions(self, parent):
		# create notebook widget
		notebook = QTabWidget()
		# add notebook to parent
		parent.addWidget(notebook)
		# create tabs widgets
		boot_tab = QShahed(log=self.log_area_widget)
		repair_tab = QWidget()
		screen_tab = QWidget()
		setting_tab = QWidget()
		# add this tabs to our notebook
		notebook.addTab(boot_tab, "Boot")
		notebook.addTab(repair_tab, "Repair")
		notebook.addTab(screen_tab, "Screen")
		notebook.addTab(setting_tab, "Settings")

	def logs_area(self, parent):

		# create label frame for log widget (QLineTextEeit)
		logs_box = QGroupBox("Log Window")
		# add labelframe to parent
		parent.addWidget(logs_box)
		# create layout
		log_layout = QHBoxLayout()
		# add layout to logs_box
		logs_box.setLayout(log_layout)
		# create log area
		self.log_area_widget = QPlainTextEdit()
		# display text inside it
		self.log_area_widget.appendPlainText(self.display_notes)
		# set log area just for read
		self.log_area_widget.setReadOnly(True)
		log_layout.addWidget(self.log_area_widget)

		# style
		self.log_area_widget.setStyleSheet("width:400px;font-size:15px;color:#c0c0c0;")

		# scrollbar
		scroll_bar = QScrollBar()
		scroll_bar.setStyleSheet("width:10px;")
		self.log_area_widget.setVerticalScrollBar(scroll_bar)

		# print(QStyleFactory.keys())

	def progress_line(self, parent):
		# progress  layout
		self.progressbar_layout = QHBoxLayout()
		parent.addLayout(self.progressbar_layout)

		# progressbar widget
		self.progress_bar = QProgressBar()
		self.progressbar_layout.addWidget(self.progress_bar)

def run():
	program = QApplication(sys.argv)
	unlix = App()
	unlix.show()
	program.setStyle("cleanlooks")
	sys.exit(program.exec_())