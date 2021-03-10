import pygame
import random
from worldObject import worldObject

patterns = {1 : [[0,0,0,0,0,0,0,0],
                [0,0,0,1,1,1,0,0],
                [0,0,1,1,1,1,1,0],
                [0,0,1,1,1,1,1,0],
                [0,0,1,1,1,1,0,0]],
                
            2: [[0,0,0,0,0,0,0,0],
                [0,0,0,1,1,1,1,1],
                [0,0,1,1,1,1,1,0],
                [0,0,1,1,1,1,1,1],
                [0,0,0,0,0,0,0,0]],

            3: [[0,0,0,0,0,0,0,0],
                [0,0,1,1,1,1,1,1],
                [0,0,1,1,1,1,1,1],
                [0,0,1,1,1,1,0,0],
                [0,0,1,1,1,1,0,0]],

            4: [[0,1,1,1,1,1,0,0],
                [0,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,1],
                [0,0,0,1,1,1,1,1],
                [0,0,1,1,1,1,1,0]],

            5: [[0,0,1,1,1,0,0,0],
                [0,1,1,1,1,1,1,0],
                [0,1,1,1,1,1,1,0],
                [0,0,1,1,1,1,1,0],
                [0,0,1,1,1,1,1,0]]
}

class Cloud(worldObject):
    def __init__(self,objectSize, pixelSize, screenWidth, screenHeight):
        super().__init__(objectSize, pixelSize, screenWidth, screenHeight)
        self.white = (255,255,255)
        index = random.randint(1,5)
        self.pattern = patterns[index]
        self.image.x = random.randint(screenWidth, screenWidth*5)
        self.image.y = random.randint(0, screenHeight//6)
        self.objectSizex, self.objectSizey = objectSize


    def draw(self):
        for row in range(0, len(self.pattern)):
            for pixel in range(0, len(self.pattern[row])):
                if self.pattern[row][pixel] == 1:
                    pygame.draw.rect(self.surf, self.white, (pixel*self.pixelSize, row * self.pixelSize, self.pixelSize, self.pixelSize))
        return self.surf