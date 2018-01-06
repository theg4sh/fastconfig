from modules.PackageManager import *

def requires(cfg):
        cfg.addPackageDependency("xorg-x11-xinit", "xorg-x11-drv-libinput", mgrtype=PackageManager.MANAGER_RPM)
        cfg.addPackageDependency("xinit", "xserver-xorg", mgrtype=PackageManager.MANAGER_DPKG)

def configure(cfg):
        cfg.addLinkFile("~/.xinitrc", "xinitrc")
