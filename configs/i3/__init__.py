from modules.PackageManager import *

def requires(cfg):
    cfg.addPackageDependency("xorg-x11-server-Xorg", "i3",
            "pulseaudio-utils", "fontawesome-fonts", mgrtype=PackageManager.MANAGER_RPM)
    cfg.addPackageDependency("xserver-xorg", "i3",
            "pulseaudio-utils", mgrtype=PackageManager.MANAGER_DPKG)

    def configure(cfg):
        cfg.addLinkPath("~/.config/i3", "i3")


def postinstall(cfg):
    # TODO: install fontawesome if DPKS manager
    pass

# vim: ts=4 sw=4 noet
