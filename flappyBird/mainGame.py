import pygame
from pygame.locals import *
import globals
from bird import Bird
from pipes import Pipe

class MainGame:

    def __init__(self):
        return

    def init(self, win_width, win_height):
        pygame.init()
        self.window = pygame.display.set_mode((win_width, win_height))
        self.clock = pygame.time.Clock()
        self.flappy = Bird()
        self.quit_game = False
        self.loss = False
        self.score = 0
        # keyboard event list
        self.keys = []
        self.pipes = []

    def update(self):
        self.flappy.update(self.keys)
        Pipe.updateList(self.pipes)
        self.window.fill((0,0,0))
        self.draw()
        pygame.display.flip()


    def checkLoss(self):
        (collision, self.score) = self.flappy.checkColisions(self.pipes, self.score)
        if(collision):
            self.loss = True
            print("\n\n\nLOOSER\n\n\n")
            self.quit_game = True


    def draw(self):
        self.flappy.draw(self.window)
        #print(self.pipes)
        Pipe.drawList(self.pipes, self.window)
        self.afficheScore()

    def gameLoop(self):
        while (not self.quit_game):
            self.clock.tick(globals.CLOCK_TICKS)
            self.checkLoss()
            for event in pygame.event.get():
                if event.type == QUIT :
                    self.quit_game = True
                if event.type == KEYDOWN :
                    self.pressKey(event.key)
                if event.type == KEYUP :
                    self.releaseKey(event.key)

            # Mise à jour de l'écran
            self.update()

    def run(self):
        self.init(globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT)
        self.gameLoop()
        pygame.quit()

    # update the key list
    def pressKey(self, keyPressed):
        if not keyPressed in self.keys:
            self.keys.append(keyPressed)

    def releaseKey(self, keyReleased):
        if keyReleased in self.keys:
            self.keys.remove(keyReleased)

    def afficheScore(self):
        # Affiche le score
        font=pygame.font.Font(pygame.font.match_font('arialblack'), 100, bold=True)
        text = font.render(str(max(0,self.score)),True, (255,255,255))
        l,h = font.size(str(max(0,self.score)))
        self.window.blit(text, (globals.WINDOW_WIDTH //2, globals.WINDOW_HEIGHT // 12))