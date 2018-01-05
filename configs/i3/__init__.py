
def requires(cfg):
	cfg.addPackageDependency("i3-wm")

def configure(cfg):
	cfg.addLinkPath("~/.config/i3", "i3")

