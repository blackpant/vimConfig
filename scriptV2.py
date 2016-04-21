import subprocess
import shlex 

print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation de Zsh."
print "--------------------------------------------------"

try :
	returncode = subprocess.call(["sudo", "apt-get", "install", "zsh"])
except Exception:
	print "Une erreur est survenue.\nreturncode : %r" % returncode

print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation de Guake."
print "--------------------------------------------------"

try:
	returncode = subprocess.call(["sudo", "apt-get", "install", "guake"])
except Exception:
	print "Une erreur est survenue.\nreturncode : %r" % returncode

print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation de Vim Spf13 + copie fichiers de configs."
print "--------------------------------------------------"

# curl http://j.mp/spf13-vim3 -L -o - | sh

print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation de Zsh."
print "--------------------------------------------------"

