import pygame
import constants

WALL_COLOR = (255, 255, 255, 255)
WALL_HEIGHT = 160

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([constants.TILE_WIDTH, constants.TILE_HEIGHT])
        self.image.fill(WALL_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x*constants.TILE_WIDTH
        self.rect.y = y*constants.TILE_HEIGHT

    def getCoords(self):
        return (self.rect.x, self.rect.y)

    def getDiscreteCoords(self):
        return (self.rect.x // constants.TILE_WIDTH, self.rect.y // constants.TILE_HEIGHT)