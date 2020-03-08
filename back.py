from colorama import *
init()
class background:
    def __init__(self, rows, columns):
        self.canvas = [[' ' for i in range(columns)] for j in range(rows)]
        self.rows = rows
        self.columns = columns
        for j in range(0, columns - 2, 3):
            self.canvas[0][j] = Fore.WHITE + Back.BLACK + Style.BRIGHT +"_" +Style.RESET_ALL
            self.canvas[0][j + 1] = Fore.WHITE + Back.BLACK + Style.BRIGHT +"|" +Style.RESET_ALL
            self.canvas[0][j + 2] = Fore.WHITE + Back.BLACK + Style.BRIGHT +"_" +Style.RESET_ALL
        for j in range(0, columns - 2, 3):
            self.canvas[1][j] = Fore.WHITE + Back.BLACK + Style.BRIGHT +"_" +Style.RESET_ALL
            self.canvas[1][j + 1] = Fore.WHITE + Back.BLACK + Style.BRIGHT +"_" +Style.RESET_ALL
            self.canvas[1][j + 2] = Fore.WHITE + Back.BLACK + Style.BRIGHT +"|" +Style.RESET_ALL
        for j in range(columns):
            self.canvas[rows - 3][j] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"_"+ Style.RESET_ALL
        for j in range(0,columns - 2, 3):
            self.canvas[rows - 2][j] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"_"+ Style.RESET_ALL
            self.canvas[rows - 2][j + 1] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"|"+ Style.RESET_ALL
            self.canvas[rows - 2][j + 2] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"_"+ Style.RESET_ALL
        for j in range(0,columns-2,3):
            self.canvas[rows - 1][j] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"_"+ Style.RESET_ALL
            self.canvas[rows - 1][j + 1] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"_"+ Style.RESET_ALL
            self.canvas[rows - 1][j + 2] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"|"+ Style.RESET_ALL

bg = background(54, 2000)
temp = background(54, 2000)
temp1 = background(54, 2000)
