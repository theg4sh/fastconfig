
def requires(cfg):
	cfg.addPackageDependency("tmux")

def configure(cfg):
	cfg.addLinkFile("~/.tmux.conf", "tmux.conf")
