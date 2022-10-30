import pygame

class Entity:
    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._height = height
        self._width = width
        self._rect = pygame.rect.Rect(x, y, width, height)

    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def getHeight(self):
        return self._height
    def getWidth(self):
        return self._width
    def getRect(self):
        return self._rect

    def update(self, dt):
        self._rect = pygame.rect.Rect(self._x, self._y, self._width, self._height)

    def draw(self, window):
        pygame.draw.rect(window, (255,255,255,255), self._rect)