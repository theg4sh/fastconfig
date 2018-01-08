import os
import sys
from modules.PackageManager import *
from modules.PathThirdparty import *
import subprocess as sp

def requires(cfg):
	cfg.addPackageDependency("fontconfig-devel", "libX11-devel",
            "libXft-devel", mgrtype=PackageManager.MANAGER_RPM)

def configure(cfg):
	cfg.addLinkFile(PathThirdparty("st", name="config.h").abspath(), "config.h");
	cfg.addLinkFile(PathThirdparty("st", name=".gitignore").abspath(), "gitignore");

def postinstall(cfg):
	make = "make -C {}".format(PathThirdparty("st").absdir())
	sys.stdout.write(make)
	sys.stdout.flush()
	sp.check_output(make, shell=True)
	print(" Done")
	print("root permission required for:")
	print()
	print("  {} install".format(make))
	print()
