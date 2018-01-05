import os
import sys
from importlib import import_module

class ConfigModule:
	def __init__(self, name, path):
		self._pkg  = os.path.split(path)
		self._name = name
		self._cfgpath = self._pkg[0]
		self._basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
		self._module = None
		self._linkfiles = {}
		self._linkpaths = {}
		self._appendToConfigs = []

	def _getModule(self):
		if self._module is None:
			try:
				self._module = import_module(self._cfgpath.replace('/', '.'));
			except Exception as e:
				print(e)
				print("An error occured in config file: {0}".format(self._cfgpath))
				self._module = False
		if not hasattr(self._module, 'configure') and not hasattr(self._module, 'install'):
			raise Exception("Module {0} has no required definition of functions 'configure' and/or 'install'. Exit")
		return self._module

	def _makeLink(self, link, path):
		try:
			sys.stdout.write("Making link: {} -> {}".format(link, path))
			os.symlink(path, link)
			print("OK")
		except Exception as e:
			print(e)
			print("Failed")

	def _absConfigPath(self, path):
		filepath = os.path.join(self._basepath, self._cfgpath, path)
		if not os.path.exists(filepath):
			raise Exception("Config file or path {} does not exists".format(filepath))
		return filepath

	def addLinkFile(self, link, config):
		self._linkfiles[os.path.expanduser(link)] = self._absConfigPath(config)

	def addLinkPath(self, link, path):
		self._linkpaths[os.path.expanduser(link)] = self._absConfigPath(path)

	def appendToConfig(self, config, datafile):
		"""
		# DO NOT REMOVE appended from file {}
		<content>
		# END appended from file {}
		"""
		self._appendToConfigs.append([config, self._absConfigPath(datafile)])

	def configure(self):
		if not self._getModule():
			return False
		if hasattr(self._getModule(), 'configure'):
			try:
				self._getModule().configure(self)
			except Exception as e:
				print(e)
				print("An error occured while executing configuration for {0}".format(self._name))
				return False
		return True

	def install(self):
		if hasattr(self._getModule(), 'install'):
			self._getModule().install(self)
			return

		for link,filename in self._linkfiles.items():
			if os.path.exists(link):
				if os.path.islink(link):
					if os.readlink(link) != filename:
						print("Removed symlink {} -> {}".format(link, filename))
					os.unlink(link)
				elif os.path.isfile(link):
					print("File is exists {0}. To override that, please, run: rm -f '{0}'".format(link))
					continue
				elif os.path.isdir(link):
					print("Expected to make file symlink, but it's a directory located by path {}".format(link))
					continue
			sys.stdout.write("File: ")
			self._makeLink(link, filename)

		for link,filepath in self._linkpaths.items():
			if os.path.exists(link):
				if os.path.islink(link):
					if os.readlink(link) != filepath:
						print("Removed symlink {} -> {}".format(link, filepath))
					os.unlink(link)
				elif os.path.isfile(link):
					print("Expected to make path symlink, but it's a file located by path {}".format(link))
					continue
				elif os.path.isdir(link):
					print("Path is exists {0}. To override that, please, run: rm -rf '{0}'".format(link))
					continue
			sys.stdout.write("Directory: ")
			self._makeLink(link, filepath)

		for config,datafile in self._appendToConfigs:
			print("Append to {}: {}".format(config, datafile))

