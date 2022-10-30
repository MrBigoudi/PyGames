import pygame
from pygame.locals import *

class GameObject:
    # constructor
    def __init__(self, x, y, width, height, colour):
        # position
        self._x = x
        self._y = y
        # size
        self._width = width
        self._height = height
        # colour
        self._colour = colour
        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)

    # getters
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getWidth(self):
        return self._width
    def getHeight(self):
        return self._height
    def getColour(self):
        return self._colour
    def getRect(self):
        return self._rect

    # setters
    def _setX(self, newX):
        self._x = newX
        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)
    def _setY(self, newY):
        self._y = newY
        self._rect = pygame.Rect(self._x, self._y, self._width, self._height)

    def toString(self):
        return  "colour: " + str(self._colour) + "\nx: " + str(self._x) + "\ny: " + str(self._y) + "\nwidth: " + str(self._width) + "\nheight: " + str(self._height)


    def draw(self, surface):
        pygame.draw.rect(surface, self._colour, self._rect)