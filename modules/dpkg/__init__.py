import subprocess as sp

def formatInstall(packages):
        return "apt-get install -y {}".format(" ".join([p.name() for p in packages]))

def checkInstalled(package):
	out = sp.check_output(['/usr/bin/env', 'LANG=en', '/usr/bin/dpkg', '--status', package])
	for opt in out.decode('utf-8').strip().split('\n'):
		if opt.startswith('Status: '):
			return ' installed' in opt
	return False
	
