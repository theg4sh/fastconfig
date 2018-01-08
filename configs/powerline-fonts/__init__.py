import sys
from modules.PathThirdparty import *
import subprocess as sp

def install(cfg):
	sys.stdout.write("Installing powerline-fonts...")
	sys.stdout.flush()
	# FIXME: already installed fonts
	pfpath = PathThirdparty("powerline-fonts")
	owd = pfpath.chdir()
	sp.check_output("./install.sh")
	print(" Done")

	sys.stdout.write("Running fc-cache...")
	sys.stdout.flush()
	sp.check_output("fc-cache")
	print(" Done")

	os.chdir(owd)
