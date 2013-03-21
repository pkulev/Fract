import sys
import pygame
import vm

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
element = [cur_x, cur_y, alf]

vm.init((window, step, alf, d_alf, cur_x, cur_y))    
vm.mainLoop(GenProgram(program, rules, deep))
