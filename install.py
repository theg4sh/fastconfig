#!/usr/bin/python3
import os
import sys

PROJECT = "fastconfig"
usrconfig_dir = os.path.expanduser("~/.config")
if os.path.dirname(__file__) == '':
	install_dir = '.'
else:
	install_dir = os.path.join(usrconfig_dir, PROJECT)
sys.path.append(install_dir)

from modules.ConfigModule import *
from modules.PackageGroup import *

def detectInstalled():
	relpath = os.path.dirname(__file__)
	if relpath == '':
		return
	abspath = os.path.dirname(os.path.abspath(__file__))
	# FIXME: symlink ~/.config/fastconfig
	if install_dir not in [abspath, relpath]:
		print("Please, run manually:")
		print(" cp -a {} {}".format(
			abspath,
			usrconfig_dir))
		print("and rerun using {}/install.py".format(install_dir))
		exit(1)

def main():
	detectInstalled()
	os.chdir(install_dir)
	reserved_names = [PROJECT, '__init__.py', '__init__.pyc']
	configs_path = "configs"
	cfglist = [c for c in os.listdir(os.path.join(install_dir, configs_path)) if c not in reserved_names]

	configs = []
	for cfgname in cfglist:
		if '.' in cfgname:
			raise Exception("Dots is not allowed in config module's name: {}".format(cfgname))
		cfgpath = os.path.join(configs_path, cfgname);
		if os.path.exists(os.path.join(cfgpath, "__init__.py")):
			configs.append(ConfigModule(cfgname, cfgpath, install_dir))

	pkgagg = PackageGroup()
	for cfg in configs:
		packages = cfg.requires()
		if packages is not None:
			pkgagg.add(packages)
	pkgagg.install()

	for cfg in configs:
		cfg.configure()
	for cfg in configs:
		cfg.install()

if __name__ == "__main__":
	main()
