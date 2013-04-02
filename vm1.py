from math import sin, cos, pi

class VirtualMachine(object):
    def __init__(self, program, cur_x, cur_y, alf, d_alf, step):
        self.program = program
        self.cur_x = cur_x
        self.cur_y = cur_y
        self.alf = alf
        self.d_alf = d_alf
        self.step = step
        self.drawCallback = None

    def GoForward(cur_x, cur_y, alf, step):
        new_x = cos(alf) * step + cur_x 
        new_y = sin(alf) * step + cur_y
        drawCallback(cur_x, cur_y, new_x, new_y)
        cur_x = new_x
        cur_y = new_y
        
    def TurnRight(alf, d_alf):
        """alf and d_alf are ints or floats
        returns alf decreases by d_alf"""
        alf += pi / 180.0 * d_alf
        return alf

    def TurnLeft(alf, d_alf):
        """alf and d_alf are ints or floats
        returns alf decreases by d_alf"""
        alf -= pi / 180.0 * d_alf
        return alf

    def Push(stack, element):
        """stack is tuple, element is tuple like (x, y, angle)
        returns stack with added element"""
        assert type(stack) == type(element) == tuple and len(element) == 3
        stack = stack + (element,)
        return stack

    def Pop(stack):
        """stack is tuple with length > 0 contains tuples like (x, y, angle)
        returns tuple stack with popped element and element (x, y, angle)"""
        assert type(stack) == tuple and len(stack) > 0
        element = stack[len(stack) - 1]
        stack = stack[:-1]
        return stack, element
    def wait():
        raise NotImplementedError

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
                    
        wait()

            #while True:
            #for event in pygame.event.get(): 
            #    if event.type == pygame.QUIT: 
            #        sys.exit(0) 
            #    else: pass
        

