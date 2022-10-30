from moving_object import MovingObject
from globals import (WINDOW_WIDTH, WINDOW_HEIGHT)
import pygame
from pygame.locals import *
from pipes import Pipe

class Bird(MovingObject):
    
    x = WINDOW_WIDTH / 4
    y = WINDOW_HEIGHT / 2
    vx = 0
    vy = 64
    colour = (255,255,255,255)
    height = 32
    width = 32
    pas = vy // 4

    def __init__(self):
        MovingObject.__init__(self, Bird.x, Bird.y, Bird.width, Bird.height, Bird.colour, Bird.vx, Bird.vy)
        self.pipeIds = []
        self.jump = False
        self.mvTmp = 0 

    def update(self, keyList):
        if K_SPACE in keyList and not Bird.jump:
            self.mvTmp += self.pas 
            self.moveUp(2*self.pas)
            if(self.mvTmp > self.vy):
                Bird.jump = True
                self.mvTmp = 0
        elif not K_SPACE in keyList:
            Bird.jump = False
            self.moveDown(4)
        else:
            self.moveDown(4)

        #print(self.toString())


    def checkInPipe(self, pipe, score):
        sc = score
        xBegPipe = pipe.getX()
        xEndPipe = pipe.getX() + pipe.getWidth()
        yBegPipe = pipe.getY()
        yEndPipe = pipe.getY() + pipe.getHeight()
        # avant pipe
        if (self._x + self._width) < xBegPipe:
            return (False, sc)
        
        # update score
        if (pipe.id not in self.pipeIds):
            self.pipeIds.append(pipe.id)
            # print("update score")
            sc += 1
            
        # apres pipe
        if (self._x > xEndPipe):
            return (False, sc)
        # dessus pipe
        if (self._y + self._height) < yBegPipe:
            return (False, sc)
        # dessous pipe
        if (self._y > yEndPipe):
            return (False, sc)
        # touche pipe
        return (True, sc)

    def checkColisions(self, pipeList, score):
        sc = score
        # check oob
        # print("y: ", self.getY(), ", wh: ", WINDOW_HEIGHT)
        if (self.getY() < 0):
            return (True, sc)
        if (self.getY() + self.getHeight() > WINDOW_HEIGHT):
            return (True, sc)
        for k in range(len(pipeList)):
            (collision, sc) = self.checkInPipe(pipeList[k], sc)
            if (collision):
                return (True, score + (score-sc)//2)
        return (False, score + (sc-score)//2)
            