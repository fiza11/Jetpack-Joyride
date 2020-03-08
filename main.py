from back import *
from person import *
import random
import numpy,time
import os
from obstacle import *
from colorama import *
from coins import *
from check import *
from person import *
from bullet import *
from timeit import default_timer as timer
from magnet import *
from enemy import *
init()

srow = 34
scol = 150

k = 0
dat = []
start = background(34, 150)

with open('start.txt') as f:
    board = f.readlines()
board = [row.rstrip('\n') for row in board]

with open('gameover.txt') as f:
    data = f.readlines()
data = [row.rstrip('\n') for row in data]

for i in range(len(board)):
    for j in range(len(board[i])):
        start.canvas[5 + i][15 +  j] = board[i][j]

for i in range(srow):
    for j in range(k, scol + k):
        print(start.canvas[i][j], end = "")
    print()
print('\033[0;0H')
time.sleep(2)

speedStart = 0.0
speedEnd = 0.0
speedFlag = 0
speedGap = 0
#Fire Beams and coins generator
randomObstacle = []
for i in range(150, 2000, 60):
     randomObstacle.append(i)
obs = [0, 1, 2]
for i in range(len(randomObstacle) - 2):
    t = (random.randint(0, 10))%3
    ifCoin = random.randint(0, 3)
    randomX = random.randint(3, 30)
    randomY = random.randint(randomObstacle[i], randomObstacle[i + 1])
    if t == 0:
        obs1 = straightObstacle(randomX, randomY)
        if ifCoin != 0:
            c1 = coin(randomX, randomY, randomObstacle[i], randomObstacle[i + 1])
    if t == 1:
        obs2 = horizontalObstacle(randomX, randomY)
        if ifCoin != 0:
            c2 = coin(randomX, randomY, randomObstacle[i], randomObstacle[i + 1])
    if t == 2:
        obs3 = diagonalObstacle(randomX, randomY)
        if ifCoin != 0:
            c3 = coin(randomX, randomY, randomObstacle[i], randomObstacle[i + 1])

#Magnets generator
totalMagnets = []
randomMagnets = []
for i in range(150, 2000, 220):
     randomMagnets.append(i)
for i in range(len(randomMagnets) - 2):
    magnets = []
    randomMagnetX = random.randint(3, 28)
    randomMagnetY = random.randint(randomMagnets[i], randomMagnets[i + 1])
    magnets.append(randomMagnetX)
    magnets.append(randomMagnetY)
    mag = magnet(randomMagnetX, randomMagnetY)
    totalMagnets.append(magnets)

randomSpeedX = random.randint(3, 31)
randomSpeedY = random.randint(200, 500)
bg.canvas[randomSpeedX][randomSpeedY] = Fore.BLUE + Back.WHITE + Style.BRIGHT + "S" +Style.RESET_ALL
flg = 1
modBullet = 0
while True:
    time = timer()
    if flg == 1:
        bg.canvas[0][k] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"S"+ Style.RESET_ALL
        bg.canvas[0][k + 1] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"C"+ Style.RESET_ALL
        bg.canvas[0][k + 2] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"O"+ Style.RESET_ALL
        bg.canvas[0][k + 3] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"R"+ Style.RESET_ALL
        bg.canvas[0][k + 4] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"E"+ Style.RESET_ALL
        bg.canvas[0][k + 5] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"="+ Style.RESET_ALL
        bg.canvas[0][k + 6] = int(test.coins/100)
        bg.canvas[0][k + 7] = int((test.coins/10)%10)
        bg.canvas[0][k + 8] = int((test.coins)%10)
        bg.canvas[1][k] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"L"+ Style.RESET_ALL
        bg.canvas[1][k + 1] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"I"+ Style.RESET_ALL
        bg.canvas[1][k + 2] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"V"+ Style.RESET_ALL
        bg.canvas[1][k + 3] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"E"+ Style.RESET_ALL
        bg.canvas[1][k + 4] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"S"+ Style.RESET_ALL
        bg.canvas[1][k + 5] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"="+ Style.RESET_ALL
        bg.canvas[1][k + 6] = int(test.lives)
        bg.canvas[2][k] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"T"+ Style.RESET_ALL
        bg.canvas[2][k + 1] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"I"+ Style.RESET_ALL
        bg.canvas[2][k + 2] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"M"+ Style.RESET_ALL
        bg.canvas[2][k + 3] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"E"+ Style.RESET_ALL
        bg.canvas[2][k + 4] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"="+ Style.RESET_ALL
        bg.canvas[2][k + 5] = 3000000 - int(timer())

        if(time > 3000000):
              quit()

        for i in range(srow):
            for j in range(k, scol + k):
                print(bg.canvas[i][j], end = "")
            print()
        print('\033[0;0H')
        if(k >= 1450):
            k = 1450
            modBullet += 1
            if modBullet > 10:
                modBullet = 0

    if test.shield == 1:
        test.shieldEnd = timer()
        if test.shieldEnd - test.shieldStart >= 10:
            test.shield = 0
            test.shieldGap = timer()

    if bg.canvas[randomSpeedX][randomSpeedY - 1] == Fore.WHITE + Back.BLUE + Style.BRIGHT +")"+ Style.RESET_ALL or bg.canvas[randomSpeedX][randomSpeedY - 1] == Fore.WHITE + Back.BLUE + Style.BRIGHT +"-"+ Style.RESET_ALL or bg.canvas[randomSpeedX][randomSpeedY - 1] == Fore.WHITE + Back.BLUE + Style.BRIGHT +"^"+ Style.RESET_ALL or bg.canvas[randomSpeedX][randomSpeedY + 1] == Fore.WHITE + Back.BLUE + Style.BRIGHT +"("+ Style.RESET_ALL or bg.canvas[randomSpeedX][randomSpeedY + 1] == Fore.WHITE + Back.BLUE + Style.BRIGHT +"-"+ Style.RESET_ALL or bg.canvas[randomSpeedX][randomSpeedY + 1] == Fore.WHITE + Back.BLUE + Style.BRIGHT +"^"+ Style.RESET_ALL or bg.canvas[randomSpeedX + 1][randomSpeedY] == Fore.WHITE + Back.BLUE + Style.BRIGHT +"o"+ Style.RESET_ALL or bg.canvas[randomSpeedX + 1][randomSpeedY] == Fore.WHITE + Back.BLUE + Style.BRIGHT +"("+ Style.RESET_ALL or bg.canvas[randomSpeedX + 1][randomSpeedY] == Fore.WHITE + Back.BLUE + Style.BRIGHT +")"+ Style.RESET_ALL or bg.canvas[randomSpeedX - 1][randomSpeedY] == Fore.WHITE + Back.BLUE + Style.BRIGHT +"^"+ Style.RESET_ALL  or bg.canvas[randomSpeedX][randomSpeedY - 1] == Fore.WHITE + Back.RED + Style.BRIGHT +")"+ Style.RESET_ALL or bg.canvas[randomSpeedX][randomSpeedY - 1] == Fore.WHITE + Back.RED + Style.BRIGHT +"-"+ Style.RESET_ALL or bg.canvas[randomSpeedX][randomSpeedY - 1] == Fore.WHITE + Back.RED + Style.BRIGHT +"^"+ Style.RESET_ALL or bg.canvas[randomSpeedX][randomSpeedY + 1] == Fore.WHITE + Back.RED + Style.BRIGHT +"("+ Style.RESET_ALL or bg.canvas[randomSpeedX][randomSpeedY + 1] == Fore.WHITE + Back.RED + Style.BRIGHT +"-"+ Style.RESET_ALL or bg.canvas[randomSpeedX][randomSpeedY + 1] == Fore.WHITE + Back.RED + Style.BRIGHT +"^"+ Style.RESET_ALL or bg.canvas[randomSpeedX + 1][randomSpeedY] == Fore.WHITE + Back.RED + Style.BRIGHT +"o"+ Style.RESET_ALL or bg.canvas[randomSpeedX + 1][randomSpeedY] == Fore.WHITE + Back.RED + Style.BRIGHT +"("+ Style.RESET_ALL or bg.canvas[randomSpeedX + 1][randomSpeedY] == Fore.WHITE + Back.RED + Style.BRIGHT +")"+ Style.RESET_ALL or bg.canvas[randomSpeedX - 1][randomSpeedY] == Fore.WHITE + Back.RED + Style.BRIGHT +"^"+ Style.RESET_ALL:
        speedStart = int(timer())
        speedFlag = 1

    if int(timer()) - speedStart >= 5:
        speedFlag = 0
        speedGap = 0

    if test.shield == 0:
        for i in range(3):
            for j in range(3):
                bg.canvas[test.jeta + i][test.jetb + j] = stick[i][j]
    else:
        for i in range(3):
            for j in range(3):
                bg.canvas[test.jeta + i][test.jetb + j] = shieldStick[i][j]

    if Boss.lives <= 0:
        print(Fore.WHITE + Back.RED + Style.BRIGHT +"YOU WON!!!!" +Style.RESET_ALL)
        quit()

    a = test.speed
    a += 0.5
    test.speed = a

    test.gravity += 0.01

    if test.lives > 0:
        k += 1
        if speedFlag == 1:
            k += 3
        test.movePerson(k)
        u = moveBullet(k)
        if u != 0:
            Boss.lives += -1
        if(k >= 1450):
            if modBullet % 10 == 0:
                enemyBullet = ebullets(Boss.posx, Boss.posy)
                p = emoveBullet(k)
                if p == 1:
                    ax = test.lives
                    if ax < 0 or ax == 0:
                        print(Fore.WHITE + Back.RED + Style.BRIGHT +"GAME OVER :((" +Style.RESET_ALL)
                    else:
                        ax -= 1
    else:
        for i in range(3):
            for j in range(3):
                    bg.canvas[test.jeta + i][test.jetb + j] = ' '

        for i in range(3):
                for j in range(3):
                    bg.canvas[test.jeta + i][test.jetb + j] = deadStick[i][j]

        for i in range(len(data)):
            for j in range(len(data[0])):
                bg.canvas[20 + i][k + 30 + j] = data[i][j]

        for i in range(srow):
            for j in range(k, scol + k):
                print(bg.canvas[i][j], end = "")
            print()

        quit()
