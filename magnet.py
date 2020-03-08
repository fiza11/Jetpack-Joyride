from back import bg
from random import randint
from colorama import *

class magnet:
    def __init__(self, x, y):
        bg.canvas[x][y] = Fore.WHITE + Back.RED + Style.BRIGHT +"M" +Style.RESET_ALL
