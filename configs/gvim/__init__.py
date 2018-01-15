from modules.PathConfig import *
from modules.PathThirdparty import *

def configure(cfg):
    cfg.addLinkFile("~/.vimrc", "vimrc")
    cfg.addLinkPath("~/.vim", "vim")
    cfg.addLinkPath(PathConfig(cfg.getConfigName(), name="vim/pack/plugins/start/vim-go"), PathThirdparty("vim-go"))
    cfg.addLinkFile(PathConfig(cfg.getConfigName(), name="vim/syntax/python.vim"), PathThirdparty("vim-python-syntax", name="syntax/python.vim"))

