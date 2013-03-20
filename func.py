import sys
import pygame
from vm import *

pygame.init()
width = 640
height = 480
cur_x = width / 2
cur_y = height / 2
window = pygame.display.set_mode((width, height))

rules = dict(F = "FF+[+F-F-F]-[-F+F+F]")
program = "F"

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
 
step = 3
deep = 5
alf = 0.0
d_alf = 460
stack = []
element = [cur_x, cur_y, alf]

program = GenProgram(program, rules, deep)

    
    
debug  = True

if debug:
    for command in program:
        if command == "F":
            GoForward(step)
        elif command == "+":
            TurnRight(d_alf)
        elif command == "-":
            TurnLeft(d_alf)
        elif command == "[":
            stack = Push(stack, (cur_x, cur_y, alf))
        elif command == "]":
            Pop(stack)

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            sys.exit(0) 
        else: pass


