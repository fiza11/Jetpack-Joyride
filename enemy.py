from person import *
from back import bg
from character import *
from bullet import *

enem = [['E' for i in range(6)] for j in range(10)]

with open('enemy.txt') as f:
    en = f.readlines()
en = [row.rstrip('\n') for row in en]

def ebullets(x, y):
    ecoor_y.append(y - 3)
    ecoor_x.append(x)
    esrc_x = x
    esrc_y = y - 3
    ebulletFlag.append(1)
    # temp.canvas[esrc_x][esrc_y] = bg.canvas[esrc_x][esrc_y]
    # temp.canvas[esrc_x][esrc_y - 1] = bg.canvas[esrc_x][esrc_y - 1]
    # bg.canvas[esrc_x][esrc_y] = Fore.WHITE + Back.BLACK + Style.BRIGHT +"="+ Style.RESET_ALL
    # bg.canvas[esrc_x][esrc_y - 1] = Fore.WHITE + Back.BLACK + Style.BRIGHT +"<"+ Style.RESET_ALL

class enemy(Character):

    def __init__(self):
        Character.__init__(self)
        self.lives = 15
        self.posx = 20
        self.posy = 1590
        for i in range(len(en)):
            for j in range(len(en[i])):
                bg.canvas[self.posx + i][self.posy + j] = en[i][j]

Boss = enemy()
