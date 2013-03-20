from math import sin, cos, pi


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
    alf += pi / 180.0 * d_alf

def TurnLeft(d_alf):
    global alf
    alf -= pi / 180.0 * d_alf

def Push(st, elem):
    st.append(elem)
    return st

def Pop(stack):
    elem = stack.pop()
    cur_x, cur_y, alf = elem
    return elem

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
