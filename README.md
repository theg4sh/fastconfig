# FastConfig

Configurator for freshly installed linux

# How to use

```
git clone https://github.com/theg4sh/fastconfig.git ~/.config/fastconfig
cd ~/.config/fastconfig
git submodule init
git submodule update --recursive
./install.py
```
### Config's callbacks

All callbacks should be declared in `configs/<config_name>/__init__.py`

- configure(cfg)

Contains list of `cfg.addLinkFile` and `cfg.addLinkPath` calls to linking configuration files from configs/<config_name> path to user's folders, e.g. `cfg.addLinkFile('~/.tmux.conf', 'tmux.conf')` from `configs/tmux` path will make a symlink `~/.tmux.conf` to `~/.config/fastconfig/configs/tmux/tmux.conf`
  
- install(cfg)

Installation callback to make specific actions for config. Default installation process will not be executed if config declare that callback. 
