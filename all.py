import sys
import pygame

#view
pygame.init()
width = 640
height = 480
window = pygame.display.set_mode((width, height))

#virtual machine implementation

from math import sin, cos, pi

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

#clean
def GoForward(cur_x, cur_y, alf, step):
    new_x = cos(alf) * step + cur_x 
    new_y = sin(alf) * step + cur_y
    pygame.draw.line(window, (255, 255, 255), (cur_x, cur_y), (new_x, new_y))
    return (new_x, new_y)
    
#clean
def TurnRight(alf, d_alf):
    """alf and d_alf are ints or floats
       returns alf decreases by d_alf"""
    alf += pi / 180.0 * d_alf
    return alf

#clean
def TurnLeft(alf, d_alf):
    """alf and d_alf are ints or floats
       returns alf decreases by d_alf"""
    alf -= pi / 180.0 * d_alf
    return alf

#clean but not tested
def Push(stack, element):
    """stack is tuple, element is tuple like (x, y, angle)
       returns stack with added element"""
    assert type(stack) == type(element) == tuple and len(element) == 3
    stack = stack + (element,)
    return stack

#clean but not tested
def Pop(stack):
    """stack is tuple with length > 0 contains tuples like (x, y, angle)
       returns tuple stack with popped element and element (x, y, angle)"""
    assert type(stack) == tuple and len(stack) > 0
    element = stack[len(stack) - 1]
    stack = stack[:-1]
    return stack, element

#eh, clean
def draw(program, cur_x, cur_y, alf, d_alf, step):
    debug  = True
    stack = (cur_x, cur_y, alf)
    if debug:
        for command in program:
            if command == "F":
                cur_x, cur_y = GoForward(cur_x, cur_y, alf, step)
            elif command == "+":
                alf = TurnRight(alf, d_alf)
            elif command == "-":
                alf = TurnLeft(alf, d_alf)
            elif command == "[":
                stack = Push(stack, (cur_x, cur_y, alf))
            elif command == "]":
                stack, (cur_x, cur_y, alf) = Pop(stack)

    while True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                sys.exit(0) 
            else: pass


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
