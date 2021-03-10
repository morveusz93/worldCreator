import pygame
from worldObject import worldObject
import random


patterns = {1: [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,2,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,2,2,0,0,0,0,0,0],
                [0,0,0,0,0,2,2,2,2,2,0,0,0,0,0],
                [0,0,0,0,2,2,2,2,2,2,2,0,0,0,0],
                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],

            2:  [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,2,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,2,2,0,0,0,0,0,0],
                [0,0,0,0,0,2,2,2,2,2,0,0,0,0,0],
                [0,0,0,0,1,1,1,1,1,1,1,0,0,0,0],
                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],

            3:  [[0,0,0,0,0,0,0,2,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,2,2,2,0,0,0,0,0,0],
                [0,0,0,0,0,2,2,2,2,2,0,0,0,0,0],
                [0,0,0,0,2,2,2,2,2,2,2,0,0,0,0],
                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,0,1,1,1,1,1,1,1,1,1,0,0,0],
                [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
                [0,0,1,1,1,1,1,1,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
}



class Moutain(worldObject):
    def __init__(self,objectSize, pixelSize, screenWidth, screenHeight):
        super().__init__(objectSize, pixelSize, screenWidth, screenHeight)
        self.grey = (103,103,103)
        self.white = (200,200,200)
        index = random.randint(1,3)
        self.pattern = patterns[index]
        self.image.x = random.randint(screenWidth, screenWidth *6)
        self.objectSizex, self.objectSizey = objectSize
        self.image.y = (500 - self.objectSizey)


    def draw(self):
        for row in range(0, len(self.pattern)):
            for pixel in range(0, len(self.pattern[row])):
                if self.pattern[row][pixel] == 1:
                    pygame.draw.rect(self.surf, self.grey, (pixel*self.pixelSize, row * self.pixelSize, self.pixelSize, self.pixelSize))
                elif self.pattern[row][pixel] == 2:
                    pygame.draw.rect(self.surf, self.white, (pixel*self.pixelSize, row * self.pixelSize, self.pixelSize, self.pixelSize))
        return self.surf