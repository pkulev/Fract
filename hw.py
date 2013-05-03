import pygame
import sys
from pygame.locals import *

def handleEvents():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else:
            print(event)

def updateState():
    pass

def drawScreen():
    pygame.display.update()

pygame.init()
display = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Yawg dog')
while True:
    handleEvents()
    updateState()
    drawScreen()

