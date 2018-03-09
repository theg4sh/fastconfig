#!/usr/bin/env python3
import os
import sys

PROJECT = "fastconfig"
if os.path.dirname(__file__) == '':
	sys.path.append('.')
	install_dir = '.'
else:
	install_dir = os.path.join(os.path.expanduser("~"), ".config", PROJECT)
	sys.path.append(install_dir)
	os.chdir(install_dir)

from modules.Path import *
from modules.PackageGroup import *
from modules.ConfigModule import *

install_dir = Path(install_dir)

def detectInstalled():
	abspath, exname = os.path.split(__file__)
	path = Path(abspath, name=exname)
	if path.dir() == '':
		return
	# FIXME: ~/.config/fastconfig is symlink
	if install_dir.absdir() not in [path.absdir(), path.dir()]:
		print("Please, run manually:")
		print(" cp -a {} {}".format(
			path.dir(),
			Path.FASTCONFIG_PATH))
		print("and rerun using {}/install.py".format(install_dir))
		exit(1)

def main():
	detectInstalled()
	install_dir.chdir()
	reserved_names = [PROJECT, '__init__.py', '__init__.pyc']
	configs_path = Path(install_dir, path="configs")
	configs = []
	for cfgname in os.listdir(configs_path.dir()):
		if cfgname in reserved_names:
			continue
		if '.' in cfgname:
			raise Exception("Dots is not allowed in config module's name: {}".format(cfgname))
		#cfgpath = os.path.join(configs_path, cfgname);
		cfgpath = Path(configs_path.reldir(), cfgname, name="__init__.py")
		if cfgpath.exists():
			configs.append(ConfigModule(cfgname, cfgpath, install_dir))

	pkgagg = PackageGroup()
	for cfg in configs:
		packages = cfg.requires()
		if packages is not None:
			pkgagg.add(packages)
	if not pkgagg.install():
		exit(0)

	for cfg in configs:
		cfg.configure()
	for cfg in configs:
		cfg.install()

if __name__ == "__main__":
	main()

# vim: ts=4 sw=4 noet
