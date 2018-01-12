import os
from modules.Path import Path

class PathConfig(Path):
    CONFIGS_BASE="configs"

    def __init__(self, config, name=None):
        super(PathConfig, self).__init__(
            os.path.join(self.__class__.FASTCONFIG_BASE, self.__class__.CONFIGS_BASE),
            config, name)
