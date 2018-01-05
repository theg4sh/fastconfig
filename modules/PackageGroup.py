from .Package import *

class PackageGroup:
	def __init__(self):
		self._packages = {}
		self._installed = {}

	def add(self, *pkgs):
		for p in pkgs:
			if type(p) == str:
				self._packages[p] = Package(p)
			elif type(pkgs) == list:
				for _p in p:
					self.add(_p)
			elif type(p).__name__ == 'Package':
				self._packages[p.name()] = p
			elif type(p).__name__ == 'PackageGroup':
				self.add(*p._packages.values())
			else:
				raise Exception("Package type {0} is unsupported".format(type(p)))

	def items(self):
		return self._packages.items()

	def notInstalled(self):
		for pkg in self._packages.values():
			if not pkg.checkInstalled():
				yield pkg

	def install(self):
		pkglist = list(self.notInstalled())
		if not pkglist:
			return

		print("Package installation is not implemented yet. Please, run manually:")
		print()
		print("  dnf install -y {}".format(" ".join([p.name() for p in plglist])))
		print()
