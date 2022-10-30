import pygame
from pygame.locals import *
from enum import Enum


WINDOW_WIDTH  = 1024
WINDOW_HEIGHT = 768
CLOCK_TICKS   = 60


class GameState(Enum):
    EXIT = 0
    PLAY = 1


class MainGame:
    
    def __init__(self):
        self._window    = 0
        self._state     = 0
        self._winWidth  = 0
        self._winHeight = 0
        self._clock     = 0


    def init(self):
        self._winWidth  = WINDOW_WIDTH
        self._winHeight = WINDOW_HEIGHT
        self._window    = pygame.display.set_mode((self._winWidth, self._winHeight))
        self._state     = GameState.PLAY.value
        self._clock     = pygame.time.Clock()
        self._ticks     = self._clock.tick(CLOCK_TICKS)
        self._keys      = []


    def pressKey(self, key):
        self._keys.append(key)


    def releaseKey(self, key):
        self._keys.remove(key)


    def inputHandler(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._state = GameState.EXIT.value
            if event.type == KEYDOWN:
                self.pressKey(event.key)
            if event.type == KEYUP:
                self.releaseKey(event.key)


    def gameLoop(self):
        while(self._state != GameState.EXIT.value):
            dt = self._ticks - self._clock.tick(CLOCK_TICKS)
            self.update(dt)
            self.draw()
            self._ticks = self._clock.tick(CLOCK_TICKS)


    def update(self, dt):
        self.inputHandler()
        pygame.display.flip()


    def draw(self):
        self._window.fill((0,0,0))


    def quit(self):
        pygame.quit()


    def run(self):
        self.init()
        self.gameLoop()
        self.quit()