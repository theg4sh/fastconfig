import sys
from modules.PathThirdparty import *
import subprocess as sp

def install(cfg):
    sys.stdout.write("Installing powerline-fonts")
    # FIXME: already installed fonts
    pfpath = PathThirdparty("powerline-fonts")
    owd = pfpath.chdir()
    sp.check_output("./install.sh")
    print(" Done")
    os.chdir(owd)
