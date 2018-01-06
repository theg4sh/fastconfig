
def requires(cfg):
	cfg.addPackageDependency("xorg-server-x11-Xorg", "i3")

def configure(cfg):
	cfg.addLinkPath("~/.config/i3", "i3")

