import random
import pygame

class worldObject:
    def __init__(self, objectSize, pixelSize, screenWidth, screenHeight):
        self.surf = pygame.Surface(objectSize)
        self.pixelSize = pixelSize
        self.surf.fill((0,0,0))
        self.surf.set_colorkey((0,0,0))
        self.image = self.surf.get_rect()
