import pygame
from pygame.locals import *
from enum import Enum
from wall import Wall
from player import Player
import map
import constants

WINDOW_WIDTH = 64*constants.TILE_WIDTH
WINDOW_HEIGHT = 32*constants.TILE_HEIGHT
TICKS = 60

class GameState(Enum):
    PLAY = 1
    EXIT = 0

class MainGame:    

    def __init__(self, mapFile):
        self._map = map.Map(mapFile)

    def init(self):
        pygame.init()
        self._winWidth = WINDOW_WIDTH
        self._winHeight = WINDOW_HEIGHT
        self._wallCoords = []
        self._window = pygame.display.set_mode((self._winWidth, self._winHeight))
        self._state = GameState.PLAY.value
        self._sprites = pygame.sprite.Group()
        self._player = 0
        self._clock = pygame.time.Clock()
        self._keys = []
        self.initSprites()
        self._intersections = []

    def initSprites(self):
        for i in range(len(self._map.map)):
            for j in range(len(self._map.map[i])):
                if(self._map.map[i][j] == map.WALL):
                    w = Wall(j,i)
                    self._sprites.add(w)
                    self._wallCoords.append(w.getCoords())
                elif(self._map.map[i][j] == map.PLAYER):
                    self._player = Player(j,i)

    def updateIntersections(self):
        self._intersections = self._player.cast(self._window, self._wallCoords)

    def drawIntersections(self):
        for inter in self._intersections:
            pygame.draw.circle(self._window, (255,0,0,255), inter, 5)

    def drawGrid(self):
        for i in range(0, WINDOW_HEIGHT, constants.TILE_HEIGHT):
            pygame.draw.line(self._window, (255,0,0,255), (0,i), (WINDOW_WIDTH,i))
        for j in range(0, WINDOW_WIDTH, constants.TILE_WIDTH):
            pygame.draw.line(self._window, (255,0,0,255), (j,0), (j,WINDOW_HEIGHT))
    

    def run(self):
        self.init()
        self.gameLoop()
        self.quit()

    def gameLoop(self):
        while(self._state != GameState.EXIT.value):
            self.inputHandler()
            self.update()
            self.draw()

    def quit(self):
        pygame.quit()

    def inputHandler(self):
        for event in pygame.event.get():
            if(event.type == QUIT):
                self._state = GameState.EXIT.value
            if(event.type == KEYDOWN):
                self.pressKey(event.key)
            if(event.type == KEYUP):
                self.releaseKey(event.key)


    def pressKey(self, key):
        if not key in self._keys:
            self._keys.append(key)

    def releaseKey(self, key):
        if key in self._keys:
            self._keys.remove(key)    

    def update(self):
        self._sprites.update()
        self._player.update(self._keys, self._sprites)
        # self.updateIntersections()
        pygame.display.flip()
        self._clock.tick(TICKS)

    def drawSky(self):
        rect = pygame.Rect(0,0,constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT/2)
        pygame.draw.rect(self._window, (0,122,122), rect)

    def draw(self):
        self._window.fill((0,0,0,0))
        self.drawSky()
        self.updateIntersections()

        # self.drawGrid()
        # self._sprites.draw(self._window)
        # self._player.draw(self._window)
        # self.drawIntersections()