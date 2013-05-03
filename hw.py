import pygame
import sys
from pygame.locals import *

AQUA      =  (  0, 255, 255)
BLACK     =  (  0,   0,   0)
BLUE      =  (  0,   0, 255)
FUCHSIA   =  (255,   0, 255)
GRAY      =  (128, 128, 128)
GREEN     =  (  0, 128,   0)
LIME      =  (  0, 255,   0)
MAROON    =  (128,   0,   0)
NAVYBLUE  =  (  0,   0, 128)
OLIVE     =  (128, 128,   0)
PURPLE    =  (128,   0, 128)
RED       =  (255,   0,   0)
SILVER    =  (192, 192, 192)
TEAL      =  (  0, 128, 128)
WHITE     =  (255, 255, 255)
YELLOW    =  (255, 255,   0)













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
    display.fill(WHITE)
    pygame.draw.polygon(display, GREEN, ((143, 0), (291, 106), (236, 277),
                                         (56, 277), (0, 166)))
    pygame.draw.line(display, BLUE, (60, 60), (120, 60), 4)
    pygame.draw.line(display, BLUE, (120, 60), (60, 120))
    pygame.draw.line(display, BLUE, (60, 120), (120, 120), 4)
    pygame.draw.circle(display, BLUE, (300, 50), 20, 0)
    pygame.draw.ellipse(display, RED, (300, 250, 40, 80), 1)
    pygame.draw.rect(display, RED, (200, 150, 100, 50))

    PixObj = pygame.PixelArray(display)
    PixObj[480][380] = BLACK
    PixObj[482][382] = BLACK
    PixObj[484][384] = BLACK
    PixObj[486][386] = BLACK
    PixObj[488][388] = BLACK
    del PixObj
    pygame.display.update()

pygame.init()
display = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')
while True:
    handleEvents()
    updateState()
    drawScreen()

