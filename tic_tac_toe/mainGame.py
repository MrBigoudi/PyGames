import pygame
from pygame.locals import *
from enum import Enum
from grid import Grid

WINDOW_WIDTH  = 1024
WINDOW_HEIGHT = 1024

class GameState(Enum):
    PLAY = 0
    QUIT = 1


class MainGame:

    def __init__(self):
        self._winHeight = 0
        self._winWidth  = 0
        self._window    = 0
        self._state     = GameState.QUIT.value
        self.keys       = []

    def init(self):
        self._winHeight = WINDOW_HEIGHT
        self._winWidth  = WINDOW_WIDTH
        self._window = pygame.display.set_mode((self._winWidth, self._winHeight))
        self._state = GameState.PLAY.value
        self._grid  = Grid()
        self._currP = Grid.p1


    def changePlayer(self):
        if self._currP == Grid.p1:
            self._currP = Grid.p2
            return
        self._currP = Grid.p1


    def inputHandler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._state = GameState.QUIT.value
            if event.type == MOUSEBUTTONDOWN:
                (xMouse,yMouse) = pygame.mouse.get_pos()
                (xGrid, yGrid)  = self._grid.getPos()
                i = (int)(xMouse - xGrid) // Grid.cellWidth
                j = (int)(yMouse - yGrid) // Grid.cellHeight
                if(self._grid.getGrid()[i,j] == 0):
                    self._grid.set(i, j, self._currP)
                    self.changePlayer()

    
    def update(self):
        self.checkEndGame()
        pygame.display.flip()


    def checkEndGame(self):
        p = self._grid.checkWin()
        if(p == Grid.p1):
            print("\n\n\nP1 WON\n\n\n")
            self._state = GameState.QUIT.value
            return
        if(p == Grid.p2):
            print("\n\n\nP2 WON\n\n\n")
            self._state = GameState.QUIT.value
            return
        if (self._grid.checkFull()):
            print("\n\n\nDRAW\n\n\n")
            self._state = GameState.QUIT.value
            return


    def draw(self):
        #self._window.fill((0,0,0))
        self._grid.draw(self._window)


    def gameLoop(self):
        while(self._state != GameState.QUIT.value):
            self.inputHandler()
            self.update()
            self.draw()


    def run(self):
        self.init()
        self.gameLoop()
        self.quit()  


    def quit(self):
        pygame.quit()      