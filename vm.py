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

def Pop(st):
    global cur_x
    global cur_y
    global alf
    global stack
    elem = st[len(st) - 1]
    cur_x, cur_y, alf = elem
    stack = st[:-1]
