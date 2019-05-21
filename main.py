import ScreenCloud
import time, requests

from PythonQt.QtCore import QFile, QSettings, QUrl
from PythonQt.QtGui import QWidget, QDialog, QDesktopServices, QMessageBox
from PythonQt.QtUiTools import QUiLoader


class SCUploader():
	def __init__(self):
		self.uil = QUiLoader()
		self.loadSettings()

	def showSettingsUI(self, parentWidget):
		self.parentWidget = parentWidget
		self.settingsDialog = self.uil.load(QFile(workingDir + "/settings.ui"), parentWidget)
		self.settingsDialog.connect("accepted()", self.saveSettings)
		self.loadSettings()
		self.settingsDialog.group_url.input_address.text = self.url_address
		self.settingsDialog.open()

	def loadSettings(self):
		settings = QSettings()
		settings.beginGroup("uploaders")
		settings.beginGroup("scuploader")
		self.url_address = settings.value("url-address", "http://s.876974.ru/upload")
		settings.endGroup()
		settings.endGroup()

	def saveSettings(self):
		settings = QSettings()
		settings.beginGroup("uploaders")
		settings.beginGroup("scuploader")
		settings.setValue("url-address", self.settingsDialog.group_url.input_address.text)
		settings.endGroup()
		settings.endGroup()

	def isConfigured(self):
		self.loadSettings()
		return not(not self.url_address)

	def getFilename(self):
		return time.time()

	def upload(self, screenshot, name):
		self.loadSettings()
		url = self.url_address

		if not url.startswith('http'):
			ScreenCloud.setError('Invalid url!')
			return False

		timestamp = time.time()
		tmpFilename = QDesktopServices.storageLocation(QDesktopServices.TempLocation) + "/" + ScreenCloud.formatFilename(str(timestamp))
		screenshot.save(QFile(tmpFilename), ScreenCloud.getScreenshotFormat())

		reply = requests.post(url,
							  files={'image': open(tmpFilename, 'rb')}
							  ).json()

		try:
			ScreenCloud.setUrl(reply['href'])
		except Exception as e:
			ScreenCloud.setError("Could not upload to: " + self.url_address + "\nError: " + e.message)
			return False
		return True
