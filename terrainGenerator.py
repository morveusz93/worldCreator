import pygame
import random
from cloud import Cloud

# colors:
white = (255,255,255)
lightBlue = (0, 255, 255)
lightGreen = (0, 255, 0)
darkGreen = (1,138,1)
brown = (74, 35, 1)

# screen size
width = 1000
height = 600
pixelSize = width//40
cloudSize = (pixelSize * 8, pixelSize * 5)

pygame.init()
clock = pygame.time.Clock()
fps = 60
pygame.display.set_caption("Terrain Generator")
screen = pygame.display.set_mode((width, height))

speed = 15

# creating first clouds
cloudsNumber = 15
clouds = []
for i in range(cloudsNumber):
    clouds.append(Cloud(cloudSize, pixelSize, width//3, height))

# main loop
run = True
while run:
    screen.fill(lightBlue)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        for cloud in clouds:
            cloud.image.x -=speed//3



#       creating new clouds
    if len(clouds) < cloudsNumber:
        clouds.append(Cloud(cloudSize, pixelSize, width, height))
    for cloud in clouds:
        screen.blit(cloud.draw(), (cloud.image.x, cloud.image.y))
        if cloud.image.x < -180:
            clouds.remove(cloud)    
    
    for cloud in clouds:
        cloud.image.x -= speed//5

    clock.tick(fps)
    pygame.display.update()
pygame.quit()