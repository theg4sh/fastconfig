from .PackageManager import *

class Package:
	def __init__(self, name):
		self._name = name

	def name(self):
		return self._name

	def checkInstalled(self):
		return PackageManager.getManager().checkInstalled(self._name)
