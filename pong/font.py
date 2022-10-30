from entity import Entity
import pygame

class Font(Entity):
    def __init__(self, x, y, width, height, text, size, bold):
        Entity.__init__(self, x, y, width, height)
        self._text = text
        self._size = size
        self._bold = bold

    def draw(self, window):
        font = pygame.font.Font(pygame.font.match_font('arialblack'), self._size, bold=self._bold)
        text = font.render(self._text, True, (255, 255, 255))
        l,h  = font.size(self._text)
        window.blit(text, (self._x - l//2, self._y - h//2))

    def setText(self, newText):
        self._text = newText