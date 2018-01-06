from modules.PackageManager import *

def requires(cfg):
	cfg.addPackageDependency("i3blocks", mgrtype=PackageManager.MANAGER_DPKG)
	cfg.addPackageDependency("xclip", "acpi", "alsa-utils")

def configure(cfg):
	cfg.addLinkPath("~/.config/i3blocks", "i3blocks")
