import os
from importlib import import_module

class PackageManager:
	__MANAGER=None
	def __init__(self, manager):
		self._manager = manager

	def checkInstalled(self, package):
		return self._manager.checkInstalled(package)

	@classmethod
	def getManager(cls):
		if cls.__MANAGER is None:
			if os.path.exists('/usr/bin/dpkg'):
				cls.__MANAGER=PackageManager(import_module("modules.dpkg"))
			elif of.path.exists('/usr/bin/rpm'):
				cls.__MANAGER=PackageManager(import_module("modules.dpkg"))
		return cls.__MANAGER
