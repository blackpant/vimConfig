import subprocess
import os
import shlex


pathpath = os.path.expanduser('~')

def install_tools():
    subprocess.check_call(["sudo", "apt-get", "install", "zsh"])
    subprocess.check_call(["sudo", "apt-get", "install", "guake"])
    subprocess.check_call(["sudo", "apt-get", "install", "vim-python-jedi"])
    subprocess.check_call(["sudo", "apt-get", "install", "Exuberant-ctags"])
    subprocess.check_call(["sudo", "apt-get", "install", "vim-nox"])

def install_OhMyZsh():
    cmd_arg2 = "sh -c \"$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)\""
    subprocess.check_call(cmd_arg2, shell=True)
    str_powerTheme = "git clone https://github.com/bhilburn/powerlevel9k.git ~/.oh-my-zsh/custom/themes/powerlevel9k"
    subprocess.check_call(str_powerTheme,shell=True)
    subprocess.os.system("cp .zshrc $HOME")


def install_VimSpf13():
    str_args  = "curl http://j.mp/spf13-vim3 -L -o - | sh"
    subprocess.check_call(str_args, shell=True)
    subprocess.os.system("cp .vimrc $HOME")
    subprocess.os.system("cp .vimrc.bundles $HOME")
    subprocess.check_call(["vim", "+PluginInstall", "+qall"])

def install_Guake():
    pass

def install_githubDepo():
    pass


def start():
    try:
        install_tools()
        install_VimSpf13()
        install_OhMyZsh()
        install_Guake()
        install_githubDepo()
    except Exception as e:
        print "Erreur lors de l'installation."
        print "Messages : %r." % e

start()
