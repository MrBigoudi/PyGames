import pygame
from pygame.locals import *
from enum import Enum
import player as pl
import ball as bl
from font import Font


WINDOW_WIDTH  = 1080
WINDOW_HEIGHT = 720
FPS = 60

class GameState(Enum):
    PLAY = 0
    EXIT = 1
    START = 2


class MainGame:

    def __init__(self):
        self._winHeight = 0
        self._winWidth  = 0
        self._window    = 0
        self._state     = GameState.EXIT.value
        self._p1        = 0
        self._p2        = 0
        self._ball      = 0
        self._keys      = []
        self._clock     = 0
        self._ticks     = 0
        self._helloPong = 0
        self._scoreP1   = 0
        self._scoreP2   = 0

    def init(self):
        pygame.init()
        self._winHeight = WINDOW_HEIGHT
        self._winWidth  = WINDOW_WIDTH
        self._window    = pygame.display.set_mode((self._winWidth, self._winHeight), vsync=1)
        self._state     = GameState.PLAY.value
        self._p1        = pl.Player(pl.MARGIN, WINDOW_HEIGHT//2 - pl.HEIGHT//2)
        self._p2        = pl.Player(WINDOW_WIDTH - pl.MARGIN - pl.WIDTH, WINDOW_HEIGHT//2 - pl.HEIGHT//2)
        self._ball      = bl.Ball(WINDOW_WIDTH // 2 - bl.WIDTH //2, WINDOW_HEIGHT//2 - bl.HEIGHT // 2)
        self._clock     = pygame.time.Clock()
        self._helloPong = Font(WINDOW_WIDTH // 2, WINDOW_WIDTH // 24, 0, 0, "Hello Pong!", 25, False)
        self._scoreP1 = Font(WINDOW_WIDTH // 4, WINDOW_WIDTH // 12, 0, 0, str(self._p1.getScore()), 100, True)
        self._scoreP2 = Font(3*WINDOW_WIDTH // 4, WINDOW_WIDTH // 12, 0, 0, str(self._p2.getScore()), 100, True)

    def run(self):
        self.init()
        self.gameLoop()
        self.quit()

    def gameLoop(self):
        dt = 0
        while(self._state != GameState.EXIT.value):
            self._clock.tick(FPS)
            self.handleInputs()
            self.update(dt)
            self.draw()
            dt = self._clock.tick(FPS)/1000.0

    def handleInputs(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self._state = GameState.EXIT.value
            if event.type == KEYDOWN:
                self.pressKey(event.key)
            if event.type == KEYUP:
                self.releaseKey(event.key)

    def pressKey(self, key):
        self._keys.append(key)

    def releaseKey(self, key):
        self._keys.remove(key)

    def update(self, dt):
        # p1 movements
        if K_w in self._keys:
            self._p1.moveUp(dt, WINDOW_HEIGHT)
        if K_s in self._keys:
            self._p1.moveDown(dt, WINDOW_HEIGHT)
        # p2 movements
        if K_UP in self._keys:
            self._p2.moveUp(dt, WINDOW_HEIGHT)
        if K_DOWN in self._keys:
            self._p2.moveDown(dt, WINDOW_HEIGHT)

        self._p1.update(dt)
        self._p2.update(dt)
        self._p1.collisionBall(self._ball)
        self._p2.collisionBall(self._ball)
        goal = self._ball.update(dt, WINDOW_HEIGHT, WINDOW_WIDTH)
        self._scoreP1.update(dt)
        self._scoreP2.update(dt)
        
        if(goal == -1):
            self._p1.score()
            self._scoreP1.setText(str(self._p1.getScore()))

        if(goal == 1):
            self._p2.score()
            self._scoreP2.setText(str(self._p2.getScore()))

        if(self._p1.won() or self._p2.won()):
            self._state = GameState.EXIT.value
        
        pygame.display.flip()

    def draw(self):
        self._window.fill((40,55,52,0))
        self._p1.draw(self._window)
        self._p2.draw(self._window)
        self._ball.draw(self._window)
        self._helloPong.draw(self._window)
        self._scoreP1.draw(self._window)
        self._scoreP2.draw(self._window)

    def quit(self):
        pygame.quit()