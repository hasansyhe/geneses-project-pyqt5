# import libraries
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import os
from guilib import *

class QShahed(QWidget):
	def __init__(self, log):
		self.path = os.getcwd()
		self.logs_area = log
		super().__init__()
		# create main_layout
		main_layout_boot = QVBoxLayout()
		# add layout to self
		self.setLayout(main_layout_boot)
		self.setWindowOpacity(0.5)

		# create hints box to help user
		hint_box = QGroupBox("Hints")
		# layout inside hint_box
		layout_hints_box = QVBoxLayout()
		hint_box.setLayout(layout_hints_box)
		# labels inside hints layout
		text1 = "You can use this buttons to boot your device to any boot mode you want"
		text2 = "This functions will help you to controling your device"
		# labels
		hint_one = QLabel("<font size='2'>You can see blow two part of actions</font>")
		hint_two = QLabel(f"<font size='2'><b>Boot Actions : </b>{text1}</font>")
		hint_three = QLabel(f"<font size='2'><b>Control Actions : </b>{text2}</font>")

		list_hints = [hint_one, hint_two, hint_three]
		for hint_element in list_hints:
			layout_hints_box.addWidget(hint_element)
		# add hint_bot to main_layout_boot
		main_layout_boot.addWidget(hint_box)

		# create to parts for actions buttons
		# but first we need layout (QHBoxLayout)
		actions_buts_layout = QHBoxLayout()
		# add actions_buts_layout to main_layout_boot
		main_layout_boot.addLayout(actions_buts_layout)

		# create two groupbox
		left_box = QGroupBox("Boot Actions")
		right_box = 	QGroupBox("Control Actions")
		# layouts nside left and right boxs
		left_box_layout = QVBoxLayout()
		right_box_layout = QVBoxLayout()
		# add layouts
		left_box.setLayout(left_box_layout)
		right_box.setLayout(right_box_layout)
		# add left and right boxs to actions_buts_layout
		actions_buts_layout.addWidget(left_box)
		actions_buts_layout.addWidget(right_box)

		# boot buttons
		reboot_button = QPushButton("Reboot")
		recovery_button = QPushButton("Recovery")
		download_button = QPushButton("Download")
		poweroff_button = QPushButton("Shutdown")
		bootloader_button = QPushButton("Bootloader")
		empty_label_button = QLabel()
		# events
		reboot_button.clicked.connect(self.reboot_function)
		recovery_button.clicked.connect(self.recovery_function)
		download_button.clicked.connect(self.download_function)
		poweroff_button.clicked.connect(self.poweroff_function)
		bootloader_button.clicked.connect(self.bootloader_function)

		# add button to left_box_layout (using for loop)
		list_boot_buttons = [reboot_button ,recovery_button, download_button, poweroff_button, bootloader_button]
		for but_element_zero in list_boot_buttons:
			# styling buttons
			but_element_zero.setStyleSheet("height:25px;")
			left_box_layout.addWidget(but_element_zero)
		left_box_layout.addWidget(empty_label_button)

		# control buttons
		function_one = QPushButton("Read Info")
		function_two = QPushButton("Enable WIFI")
		function_three = QPushButton("Disable WIFI")
		function_four = QPushButton("Bootanimation")
		function_five = QPushButton("None")
		function_six = QPushButton("None")
		function_sivn = QPushButton("None")
		# event
		function_one.clicked.connect(self.function_getinfo)
		function_two.clicked.connect(self.function_wifi_en)
		function_three.clicked.connect(self.function_wifi_dis)
		function_four.clicked.connect(self.function_bootanimation)

		list_control_buttons = [function_one, function_two, function_three, function_four, function_five,
		function_six, function_sivn]
		for but_element_one in list_control_buttons:
			# styeling buttons
			but_element_one.setStyleSheet("height:25px;")
			right_box_layout.addWidget(but_element_one)
		# create empty label
		empty_label = QLabel()
		main_layout_boot.addWidget(empty_label)

	"""
	here you will see all functions to boot actions or control actions
	-> keys <-
	# shahed
	# fatima
	# lara
	# maryam
	# amal

	"""
	def reboot_function(self):
		self.logs_area.clear()
		self.logs_area.appendPlainText("starting adb deamon ...")
		os.system("adb devices")
		self.logs_area.appendPlainText("starting rebooting ...")
		os.system("adb shell reboot")
		self.logs_area.appendPlainText("Done [CODE: reboot system]")


	def recovery_function(self):
		self.logs_area.clear()
		self.logs_area.appendPlainText("starting adb deamon ...")
		os.system("adb devices")
		self.logs_area.appendPlainText("starting rebooting ...")
		os.system("adb shell reboot recovery")
		self.logs_area.appendPlainText("Done [CODE: recovery mode]")

	def download_function(self):
		self.logs_area.clear()
		self.logs_area.appendPlainText("starting adb deamon ...")
		os.system("adb devices")
		self.logs_area.appendPlainText("starting rebooting ...")
		os.system("adb shell reboot download")
		self.logs_area.appendPlainText("Done [CODE: download mode]")
	def poweroff_function(self):
		self.logs_area.clear()
		self.logs_area.appendPlainText("starting adb deamon ...")
		os.system("adb devices")
		self.logs_area.appendPlainText("starting rebooting ...")
		os.system("adb shell reboot -p")
		self.logs_area.appendPlainText("Done [CODE: shutdown system]")

	def bootloader_function(self):
		self.logs_area.clear()
		self.logs_area.appendPlainText("starting adb deamon ...")
		os.system("adb devices")
		self.logs_area.appendPlainText("starting rebooting ...")
		os.system("adb shell reboot bootloader")
		self.logs_area.appendPlainText("Done [CODE: bootloader mode]")


	def function_getinfo(self):
		self.logs_area.clear()
		self.logs_area.appendPlainText("starting adb deamon ...")
		os.system("adb devices")
		self.logs_area.appendPlainText("adb deamon [Running]... Done")
		self.logs_area.appendPlainText("Push getinfo script ...")
		os.system(f"adb push {self.path}/script/getinfo.sh /sdcard")
		self.logs_area.appendPlainText("executeing getinfo script ...")
		os.system("adb shell sh /sdcard/getinfo.sh")
		self.logs_area.appendPlainText("Pull info file ...")
		os.system(f"adb pull /sdcard/info.txt {self.path}/dump")
		self.logs_area.appendPlainText("Display Info ...")
		info_file = open(f"{self.path}/dump/info.txt", "r")
		info_to_display = info_file.read()
		info_file.close()
		self.logs_area.appendPlainText(info_to_display)
		self.logs_area.appendPlainText("Done")
		os.system(f"rm {self.path}/dump/info.txt")
	def function_wifi_en(self):
		self.logs_area.clear()
		self.logs_area.appendPlainText("starting adb deamon ...")
		os.system("adb devices")
		self.logs_area.appendPlainText("starting wifi ...")
		os.system("adb shell svc wifi enable")

	def function_wifi_dis(self):
		self.logs_area.clear()
		self.logs_area.appendPlainText("starting adb deamon ...")
		os.system("adb devices")
		self.logs_area.appendPlainText("stopping wifi ...")
		os.system("adb shell svc wifi disable")

	def function_bootanimation(self):
		self.logs_area.clear()
		self.logs_area.appendPlainText("starting adb deamon ...")
		os.system("adb devices")
		self.logs_area.appendPlainText("starting Bootanimation ...")
		os.system("adb shell bootanimation")

class QMaryam(QWidget):
	def __init__(self):
		self.path = os.getcwd()
		super().__init__()
		# create main layout
		setting_main_layout = QVBoxLayout()
		# set main layout inside self
		self.setLayout(setting_main_layout)
		developer = "or you can active developers edition of this project to see more options [IMEI Tab] or [Backup Tab]"
		setting_hint_text = QLabel(f"<font size='2'>You can change themes and project language <br> {developer}</font> ")
		setting_hints_box = QGroupBox("Hints")
		setting_main_layout.addWidget(setting_hints_box)
		layout_hints_text = QHBoxLayout()
		setting_hints_box.setLayout(layout_hints_text)
		layout_hints_text.addWidget(setting_hint_text)

		themes_items_box = QGroupBox("Themes")
		setting_main_layout.addWidget(themes_items_box)
		# create layout inside themes_items_box
		layout_themes = QVBoxLayout()
		# set this layout inside themes_items_box
		themes_items_box.setLayout(layout_themes)
		# themes combobox
		themes_combobox = QComboBox()
		themes_combobox.setStyleSheet("height:25px;")
		# add combobox 
		list_theme = QStyleFactory.keys()
		layout_themes.addWidget(themes_combobox)
		for theme in list_theme:
			themes_combobox.addItem(theme)
		# create buuton
		apply_button = QPushButton("Apply")
		apply_button.setStyleSheet("height:20px;")
		# add button
		layout_themes.addWidget(apply_button)

		# developer box
		developer_box = QGroupBox("Active Developer Eidtion")
		setting_main_layout.addWidget(developer_box)
		# layout inside Developer box
		developer_box_layout = QHBoxLayout()
		# add layout to box
		developer_box.setLayout(developer_box_layout)
		# keys
		key_one = QLineEdit()
		key_tow = QLineEdit()
		key_three = QLineEdit()
		key_four = QLineEdit()
		but_active = QPushButton("Enable")
		list_keys = [key_one, key_tow, key_three, key_four]
		for key_element in list_keys:
			key_element.setPlaceholderText("N 0 F 0")
			developer_box_layout.addWidget(key_element)
		developer_box_layout.addWidget(but_active)


		# empty label inside setting_main_layout
		empty_label_setting = QLabel()
		# add this label
		setting_main_layout.addWidget(empty_label_setting)

class QImei(QWidget):
	def __init__(self):
		super().__init__()
		pass

class QBackup(QWidget):
	def __init__(self):
		super().__init__()
		pass
