from back import bg, temp
from person import *
from colorama import *

coor_x = []
coor_y = []
bulletFlag = []
ecoor_x = []
ecoor_y = []
ebulletFlag = []

def moveBullet(k) :
    y = 0
    for i in range(len(coor_x)):
        if coor_y[i] < 150 + k and bulletFlag[i] :
            bg.canvas[coor_x[i]][coor_y[i]] = temp.canvas[coor_x[i]][coor_y[i]]
            bg.canvas[coor_x[i]][coor_y[i] + 1] = temp.canvas[coor_x[i]][coor_y[i] + 1]
            for j in range (1, 5) :
                temp.canvas[coor_x[i]][coor_y[i] + j] = bg.canvas[coor_x[i]][coor_y[i] + j]
            if bg.canvas[coor_x[i]][coor_y[i] + 1] == '/' or bg.canvas[coor_x[i]][coor_y[i] + 1] == '(' or bg.canvas[coor_x[i]][coor_y[i] + 1] == 'V':
                y = 1
            clearObstacles(coor_x[i], coor_y[i] + 1)
            clearObstacles(coor_x[i], coor_y[i] + 2)
            clearObstacles(coor_x[i], coor_y[i] + 3)
            clearObstacles(coor_x[i], coor_y[i] + 4)
            coor_y[i] += 3
            bg.canvas[coor_x[i]][coor_y[i]] = Fore.WHITE + Back.BLACK + Style.BRIGHT +"="+ Style.RESET_ALL
            bg.canvas[coor_x[i]][coor_y[i] + 1] = Fore.WHITE + Back.BLACK + Style.BRIGHT +">"+ Style.RESET_ALL
        else :
            bulletFlag[i] = 0
            bg.canvas[coor_x[i]][coor_y[i]] = temp.canvas[coor_x[i]][coor_y[i]]
            bg.canvas[coor_x[i]][coor_y[i] + 1] = temp.canvas[coor_x[i]][coor_y[i] + 1]
    return y

def checkDiagonal(x , y):
    co_x = x
    co_y = y
    while(bg.canvas[co_x][co_y] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"\\"+ Style.RESET_ALL):
        bg.canvas[co_x][co_y] = ' '
        co_x -= 1
        co_y -= 1
    co_x = x + 1
    co_y = y + 1
    while(bg.canvas[co_x][co_y] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"\\"+ Style.RESET_ALL):
        bg.canvas[co_x][co_y] = ' '
        co_x += 1
        co_y += 1
    co_x = x
    co_y = y + 1
    while(bg.canvas[co_x][co_y] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"\\"+ Style.RESET_ALL):
        bg.canvas[co_x][co_y] = ' '
        co_x += 1
        co_y += 1
    co_x = x - 1
    co_y = y
    while(bg.canvas[co_x][co_y] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"\\"+ Style.RESET_ALL):
        bg.canvas[co_x][co_y] = ' '
        co_x -= 1
        co_y -= 1

def clearObstacles(co_x, co_y):
    tem_x = co_x
    tem_y = co_y
    for i in range(-3 , 4) :
        checkDiagonal(co_x + i , co_y + i)
    while(bg.canvas[co_x][co_y] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"|"+ Style.RESET_ALL):
        bg.canvas[co_x][co_y] = ' '
        co_x -= 1
    co_x = tem_x + 1
    while(bg.canvas[co_x][co_y] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"|"+ Style.RESET_ALL):
        bg.canvas[co_x][co_y] = ' '
        co_x += 1
    co_x = tem_x - 1
    while(bg.canvas[co_x][co_y + 1] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"|"+ Style.RESET_ALL):
        bg.canvas[co_x][co_y + 1] = ' '
        co_x -= 1
    co_x = tem_x + 1
    while(bg.canvas[co_x][co_y + 1] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"|"+ Style.RESET_ALL):
        bg.canvas[co_x][co_y + 1] = ' '
        co_x += 1

    co_x = tem_x
    co_y = tem_y

    while(bg.canvas[co_x][co_y] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"_"+ Style.RESET_ALL):
        bg.canvas[co_x][co_y] = ' '
        co_y += 1
    co_y = tem_y

    while(bg.canvas[co_x - 1][co_y] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"_"+ Style.RESET_ALL):
        bg.canvas[co_x - 1][co_y] = ' '
        co_y += 1
    co_y = tem_y
    while(bg.canvas[co_x + 1][co_y] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"_"+ Style.RESET_ALL):
        bg.canvas[co_x + 1][co_y] = ' '
        co_y += 1
    co_y = tem_y
    while(bg.canvas[co_x - 2][co_y] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"_"+ Style.RESET_ALL):
        bg.canvas[co_x - 2][co_y] = ' '
        co_y += 1
    co_y = tem_y
    while(bg.canvas[co_x + 2][co_y] == Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"_"+ Style.RESET_ALL):
        bg.canvas[co_x + 2][co_y] = ' '
        co_y += 1
    co_y = tem_y

def emoveBullet(k) :
    t = 0
    for i in range(len(ecoor_x)):
        if ecoor_y[i] > k and ebulletFlag[i] :
            bg.canvas[ecoor_x[i]][ecoor_y[i]] = temp.canvas[ecoor_x[i]][ecoor_y[i]]
            bg.canvas[ecoor_x[i]][ecoor_y[i] - 1] = temp.canvas[ecoor_x[i]][ecoor_y[i] - 1]
            for j in range (1, 5) :
                temp.canvas[ecoor_x[i]][ecoor_y[i] - j] = bg.canvas[ecoor_x[i]][ecoor_y[i] - j]
            if bg.canvas[ecoor_x[i]][ecoor_y[i] - 2] == Fore.WHITE + Back.BLUE + Style.BRIGHT +")"+ Style.RESET_ALL or bg.canvas[ecoor_x[i]][ecoor_y[i] - 2] == Fore.WHITE + Back.BLUE + Style.BRIGHT +"-"+ Style.RESET_ALL or bg.canvas[ecoor_x[i]][ecoor_y[i] - 2] == Fore.WHITE + Back.BLUE + Style.BRIGHT +"^"+ Style.RESET_ALL:
                t = 1
            ecoor_y[i] -= 3
            bg.canvas[ecoor_x[i]][ecoor_y[i]] = Fore.WHITE + Back.BLACK + Style.BRIGHT +"="+ Style.RESET_ALL
            bg.canvas[ecoor_x[i]][ecoor_y[i] - 1] = Fore.WHITE + Back.BLACK + Style.BRIGHT +"<"+ Style.RESET_ALL
        else :
            ebulletFlag[i] = 0
            bg.canvas[ecoor_x[i]][ecoor_y[i]] = temp.canvas[ecoor_x[i]][ecoor_y[i]]
            bg.canvas[ecoor_x[i]][ecoor_y[i] - 1] = temp.canvas[ecoor_x[i]][ecoor_y[i] - 1]
    return t
