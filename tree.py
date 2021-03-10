import pygame
import random
from worldObject import worldObject


patterns = {1: [[0,0,0,0,0,0],
                [0,0,1,1,0,0],
                [0,1,1,1,1,0],
                [0,1,1,1,1,0],
                [0,1,1,1,1,0],
                [0,0,1,1,0,0],
                [0,0,2,2,0,0],
                [0,0,2,2,0,0]],

            2: [[0,0,0,0,0,0],
                [0,1.1,1,1,0],
                [0,1,1,1,1,0],
                [1,1,1,1,1,1],
                [1,1,1,1,1,1],
                [0,1,1,1,1,0],
                [0,0,2,2,0,0],
                [0,0,2,2,0,0]],

            3: [[0,0,1,1,0,0],
                [0,1,1,1,1,0],
                [0,0,1,1,0,0],
                [0,1,1,1,1,0],
                [0,0,1,1,0,0],
                [0,1,1,1,1,0],
                [0,0,2,2,0,0],
                [0,0,2,2,0,0]],

            4: [[0,0,0,0,0,0],
                [0,0,1,1,0,0],
                [0,0,1,1,0,0],
                [0,1,1,1,1,0],
                [0,1,1,1,1,0],
                [0,0,1,1,0,0],
                [0,0,2,2,0,0],
                [0,0,2,2,0,0]],

            5: [[0,0,0,0,0,0],
                [0,0,1,1,0,0],
                [0,1,1,1,1,0],
                [0,1,1,1,1,0],
                [0,1,1,1,1,0],
                [0,1,1,1,1,0],
                [0,0,2,2,0,0],
                [0,0,2,2,0,0]]
}



class Tree(worldObject):
    def __init__(self, objectSize, pixelSize, screenWidth, screenHeight):
        super().__init__(objectSize, pixelSize, screenWidth, screenHeight)
        self.lightGreen = (0, 255, 0)
        self.darkGreen = (1,138,1)
        self.brown = (74, 35, 1)
        
        index = random.randint(1,5)
        self.pattern = patterns[index]
        self.objectSizex, self.objectSizey = objectSize
        self.image.x = random.randint(screenWidth, screenWidth *6)
        self.image.y = random.randint(screenHeight - 100 - self.objectSizey, screenHeight - self.objectSizey)
        self.color = random.choice((self.lightGreen, self.darkGreen))


    def draw(self):
        for row in range(0, len(self.pattern)):
            for pixel in range(0, len(self.pattern[row])):
                if self.pattern[row][pixel] == 1:
                    pygame.draw.rect(self.surf, self.color, (pixel*self.pixelSize, row * self.pixelSize, self.pixelSize, self.pixelSize))
                elif self.pattern[row][pixel] == 2:
                    pygame.draw.rect(self.surf, self.brown, (pixel*self.pixelSize, row * self.pixelSize, self.pixelSize, self.pixelSize))
        return self.surf