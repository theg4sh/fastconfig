
def requires(cfg):
	cfg.addPackageDependency("i3blocks")

def configure(cfg):
	cfg.addLinkPath("~/.config/i3blocks", "i3blocks")
