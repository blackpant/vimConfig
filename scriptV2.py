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

returncode = 0
print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation de Guake."
print "--------------------------------------------------"

try:
	returncode = subprocess.call(["sudo", "apt-get", "install", "guake"])
except Exception:
	print "Une erreur est survenue.\nreturncode : %r" % returncode

returncode = 0

print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation de Python-pip + Exuberant-ctags."
print "--------------------------------------------------"

subprocess.call(["sudo", "apt-get", "install", "python-pip"])
subprocess.call(["sudo", "apt-get", "install", "Exuberant-ctags"])


print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation de Vim Spf13 + copie fichiers de configs."
print "--------------------------------------------------"

try:
	#returncode = subprocess.os.system("curl http://j.mp/spf13-vim3 -L -o - | sh")

    subprocess.call(["sudo", "apt-get", "install", "vim-nox"])
    subprocess.os.system("cp .vimrc $HOME")
    subprocess.os.system("cp .vimrc.bundles $HOME")
    subprocess.call(["vim", "+PluginInstall", "+qall"])

except Exception:
	print "Une erreur est survenue!!"
	print "(Spf13) returncode : %r" % returncode

returncode = 0
print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation de Zsh + OhMyZsh."
print "--------------------------------------------------"

