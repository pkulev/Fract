import sys
import pygame
from math import sin, cos
from math import pi as PI

pygame.init()
width = 640
height = 480
cur_x = 10 #width / 2
cur_y = height -10 #/ 2
window = pygame.display.set_mode((width, height))

rules = dict(X = "-YF+XFX+FY-", Y = "+XF-YFY-FX+")
program = "X"

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
 
step = 4
deep = 7
alf = 0.0
d_alf = 360.0/4.0
stack = []
element = [cur_x, cur_y, alf]

program = GenProgram(program, rules, deep)

def GoForward(step):
    global cur_x
    global cur_y
    new_x = cos(alf) * step + cur_x 
    new_y = sin(alf) * step + cur_y
    pygame.draw.line(window, (255, 255, 255), (cur_x, cur_y), (new_x, new_y))
    cur_x = new_x
    cur_y = new_y
    
def TurnRight(d_alf):
    global alf
    alf += PI / 180.0 * d_alf

def TurnLeft(d_alf):
    global alf
    alf -= PI / 180.0 * d_alf

def Push(st, elem):
    st.append(elem)
    return st

def Pop(st):
    global cur_x
    global cur_y
    global alf
    global stack
    elem = st[len(st) - 1]
    cur_x, cur_y, alf = elem
    stack = st[:-1]
    
    
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


