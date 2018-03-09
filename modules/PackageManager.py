import os
from importlib import import_module

class PackageManager:
    __MANAGER=None

    MANAGER_ANY  = 0
    MANAGER_DPKG = 1
    MANAGER_RPM  = 2
    def __init__(self, mgrtype, manager):
        self._mgrtype = mgrtype
        self._manager = manager

    def checkMgrType(self, mgrtype):
        return mgrtype in [PackageManager.MANAGER_ANY, self._mgrtype]

    def _checkMgrType(self, package):
        return self.checkMgrType(package._mgrtype)

    def checkInstalled(self, package):
        if type(package).__name__ != 'Package' or self._checkMgrType(package):
            return self._manager.checkInstalled(package)
        else:
            return True

    def formatInstall(self, packages):
        return self._manager.formatInstall([p for p in packages if self._checkMgrType(p)])

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
