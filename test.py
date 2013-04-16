#!/usr/bin/env python

from vm1 import *

import sys, pygame

#view
pygame.init()
width = 640
height = 480
window = pygame.display.set_mode((width, height))


def GenProgram(current, rules, depth):
    if depth == 0:
        return current
    else:
        temp = ""
        for command in current:
            if command in rules:
                temp += rules[command]
            else:
                temp += command
        return GenProgram(temp, rules, depth - 1)


rules = dict(P = "F+F+F+F")
program = "P"
        
step = 30
deep = 5
alf = 0.0
d_alf = 90.0


program = GenProgram(program, rules, deep)

vm = VirtualMachine(program, width / 2, height /2, alf, d_alf, step)
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
vm.Draw()
