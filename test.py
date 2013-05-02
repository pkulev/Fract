#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description = "some description")
parser.add_argument("-v", dest = "accumulate", action = "store_const",
                    const = sum, default = max, help = "coonst heelp")

args = parser.parse_args()




from vm1 import *

import sys, pygame

#view
pygame.init()
width = 640
height = 480
window = pygame.display.set_mode((width, height))


rules = dict(X = "X+YF", Y = "FX-Y")
program = "FX"
        
step = 5
deep = 50
alf = 0.0
d_alf = 90.0


#program = GenProgram(program, rules, deep)

vm = VirtualMachine(width / 2, height /2, alf, d_alf, step)
def DrawCallback(cur_x, cur_y, new_x, new_y):
    pygame.draw.line(window, (255, 255, 255), (cur_x, cur_y), (new_x, new_y))

def EventCallback():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        else: 
            print event

vm.SetDrawCallback(DrawCallback)
vm.SetEventCallback(EventCallback)
#vm.Draw()
vm.Process(program, rules, deep)
