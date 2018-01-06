import os
from importlib import import_module

class PackageManager:
	__MANAGER=None

	MANAGER_DPKG=1
	MANAGER_RPM=2
	def __init__(self, mgrtype, manager):
		self._mgrtype = mgrtype
		self._manager = manager

	def checkInstalled(self, package):
		return self._manager.checkInstalled(package)

	def formatInstall(self, packages):
		return self._manager.formatInstall(packages)

	@classmethod
	def getManager(cls):
		if cls.__MANAGER is None:
			if os.path.exists('/usr/bin/dpkg'):
				cls.__MANAGER=PackageManager(cls.MANAGER_DPKG, import_module("modules.dpkg"))
			elif os.path.exists('/usr/bin/rpm'):
				cls.__MANAGER=PackageManager(cls.MANAGER_RPM,  import_module("modules.rpm"))
			else:
				raise Exception("Unknown OS manager")
		return cls.__MANAGER
