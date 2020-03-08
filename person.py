import signal, os
import numpy as np
import time
from back import bg
from timeit import default_timer as timer
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from check import *
from bullet import *
from enemy import *
from colorama import *

stick = [[Fore.WHITE + Back.BLUE + Style.BRIGHT +"("+ Style.RESET_ALL, Fore.WHITE + Back.BLUE + Style.BRIGHT +"o"+ Style.RESET_ALL, Fore.WHITE + Back.BLUE + Style.BRIGHT +")"+ Style.RESET_ALL ] , [Fore.WHITE + Back.BLUE + Style.BRIGHT +"-"+ Style.RESET_ALL, Fore.WHITE + Back.BLUE + Style.BRIGHT +"|"+ Style.RESET_ALL, Fore.WHITE + Back.BLUE + Style.BRIGHT +"-"+ Style.RESET_ALL], [Fore.WHITE + Back.BLUE + Style.BRIGHT +"^"+ Style.RESET_ALL, Fore.WHITE + Back.BLUE + Style.BRIGHT +" "+ Style.RESET_ALL , Fore.WHITE + Back.BLUE + Style.BRIGHT +"^"+ Style.RESET_ALL]]
shieldStick = [[Fore.WHITE + Back.RED + Style.BRIGHT +"("+ Style.RESET_ALL, Fore.WHITE + Back.RED + Style.BRIGHT +"o"+ Style.RESET_ALL, Fore.WHITE + Back.RED + Style.BRIGHT +")"+ Style.RESET_ALL ] , [Fore.WHITE + Back.RED + Style.BRIGHT +"-"+ Style.RESET_ALL, Fore.WHITE + Back.RED + Style.BRIGHT +"|"+ Style.RESET_ALL, Fore.WHITE + Back.RED + Style.BRIGHT +"-"+ Style.RESET_ALL], [Fore.WHITE + Back.RED + Style.BRIGHT +"^"+ Style.RESET_ALL, Fore.WHITE + Back.RED + Style.BRIGHT +" "+ Style.RESET_ALL , Fore.WHITE + Back.RED + Style.BRIGHT +"^"+ Style.RESET_ALL]]
deadStick = [[Fore.WHITE + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL, Fore.WHITE + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL, Fore.WHITE + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL ] , [Fore.WHITE + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL, Fore.WHITE + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL, Fore.WHITE + Back.BLACK + Style.BRIGHT +" "+ Style.RESET_ALL], [Fore.WHITE + Back.BLACK + Style.BRIGHT +"o"+ Style.RESET_ALL, Fore.WHITE + Back.BLACK + Style.BRIGHT +"--"+ Style.RESET_ALL , Fore.WHITE + Back.BLACK + Style.BRIGHT +"<"+ Style.RESET_ALL]]

def bullets(x, y):
    coor_y.append(y + 3)
    coor_x.append(x)
    src_x = x
    src_y = y + 3
    bulletFlag.append(1)
    temp.canvas[src_x][src_y] = bg.canvas[src_x][src_y]
    temp.canvas[src_x][src_y + 1] = bg.canvas[src_x][src_y + 1]
    bg.canvas[src_x][src_y] = '='
    bg.canvas[src_x][src_y + 1] = '>'

class person:

    def __init__(self, rowx):
        self._jeta = 16
        self._jetb = 90
        self._lives = 10
        self._coins = 0
        self._shield = 0
        self._shieldStart = 0.0
        self._shieldEnd = 0.0
        self._shieldGap = 0.0
        self._shieldFlag = 0
        self._speed = 0.0
        self._gravity = 0.0
        self._x = rowx
        for i in range(3):
            for j in range(3):
                bg.canvas[self._jeta + i][self._jetb + j] = stick[i][j]

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, x):
        self._speed = x

    @property
    def jeta(self):
        return self._jeta

    @jeta.setter
    def jeta(self, x):
        self._jeta += x

    @property
    def jetb(self):
        return self._jetb

    @jetb.setter
    def jetb(self, x):
        self._jetb += x

    @property
    def shieldStart(self):
        return self._shieldStart

    @shieldStart.setter
    def shieldStart(self, x):
        self._shieldStart = x

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self,x):
        self._lives += x

    @property
    def coins(self):
        return self._coins

    @coins.setter
    def coins(self, x):
        self._coins += x

    @property
    def shield(self):
        return self._shield

    @shield.setter
    def shield(self, x):
        self._shield = x

    @property
    def shieldEnd(self):
        return self._shieldEnd

    @shieldEnd.setter
    def shieldEnd(self, x):
        self._shieldEnd = x

    @property
    def shieldGap(self):
        return self._shieldGap

    @shieldGap.setter
    def shieldGap(self, x):
        self._shieldGap = x

    @property
    def shieldFlag(self):
        return self._shieldFlag

    @shieldFlag.setter
    def shieldFlag(self, x):
        self._shieldFlag = x

    @property
    def gravity(self):
        return self._gravity

    @gravity.setter
    def gravity(self, x):
        self._gravity += x

    def movePerson(self, k):
        def alarmhandler(signum, frame):
                raise AlarmException

        def userInput(timeout = 0.1):
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        char = userInput()

        if char == 'q':
            quit()

        if self._jetb <= k :
            self._coins += checkCoins(self._jeta, k + 3)
            for i in range(3):
                for j in range(3):
                    bg.canvas[self._jeta + i][self._jetb + j] = ' '

            if checkIndex(self._jeta , k + 3) == 'ok':
                self._jetb += (k + 3 - self._jetb)

            if checkObstacle(self._jeta, self._jetb) == 1 and self._shield == 0:
                self._lives += -1

            if self._shield == 1:
                for i in range(3):
                    for j in range(3):
                        bg.canvas[self._jeta + i][self._jetb + j] = shieldStick[i][j]
            else:
                for i in range(3):
                    for j in range(3):
                        bg.canvas[self._jeta + i][self._jetb + j] = stick[i][j]

        magnetRight = checkMagnetRight(self._jeta, self._jetb)
        if magnetRight != - 1:
            for i in range(3):
                for j in range(3):
                    bg.canvas[self._jeta + i][self._jetb + j] = ' '
            self._jetb += 3
            for i in range(3):
                for j in range(3):
                    bg.canvas[self._jeta + i][self._jetb + j] = stick[i][j]

        magnetLeft = checkMagnetLeft(self._jeta, self._jetb)
        if magnetLeft != - 1:
            for i in range(3):
                for j in range(3):
                    bg.canvas[self._jeta + i][self._jetb + j] = ' '
            self._jetb += -3
            for i in range(3):
                for j in range(3):
                    bg.canvas[self._jeta + i][self._jetb + j] = stick[i][j]

        if char == ' ' and (timer() - self._shieldGap > 60 or self._shieldFlag == 0):
            self._shield = 1
            self._shieldFlag = 1
            self._shieldStart = timer()

        if char == 'w' and checkIndex(self._jeta - 2, self._jetb) == 'ok' :
            self._speed = 0
            self._gravity = 0
            for i in range(len(en)):
                for j in range(len(en[i])):
                    bg.canvas[Boss.posx + i][Boss.posy + j] = ' '

            if Boss.posx - 2 > 2:
                Boss.posx += -2

            for i in range(len(en)):
                for j in range(len(en[i])):
                    bg.canvas[Boss.posx + i][Boss.posy + j] = en[i][j]

            self._coins += checkCoins(self._jeta - 2, self._jetb)

            for i in range(3):
                for j in range(3):
                    bg.canvas[self._jeta + i][self._jetb + j] = ' '

            if(self._jeta - 2 > 2):
                self._jeta += -2

            self._coins += checkCoins(self._jeta, self._jetb)

            if checkObstacle(self._jeta, self._jetb) == 1 and self._shield == 0:
                self._lives += -1

            if self._shield == 1:
                for i in range(3):
                    for j in range(3):
                        bg.canvas[self._jeta + i][self._jetb + j] = shieldStick[i][j]
            else:
                for i in range(3):
                    for j in range(3):
                        bg.canvas[self._jeta + i][self._jetb + j] = stick[i][j]


        if char == 's' and checkIndex(self._jeta + 2, self._jetb) == 'ok':
            if checkIndex(Boss.posx + 3, Boss.posy) == 'ok':
                for i in range(len(en)):
                    for j in range(len(en[i])):
                        bg.canvas[Boss.posx + i][Boss.posy + j] = ' '

                Boss.posx += 3

                for i in range(len(en)):
                    for j in range(len(en[i])):
                        bg.canvas[Boss.posx + i][Boss.posy + j] = en[i][j]

            self._coins += checkCoins(self._jeta + 2 , self._jetb)

            for i in range(3):
                for j in range(3):
                    bg.canvas[self._jeta + i][self._jetb + j] = ' '

            if(self._jeta + 2 < 31):
                self._jeta += 2

            self._coins += checkCoins(self._jeta, self._jetb)

            if checkObstacle(self._jeta,self._jetb) == 1 and self._shield == 0:
                self._lives += -1

            if self._shield == 1:
                for i in range(3):
                    for j in range(3):
                        bg.canvas[self._jeta + i][self._jetb + j] = shieldStick[i][j]
            else:
                for i in range(3):
                    for j in range(3):
                        bg.canvas[self._jeta + i][self._jetb + j] = stick[i][j]


        if char == 'a' and checkIndex(self._jeta, self._jetb - 1) == 'ok':

            self._coins += checkCoins(self._jeta, self._jetb - 1)

            for i in range(3):
                for j in range(3):
                    bg.canvas[self._jeta + i][self._jetb + j] = ' '

            self._jetb += -1;

            self._coins += checkCoins(self._jeta, self._jetb)

            if(self._jeta + int(self._gravity) < 31):
                self._jeta += int(self._gravity)
            else:
                self._jeta = 30

            if checkObstacle(self._jeta,self._jetb) == 1 and self._shield == 0:
                self._lives += -1

            if self._shield == 1:
                for i in range(3):
                    for j in range(3):
                        bg.canvas[self._jeta + i][self._jetb + j] = shieldStick[i][j]
            else:
                for i in range(3):
                    for j in range(3):
                        bg.canvas[self._jeta + i][self._jetb + j] = stick[i][j]


        if char == 'd' and checkIndex(self._jeta, self._jetb + 2) == 'ok':

            self._coins += checkCoins(self._jeta, self._jetb + 2)

            for i in range(3):
                for j in range(3):
                    bg.canvas[self._jeta + i][self._jetb + j] = ' '

            if(self._jeta + int(self._gravity) < 31):
                self._jeta += int(self._gravity)
            else:
                self._jeta = 30

            self._jetb += 2

            self._coins += checkCoins(self._jeta, self._jetb)

            if checkObstacle(self._jeta,self._jetb) == 1 and self._shield == 0:
                self._lives += -1

            if self._shield == 1:
                for i in range(3):
                    for j in range(3):
                        bg.canvas[self._jeta + i][self._jetb + j] = shieldStick[i][j]
            else:
                for i in range(3):
                    for j in range(3):
                        bg.canvas[self._jeta + i][self._jetb + j] = stick[i][j]

        elif checkIndex(self._jeta + 1, self._jetb) == 'ok':

            self._coins += checkCoins(self._jeta + 1 , self._jetb)

            for i in range(len(en)):
                for j in range(len(en[i])):
                    bg.canvas[Boss.posx + i][Boss.posy + j] = ' '

            for i in range(3):
                for j in range(3):
                    bg.canvas[self._jeta + i][self._jetb + j] = ' '

            if(Boss.posx + self._speed < 31):
                Boss.posx += int(self._speed)
            else:
                Boss.posx += (30 - Boss.posx)

            for i in range(len(en)):
                for j in range(len(en[i])):
                    bg.canvas[Boss.posx + i][Boss.posy + j] = en[i][j]

            if(self._jeta + int(self._speed) < 31):
                self._jeta += int(self._speed)
            else:
                self._jeta = 30

            if checkObstacle(self._jeta, self._jetb) == 1 and self._shield == 0:
                self._lives += -1

            if self._shield == 1:
                for i in range(3):
                    for j in range(3):
                        bg.canvas[self._jeta + i][self._jetb + j] = shieldStick[i][j]
            else:
                for i in range(3):
                    for j in range(3):
                        bg.canvas[self._jeta + i][self._jetb + j] = stick[i][j]

        if char == 'j' :
            b1 = bullets(self._jeta, self._jetb)

test = person(34)
