from back import bg
from person import *
from bullet import *
from colorama import *

def checkIndex(in_x, in_y):
    obstacle = 'ok';
    if in_x < 2 or in_x + 2 > 32:
        obstacle = 'wall'
    return obstacle

def checkCoins(in_x, in_y):
    coins = 0
    for i in range(in_x, in_x + 3):
        for j in range(in_y, in_y + 3):
            if bg.canvas[i][j] == Fore.BLACK + Back.GREEN + Style.BRIGHT +"$"+ Style.RESET_ALL:
                coins += 1
    return coins

def checkObstacle(in_x, in_y):
    for i in range(in_x, in_x + 3):
        for j in range(in_y, in_y + 3):
            if bg.canvas[i][j] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"_"+ Style.RESET_ALL or bg.canvas[i][j] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"|"+ Style.RESET_ALL or bg.canvas[i][j] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"\\"+ Style.RESET_ALL :
                if in_x > 0 or in_x + 2 < 31:
                    return 1
    return -1

def checkMagnetRight(in_x, in_y):
    for i in range(1, 35):
        for j in range(in_y, in_y + 20):
            if bg.canvas[i][j] == Fore.WHITE + Back.RED + Style.BRIGHT +"M" +Style.RESET_ALL:
                return j
    return -1

def checkMagnetLeft(in_x, in_y):
    for i in range(1, 35):
        for j in range(in_y, in_y - 20):
            if bg.canvas[i][j] == Fore.WHITE + Back.RED + Style.BRIGHT +"M" +Style.RESET_ALL:
                return j
    return -1

def checkSpeedup(in_x, in_y):
    for i in range(in_x, in_x + 3):
        for j in range(in_y, in_y + 3):
            if bg.canvas[i][j] == 'S':
                return 1
    return -1
