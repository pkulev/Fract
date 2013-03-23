import sys
import pygame

#view
pygame.init()
width = 640
height = 480
window = pygame.display.set_mode((width, height))

#executable

inp = "auto"  # manual or auto
if inp == "auto":
    rules = dict(P = "F+F+F+F")
    program = "P"
else:
    rnumb = raw_input("[how much]")
    rules = dict()
#TODO: user input
        
        
step = 30
deep = 5
alf = 0.0
d_alf = 90.0


program = GenProgram(program, rules, deep)

draw(program, width / 2, height / 2, alf,  d_alf, step)
