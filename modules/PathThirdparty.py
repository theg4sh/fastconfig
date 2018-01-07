import os
from modules.Path import Path

class PathThirdparty(Path):
    THIRDPARTY_BASE="thirdparty"

    def __init__(self, submodule, name=None):
        super(PathThirdparty, self).__init__(
            os.path.join(self.__class__.FASTCONFIG_BASE, self.__class__.THIRDPARTY_BASE),
            submodule, name)

