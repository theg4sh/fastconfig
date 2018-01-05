#!/usr/bin/python3
import os
import sys

PROJECT = "fastconfig"
usrconfig_dir = os.path.expanduser("~/.config")
install_dir = os.path.join(usrconfig_dir, PROJECT)
sys.path.append(install_dir)

from modules.ConfigModule import *


def detectInstalled():
	relpath = os.path.dirname(__file__)
	if relpath == '':
		#relpath = os.environ.get('PWD')
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
	try:
		cfglist = [c for c in os.listdir(os.path.join(install_dir, configs_path)) if c not in reserved_names]
	except Exception as e:
		print(e)
		exit(1)

	configs = {}
	for cfgname in cfglist:
		if '.' in cfgname:
			raise Exception("Dots is not allowed in config module's name: {}".format(cfgname))
		cfgpath = os.path.join(configs_path, cfgname);
		if os.path.exists(os.path.join(cfgpath, "__init__.py")):
			configs[cfgname] = ConfigModule(cfgname, cfgpath, install_dir)
	for cfgname,cfg in configs.items():
		try:
			cfg.configure()
			cfg.install()
		except Exception as e:
			print(cfgname,e)
	#print(configs, cfglist)

if __name__ == "__main__":
	main()
