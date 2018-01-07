from modules.PackageManager import *

def requires(cfg):
	cfg.addPackageDependency("xorg-x11-server-Xorg", "i3", mgrtype=PackageManager.MANAGER_RPM)
	cfg.addPackageDependency("xserver-xorg", "i3", mgrtype=PackageManager.MANAGER_DPKG)

def configure(cfg):
	cfg.addLinkPath("~/.config/i3", "i3")

