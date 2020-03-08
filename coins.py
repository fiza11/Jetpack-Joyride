from back import bg
from random import randint
from colorama import *

class coin:
    def __init__(self, x, y, s, t):
        if(x - 5  > 3 and y - s > 20):
            self.nx = randint(3, x)
            self.ny = randint(s, y)
            for i in range(self.nx, self.nx + 5):
                for j in range(self.ny, self.ny + 20):
                    bg.canvas[i][j] = Fore.BLACK + Back.GREEN + Style.BRIGHT +"$"+ Style.RESET_ALL
        elif(x + 5 < 31 and y - s > 20):
            self.nx = randint(x, 37)
            self.ny = randint(s, y)
            for i in range(self.nx, self.nx + 5):
                for j in range(self.ny, self.ny + 20):
                    bg.canvas[i][j] = Fore.BLACK + Back.GREEN + Style.BRIGHT +"$"+ Style.RESET_ALL
        elif (x - 5 > 3 and t - y > 20):
            self.nx = randint(3, x)
            self.ny = randint(y, t)
            for i in range(self.nx, self.nx + 5):
                for j in range(self.ny, self.ny + 20):
                    bg.canvas[i][j] = Fore.BLACK + Back.GREEN + Style.BRIGHT +"$"+ Style.RESET_ALL
        elif (x + 5 < 31 and t - y > 20):
            self.nx = randint(x, 37)
            self.ny = randint(y, t)
            for i in range(self.nx, self.nx + 5):
                for j in range(self.ny, self.ny + 20):
                    bg.canvas[i][j] = Fore.BLACK + Back.GREEN + Style.BRIGHT +"$"+ Style.RESET_ALL
