import os
from termcolor import colored

def current_path():
    return os.getcwd()

def change_colour(path, std_output, colour):
    if path.startswith(current_path()):
        print colored(std_output, colour)
    else:
        print std_output


change_colour("dsiufsdfihsd"+current_path(),"my test string",'red')

