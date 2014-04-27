#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description = "some description")
parser.add_argument("-v", dest = "accumulate", action = "store_const",
                    const = sum, default = max, help = "coonst heelp")

args = parser.parse_args()


from vm import *

import sys 
import pygame
from pygame.locals import *


#view
pygame.init()
width = 800
height = 600
window = pygame.display.set_mode((width, height))



program = "FX"
rules = dict(X = "X+YF", Y = "FX-Y")

depth = 10
center_x = width / 2
center_y = height / 2
alf = 0.0
d_alf = 90.0
step = 10

args = (program, rules, depth, center_x, center_y, alf, d_alf, step)

vm = VirtualMachine(*args)

def DrawCallback(cur_x, cur_y, new_x, new_y):
    pygame.draw.line(window, (255, 255, 255), (cur_x, cur_y), (new_x, new_y))
    pygame.display.update()

def EventCallback():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        else: 
            print event

vm.SetDrawCallback(DrawCallback)
vm.SetEventCallback(EventCallback)

vm.Process()
