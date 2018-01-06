
def requires(cfg):
	cfg.addPackageDependency("i3blocks", "xclip", "acpi", "alsa-utils")

def configure(cfg):
	cfg.addLinkPath("~/.config/i3blocks", "i3blocks")
