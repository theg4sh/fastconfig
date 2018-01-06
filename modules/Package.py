from .PackageManager import *

class Package:
	def __init__(self, name, mgrtype=PackageManager.MANAGER_ANY):
		self._name = name
		self._mgrtype = mgrtype

	def name(self):
		return self._name

	def checkInstalled(self):
		return PackageManager.getManager().checkInstalled(self)
