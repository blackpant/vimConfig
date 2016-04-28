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

try:

    returncode = subprocess.os.system("curl http://j.mp/spf13-vim3 -L -o - | sh")

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
print "Installation de  OhMyZsh."
print "--------------------------------------------------"

cmd_arg2 = "sh -c \"$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)\""

args = shlex.split(cmd_arg2)
print "Commande : \n%r" % args
codeReturn = subprocess.os.system(cmd_arg2)

try:
    subprocess.os.system("cd ~/.oh-my-zsh/custom && mkdir themes")
except Exception :
    print "Dossier deja existant ou erreur lors de la creation du dossier."

print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation du Theme OhMyZsh Powerlevel9k."
print "--------------------------------------------------"

ha = "git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k"

toto = subprocess.os.system(ha)
subprocess.os.system("cp .zshrc $HOME")
print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation de Powerline Fonts."
print "--------------------------------------------------"

#installation powerline-fonts
#installation via https://github.com/powerline/fonts et ensuite lancer ./install.sh
# commandes :
# git clone https://github.com/powerline/fonts $HOME/Documents/fonts
# $HOME/Documents/fonts/./install.sh

powerArgs = "git clone https://github.com/powerline/fonts $HOME/Documents/fonts"
powerList = shlex.split(powerArgs)
subprocess.call([powerList])

subprocess.call(["$HOME/Documents/fonts/./install.sh"])

print "--------------------------------------------------"
print "--------------------------------------------------"
print "Installation de Guake Tomorrow Night Theme."
print "--------------------------------------------------"

#installation guake-tomorrow-night
#changement de theme guake,
    # ./set_tomorrow_night.sh

subprocess.call(["git", "clone", "https://github.com/carwin/guake-tomorrow-night"])
subprocess.call(["cd", "quake-tomorrow-night"])
subprocess.call(["./set_tomorrow_night.sh"])
