from modules.PathConfig import *
from modules.PathThirdparty import *

def requires(cfg):
    try:
        cfg.addPackageDependecy("vim-youcompleteme", mgrtype=PackageManager.MANAGER_DPKG);
    except:
        pass

def configure(cfg):
    cfg.addLinkPath("~/.vim", "vim")
    cfg.addLinkFile("~/.vimrc", "vimrc")

    cfg.addLinkPath(PathConfig(cfg.getConfigName(), name="vim/pack/plugins/start/vim-go"), PathThirdparty("vim-go"))
    cfg.addLinkPath(PathConfig(cfg.getConfigName(), name="vim/pack/plugins/start/typescript-vim"), PathThirdparty("typescript-vim"))
    #cfg.addLinkPath(PathConfig(cfg.getConfigName(), name="vim/syntax/python.vim"), PathThirdparty("vim-python-syntax", name="syntax/python.vim"))
    #cfg.addLinkPath(PathConfig(cfg.getConfigName(), name="vim/bundle/YouCompleteMe"), PathThirdparty("YouCompleteMe"))
    cfg.addLinkPath(PathConfig(cfg.getConfigName(), name="vim/bundle/Vundle.vim"), PathThirdparty("Vundle.vim"))


    cfg.addLinkFile(PathConfig(cfg.getConfigName(), name="vim/syntax/python.vim"), PathThirdparty("vim-python-syntax", name="syntax/python.vim"))

