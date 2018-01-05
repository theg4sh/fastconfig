import os
import sys

from modules.ConfigModule import *

def main():
	reserved_names = ['fastconfig', '__init__.py']
	configs_path = os.path.join(os.path.dirname(sys.argv[0]), "configs")
	try:
		cfglist = [c for c in os.listdir(configs_path) if c not in reserved_names]
	except Exception as e:
		print(e)
		exit(1)
	configs = {}
	for cfgname in cfglist:
		cfgpath = os.path.join(configs_path, cfgname, "__init__.py");
		if os.path.exists(cfgpath):
			configs[cfgname] = ConfigModule(cfgname, cfgpath)
	for cfgname,cfg in configs.items():
		try:
			cfg.configure()
			cfg.install()
		except Exception as e:
			print(cfgname,e)
	#print(configs, cfglist)

if __name__ == "__main__":
	abspath = os.path.dirname(os.path.abspath(__file__))
	if abspath != os.path.expanduser("~/.config/fastconfig"):
		print("Please, run manually:")
		print(" cp -a {} {}".format(
			os.path.abspath(os.path.dirname(__file__)),
			os.path.expanduser("~/.config/fastconfig")))
		print("and rerun using ~/.config/fastconfig/install.py")
		exit(1)
	os.chdir(abspath)
	main()
