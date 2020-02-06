import curses
import time
import sys
import os

# import other files
from rooms import Room

class Game:

    def __init__(self):
        self.initCurses()
        self.initStats() 
        self.getyx()
        self.printStatus()
        self.topMessage("Welcome to Enzo Rogue!")

    def initCurses(self):
        stdscr = curses.initscr()
        curses.noecho()
        curses.raw()
        begin_x = 0; begin_y = 0
        height = 36; width = 116
        self.win = curses.newwin(height, width, begin_y, begin_x)
        self.win.keypad(True)
        self.win.nodelay(True)

    def initStats(self):
        self.level = 1
        self.armor = 0
        self.hp = 100
        self.midpointx = 58
        self.midpointy = 18
        self.posx = self.midpointx
        self.posy = self.midpointy
        self.chars = {
                "floor": ".",
                "vwall": "|",
                "hwall": "-",
                "hallEnter": "+",
                "player": "@"
                }
        self.currentRoom = None

    def getyx(self):
        self.height,self.width = self.win.getmaxyx()

    def printStatus(self):
        self.botMessage("Level: " + str(self.level) + "   HP: " + str(self.hp) + "   Armor: " + str(self.armor))

    def topMessage(self, msg):
        self.win.addstr(0, 0, msg)
        self.win.refresh()

    def botMessage(self, msg):
        self.win.addstr(self.height-1, 0, msg)
        self.win.refresh()

    def recvChar(self):
        # left 260 ---  right 261 --- up 259 --- down 258
        self.c = self.win.getch()
        if self.c == 3:
            self.exit()
        # left 260
        self.win.addstr(1,0, str(self.posx))
        self.win.addstr(2,0, str(self.currentRoom.w/2))
        if(self.posx < (self.currentRoom.w/2+self.midpointx) and self.posy < (self.currentRoom.h/2+self.midpointy)):
            if self.c == 260:
                self.posx-=1
            # right 261
            elif self.c == 261:
                self.posx+=1
            # up 259
            elif self.c == 259:
                self.posy-=1
            # down 258
            elif self.c == 258:
                self.posy+=1
        else:
            f = open("demofile3.txt", "a")
            f.write(str(self.c)+"      ")
            f.close()

    def display(self):
        if self.currentRoom == None:
            self.currentRoom = Room()

        self.drawWall(self.currentRoom.w, self.chars["hwall"], 1)
        self.drawWall(self.currentRoom.w, self.chars["hwall"], 0)

        for y in range(self.currentRoom.h-3):
            self.win.move(self.midpointy - int(self.currentRoom.h/2) + y + 2, self.midpointx - int(self.currentRoom.w/2))
            for x in range(self.currentRoom.w):
                if x == 0:
                    self.win.addstr(self.chars["vwall"])
                elif x == self.currentRoom.w-1:
                    self.win.addstr(self.chars["vwall"])
                else:
                    self.win.addstr(self.chars["floor"])
        # Draw Player
        self.win.move(self.posy, self.posx)
        self.win.addstr(self.chars["player"])
        self.win.move(self.posy, self.posx)

        self.win.refresh()

    def drawWall(self, width, char, lowerUpper):
        chars = ""
        for x in range(width):
            chars+=char
        if lowerUpper == 1:
            self.win.addstr(self.midpointy - int(self.currentRoom.h/2) + 1, self.midpointx - int(self.currentRoom.w/2), chars)
        if lowerUpper == 0:
            self.win.addstr(self.midpointy + int(self.currentRoom.h/2) - 1, self.midpointx - int(self.currentRoom.w/2), chars)


    def exit(self):
        curses.nocbreak()
        self.win.keypad(False)
        curses.echo()
        curses.endwin()
        print(self.currentRoom.halls)
        sys.exit()


game = Game()

def main():
    # Game loop
    while(True):
        game.display()
        game.recvChar()


if __name__ == '__main__':
    main()
