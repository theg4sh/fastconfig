
def requires(cfg):
	cfg.addPackageDependency("git")

def configure(cfg):
	cfg.addLinkFile("~/.gitignore_global", "gitignore_global")
	cfg.appendToConfig("~/.gitconfig", "gitconfig")

