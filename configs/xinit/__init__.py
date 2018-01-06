def requires(cfg):
        cfg.addPackageDependency("xorg-x11-xinit", "xorg-x11-drv-libinput")

def configure(cfg):
        cfg.addLinkFile("~/.xinitrc", "xinitrc")
