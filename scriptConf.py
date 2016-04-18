#import
import subprocess
#installation de zsh
#a mettre dans le script de commande admin scriptAd.py
#j'ai dis de la merde, juste a lancer la commande
    #subprocess.call(["sudo", "apt-get", "update"])
#sudo apt-get install zsh -> subprocess.call(["sudo", "apt-get", "install zsh"])

codeReturn = subprocess.call(["sudo", "apt-get", "install", "zsh"])
if codeReturn == 0:
    print "Installation de Zsh : OK"
else :
    print "(Zsh)Installation Erreur, n\'a pas pu s\'installer."

#installation de Oh My Zsh
#besoin detre sudo ou pas ?!
#comand au complet :
#sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

cmd = "sh"
cmd_arg = "-c"
cmd_arg2 = "\"$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)\""

#codeReturn = subprocess.call([cmd, cmd_arg, cmd_arg2])
codeReturn = subprocess.os.system(cmd + " " + cmd_arg +" "+cmd_arg2)
if codeReturn == 0 :
    print "Installation de OhMyZsh : OK"
else :
    print "(OhMyZsh)Installation Erreur, n\'a pas pu s\'installer."

#changement de shell
#sudo chsh -s /bin/zsh
cmd = "sudo"
cmd_arg = "chsh"
cmd_arg2 = "-s"
cmd_arg3 = "/bin/zsh"

codeReturn = subprocess.call([cmd, cmd_arg, cmd_arg2, cmd_arg3])

if codeReturn == 0 :
    print "(Shell) Changement de shell : OK"
else :
    print "(OhMyZsh)Changement de shell Erreur, n\'a pas pu etre effectue."


#avant verifier que le dossier ~/.oh-my-zsh/custom/themes/ existe bien, si non, le creer
#appel d'un script pour une command admin,
#ls ~/.oh-my-zsh/custom/ , voir si le dossier themes existe.
cmd = "ls"
cmd_arg = "~/.oh-my-zsh/custom/"
strRes = subprocess.check_output([cmd, cmd_arg])
dirIWant = "themes"

if dirIWant in strRes:
    print "~/.oh-my-zsh/custom/themes/ Already exist. OK"
else :
    print "the ~/.oh-my-zsh/custom/themes/ does not exist."
    codeReturn = subprocess.call(["mkdir","~/.oh-my-zsh/custom/themes/"])
    if codeReturn == 0:
        print "(Themes) Directory successfully created. OK"
    else :
        print "(Themes) Failed to created the ~/.oh-my-zsh/custom/themes/ directory."


# #
# #installation du theme ohmyzsh powerlevel9k
# git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k

# #application du theme
# #code python
# #Trouver la ligne avec "ZSH_THEME" est changer le theme par "powerlevel9k"

# #copie de mon fichie de config .zshrc
# #code

# #download guake
# sudo apt-get install guake

# #download tomorrow night theme for guake
# git clone https://github.com/carwin/guake-tomorrow-night

# #installation guake-tomorrow-night
# cd guake-tomorrow-night
# ./set_tomorrow_night.sh
# #retour dans $HOME
# cd ~

# #telechargement de la configuration spf13 vim et installation
# curl http://j.mp/spf13-vim3 -L -o - | sh
# #telechargement de mes fichiers de config vimConfig
# cd ~/Documents/
# git clone https://github.com/blackpant/vimConfig

# #copier/coller de mes fichiers de configs pour qu'ils soient pris en compte
# cp ~/Documents/vimConfig/.vimrc ~  && cp ~/Documents/vimConfig/.vimrc.bundles ~

# #installation verification update des bundle de VIM
# vim +BundleInstall! +BundleClean +q



