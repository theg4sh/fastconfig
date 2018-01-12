import os

class Path:
    FASTCONFIG_BASE="~/.config/fastconfig"

    def __init__(self, basepath, path=None, name=None):
        self._basepath = basepath if type(basepath) == str else str(basepath)
        self._path     = path
        self._name     = name

    def __str__(self):
        return os.path.join(os.path.expanduser(self._basepath),
            self._path if self._path is not None else "",
            self._name if self._name is not None else "")

    def name(self):
        return self._name

    def reldir(self):
        return self._path

    def dir(self):
        return os.path.join(self._basepath,
            self._path if self._path is not None else "")

    def absdir(self):
        return os.path.abspath(os.path.expanduser(self.dir()))

    def abspath(self):
        return os.path.join(self.absdir(), self._name)

    def chdir(self):
        owd = os.getcwd()
        os.chdir(self.absdir())
        return owd

    def join(self, *paths):
        path = self._path if self._path is not None else ""
        for p in paths:
            if type(p) == str:
                path = os.path.join(path, p)
            else:
                raise Exception("Paths could be joined only with str type")
        return Path(self._basepath, path=path if path != "" else None, name=self._name)

    def exists(self):
        return os.path.exists(str(self))

# vim: ts=4 sw=4 et
