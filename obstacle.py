from back import bg
from colorama import *
class straightObstacle:
    def __init__(self, st_x, st_y):
        self.obs_st_x = st_x
        self.obs_st_y = st_y
        for i in range(self.obs_st_x , self.obs_st_x + 5):
            bg.canvas[i][self.obs_st_y] = Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"|"+ Style.RESET_ALL
            bg.canvas[i][self.obs_st_y + 1] = Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"|"+ Style.RESET_ALL

class diagonalObstacle:
    def __init__(self, st_x, st_y):
        self.obs_st_x = st_x
        self.obs_st_y = st_y
        for i in range(5):
            bg.canvas[self.obs_st_x + i][self.obs_st_y + i] = Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"\\"+ Style.RESET_ALL
            bg.canvas[self.obs_st_x + i][self.obs_st_y + i + 1] = Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"\\"+ Style.RESET_ALL

class horizontalObstacle:
    def __init__(self, st_x, st_y):
        self.obs_st_x = st_x
        self.obs_st_y = st_y
        for i in range(15):
            bg.canvas[ self.obs_st_x][self.obs_st_y + i] = Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"_"+ Style.RESET_ALL
            bg.canvas[ self.obs_st_x + 1][self.obs_st_y + i] = Fore.LIGHTYELLOW_EX + Back.RED + Style.BRIGHT +"_"+ Style.RESET_ALL
