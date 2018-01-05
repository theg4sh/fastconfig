import subprocess as sp

def checkInstalled(package):
	out = sp.check_output(['/usr/bin/env', 'LANG=en', '/usr/bin/rpm', package])
	#for opt in out.decode('utf-8').strip().split('\n'):
	#	if opt.startswith('Status: '):
	#		return ' installed' in opt
	return False

