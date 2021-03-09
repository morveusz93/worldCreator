import pygame
import random


patterns = {1 : [[0,0,0,0,0,0,0,0],
                [0,0,0,1,1,1,0,0],
                [0,0,1,1,1,1,1,0],
                [0,0,1,1,1,0,0,0],
                [0,0,0,0,0,0,0,0]],
            2: [[0,0,0,0,0,0,0,0],
                [0,0,0,1,1,1,1,1],
                [0,0,1,1,1,1,1,0],
                [0,0,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0]],
            3: [[0,0,0,0,0,0,0,0],
                [0,0,1,1,1,1,1,1],
                [0,0,1,1,1,1,1,1],
                [0,0,1,1,1,1,0,0],
                [0,0,0,0,0,0,0,0]],
            4: [[0,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1],
                [0,0,0,1,1,1,1,1],
                [0,0,0,0,0,0,0,0]],
            5: [[0,0,1,1,1,0,0,0],
                [0,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,0],
                [0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0]]
}

class Cloud():
    def __init__(self, objectSize, pixelSize, screenWidth, screenHeight):
        self.surf = pygame.Surface(objectSize)
        self.pixelSize = pixelSize
        self.white = (255,255,255)
        index = random.randint(1,5)
        self.pattern = patterns[index]
        self.surf.fill((0,0,0))
        self.surf.set_colorkey((0,0,0))
        self.image = self.surf.get_rect()
        self.image.x = random.randint(screenWidth, screenWidth*3)
        self.image.y = random.randint(0, screenHeight//6)
        
    def draw(self):
        for row in range(0, len(self.pattern)):
            for pixel in range(0, len(self.pattern[row])):
                if self.pattern[row][pixel] == 1:
                    pygame.draw.rect(self.surf, self.white, (pixel*self.pixelSize, row * self.pixelSize, self.pixelSize, self.pixelSize))
        return self.surf