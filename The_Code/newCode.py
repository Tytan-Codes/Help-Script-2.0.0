import os
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import argparse
#args
parser = argparse.ArgumentParser(description='This is a script that will make your day faster.')
args = parser.parse_args()
#added another comment

#Defs

def ChooseOS():
    ChooseOS = str(input(f'{Fore.GREEN}What Operating System are you using, Linux, Mac or Windows? cAsE SeNsItIvE: '))
    os.system('cls')

    





#Defs


ChooseOS()