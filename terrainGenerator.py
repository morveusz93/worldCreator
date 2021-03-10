import pygame
import random
from cloud import Cloud
from tree import Tree
from moutain import Moutain

lightBlue = (0, 255, 255)
grey = (35,35,35)

# screen size
width = 1000
height = 600
pixelSize = width//40
cloudSize = (pixelSize * 8, pixelSize * 5)
treeSize = (pixelSize * 6, pixelSize * 8)
moutainSize = (pixelSize * 15, pixelSize * 11)

# starting objects:
cloudsNumber = 15
clouds = []
treesNumber = 10
trees = []
moutainsNumber = 10
moutains = []

pygame.init()
clock = pygame.time.Clock()
fps = 60
pygame.display.set_caption("Terrain Generator")
screen = pygame.display.set_mode((width, height))

speed = 30

def drawStartObjects():
    # creating first world objects
    for i in range(cloudsNumber):
        clouds.append(Cloud(cloudSize, pixelSize, width//3, height))

    for i in range(treesNumber):
        trees.append(Tree(treeSize, pixelSize, width//2, height))

    for i in range(moutainsNumber):
        moutains.append(Moutain(moutainSize, pixelSize, width//2, height))

def redrawObjects():
    if len(clouds) < cloudsNumber:
        clouds.append(Cloud(cloudSize, pixelSize, width, height))

    if len(trees) < treesNumber:
        trees.append(Tree(treeSize, pixelSize, width, height))

    if len(moutains) < moutainsNumber:
        moutains.append(Moutain(moutainSize, pixelSize, width, height))

    for cloud in clouds:
        screen.blit(cloud.draw(), (cloud.image.x, cloud.image.y))
        if cloud.image.x < -cloud.objectSizex:
            clouds.remove(cloud)    

    for moutain in moutains:
        screen.blit(moutain.draw(), (moutain.image.x, moutain.image.y))
        if moutain.image.x < -moutain.objectSizex:
            moutains.remove(moutain)

    for tree in trees:
        screen.blit(tree.draw(), (tree.image.x, tree.image.y))
        if tree.image.x < -tree.objectSizex:
            trees.remove(tree)    

    for cloud in clouds:
        cloud.image.x -= speed//5

drawStartObjects()
# main loop
run = True
while run:
    screen.fill(lightBlue)
    pygame.draw.rect(screen, grey, (0, 500, width, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        for cloud in clouds:
            cloud.image.x -=speed//8
        for tree in trees:
            tree.image.x -=speed//4
        for moutain in moutains:
            moutain.image.x -=speed//8



    redrawObjects()

    clock.tick(fps)
    pygame.display.update()
pygame.quit()