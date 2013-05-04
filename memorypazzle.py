import random
import sys
import pygame
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

class game(object):

    def __init__(self, wWidth = 640, wHeight = 480, fullscreen = 0, depth = 32):

        pygame.init()
        self.display = pygame.display.set_mode((wWidth, wHeight), fullscreen, depth)
        pygame.display.set_caption('Memory game')
        self.fpsClock = pygame.time.Clock()
        
        self.FPS = 30
        self.revealSpeed = 8 #speed boxes' sliding reveals and covers
        self.boxSize = 40 #box's width & height in pixels
        self.gapSize = 10 #gap's size between boxes in pixels
        self.boardWidth = 10 #number of columns of icons
        self.boardHeight = 7 #number of rows of icons
        assert (self.boardWidth * self.boardHeight) % 2 == 0, 'Needs to have even number of boxes'
        self.xMargin = int((wWidth - (self.boardWidth * (self.boxSize + self.gapSize))) / 2)
        self.yMargin = int((wHeight - (self.boardHeight * (self.boxSize + self.gapSize))) / 2)
        #colors
        self.bgColor = NAVYBLUE
        self.lightBgColor = GRAY
        self.boxColor = WHITE
        self.hightLightColor = BLUE
        #shapes
        self.donut = 'donut'
        self.square = 'square'
        self.diamond = 'diamond'
        self.lines = 'lines'
        self.oval = 'oval'
        self.allShapes = (self.donut, self.square, self.diamond, self.lines, self.oval)
        self.allColors = (RED, GREEN, BLUE, YELLOW, SILVER, PURPLE, AQUA)
        
        assert len(self.allColors) * len(self.allShapes) * 2 >= self.boardWidth * self.boardHeight, \
            "Board is too big for thr number of shapes/colors defined."
        #controls
        self.mousex = 0
        self.mousey = 0
        
        self.mainBoard = self.getRandomizedBoard()
        self.revealedBoxes = self.generateRevealedBoxesData(False)
        self.mouseClicked = False
        self.firstSelection = None #stores (x,y) of the first box clicked

        self.boxx = 0
        self.boxy = 0

        self.mainBoard = None
        
        self.display.fill(self.bgColor)
        self.startGameAnimation(self.mainBoard)

    def init(self):
        pass

    def quit(self):
        pass

    def getRandomizedBoard(stub):
        return None

    def generateRevealedBoxesData(stub,stub_):
        return [[None], [None]]
    
    def startGameAnimation(self, stub):
        print "SGA STUB!"

    def getBoxAtPixel(self, stub_1, stub_2):
        return (0, 0)

    def drawHighlightBox(self, stub_1, stub_2):
        pass

    def drawBoard(self, stub_1, stub_2):
        pass

    def revealBoxesAnimation(self, stub_1, stub_2):
        pass

    def handleEvents(self):
        self.mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                self.mousex, self.mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                self.mousex, self.mousey = event.pos
                self.mouseClicked = True
            else:
                print(event)


    def updateState(self):
        self.boxx, self.boxy = self.getBoxAtPixel(self.mousex, self.mousey)
        if self.boxx != None and self.boxy != None:
            if not self.revealedBoxes[self.boxx][self.boxy]:
                self.drawHighlightBox(self.boxx, self.boxy)
            if not self.revealedBoxes[self.boxx][self.boxy] and self.mouseClicked:
                self.revealBoxesAnimation(self.mainBoard, [(self.boxx, self.boxy)])
                self.revealedBoxes[self.boxx][self.boxy] = True

                if self.firstSelection == None: #the current box was the first box clicked
                    self.firstSelection = (self.boxx, self.boxy)
                else: #the current box was the second box clicked
                    #Check if there is a match between the two icons
                    self.firstIconShape, self.firstIconColor = self.getShapeAndColor(
                        self.mainBoard, self.firstSelection[0], self.firstSelection[2])
                    self.secondIconShape, self.secondIconColor = self.getShapeAndColor(
                        self.mainBoard, self.boxx, self.boxy)
                    if self.firstIconShape != self.secondIconShape or firstIconColor != secondIconColor:
                        #icons don't match. Re-cover up both selections
                        pygame.time.wait(1000) #1 sec
                        self.coverBoxesAnimation(self.mainBoard,
                                                 [(self.firstSelection[0], self.firstSelection[1])], 
                                                 (self.boxx, self.boxy))
                        
    def drawScreen(self):
        self.display.fill(self.bgColor)
        self.drawBoard(self.mainBoard, self.revealedBoxes)

        pygame.display.update()
        self.fpsClock.tick(self.FPS)


memgame = game()

while True:
    memgame.handleEvents()
    memgame.updateState()
    memgame.drawScreen()
