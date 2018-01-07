import subprocess as sp

def formatInstall(packages):
        return "dnf install -y {}".format(" ".join([p.name() for p in packages]))

def checkInstalled(package):
        try:
            out = sp.check_output(['/usr/bin/env', 'LANG=en', '/usr/bin/rpm', '-q', package.name()])
            return True
        except Exception as e:
            return False

