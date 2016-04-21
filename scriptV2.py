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

subprocess.call(["sudo", "apt-get", "install", "vim-python-jedi"])
subprocess.call(["sudo", "apt-get", "install", "Exuberant-ctags"])


print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation de Vim Spf13 + copie fichiers de configs."
print "--------------------------------------------------"

# try:

    # returncode = subprocess.os.system("curl http://j.mp/spf13-vim3 -L -o - | sh")

    # subprocess.call(["sudo", "apt-get", "install", "vim-nox"])
    # subprocess.os.system("cp .vimrc $HOME")
    # subprocess.os.system("cp .vimrc.bundles $HOME")
    # subprocess.call(["vim", "+PluginInstall", "+qall"])

# except Exception:
	# print "Une erreur est survenue!!"
	# print "(Spf13) returncode : %r" % returncode

# returncode = 0
print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation de  OhMyZsh."
print "--------------------------------------------------"

cmd_arg2 = "sh -c \"$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)\""

args = shlex.split(cmd_arg2)
print "Commande : \n%r" % args
codeReturn = subprocess.os.system(cmd_arg2)

subprocess.os.system("cd ~/.oh-my-zsh/custom && mkdir themes")

ha = "git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k"

toto = subprocess.os.system(ha)

#installation powerline-fonts
#installation via https://github.com/powerline/fonts et ensuite lancer ./install.sh

subprocess.call(["cd", "~/Documents/"])
subprocess.call(["git", "clone", "https://github.com/powerline/fonts"])
subprocess.call(["cd","fonts", "&&", "./install.sh"])


#installation guake-tomorrow-night
#changement de theme guake,
    # ./set_tomorrow_night.sh

subprocess.call(["git", "clone", "https://github.com/carwin/guake-tomorrow-night"])
subprocess.call(["cd", "quake-tomorrow-night"])
subprocess.call((["./set_tomorrow_night.sh"])

#changement de la police de Guake par une de Powerline.
#Meslo* est pas mal.
