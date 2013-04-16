from math import sin, cos, pi
class VirtualMachine(object):

    def __init__(self, program, cur_x, cur_y, alf, d_alf, step):
        self.program = program
        self.cur_x = cur_x
        self.cur_y = cur_y
        self.alf = alf
        self.d_alf = d_alf
        self.step = step
        self.DrawCallback = None
        self.EventCallback = None
        self.stack = []

    def SetEventCallback(self, callback):
        self.EventCallback = callback
    
    def SetDrawCallback(self, callback):
        self.DrawCallback = callback
    
    def GoForward(self):
        new_x = cos(self.alf) * self.step + self.cur_x 
        new_y = sin(self.alf) * self.step + self.cur_y
        self.DrawCallback(self.cur_x, self.cur_y, new_x, new_y)
        self.cur_x = new_x
        self.cur_y = new_y
        
    def TurnRight(self):
        """alf and d_alf are ints or floats
        returns alf decreases by d_alf"""
        self.alf += pi / 180.0 * self.d_alf
        
    def TurnLeft(self):
        """alf and d_alf are ints or floats
        returns alf decreases by d_alf"""
        self.alf -= pi / 180.0 * self.d_alf
    
    def ProcessEvents(self):
        while True:
                self.EventCallback()

    def Draw(self):
        debug  = True
        self.stack = (self.cur_x, self.cur_y, self.alf)
        if debug:
            for command in self.program:
                if command == "F":
                    self.GoForward()
                elif command == "+":
                    self.TurnRight()
                elif command == "-":
                    selfTurnLeft()
                elif command == "[":
                    self.stack.append(self.cur_x, self.cur_y, self.alf)
                elif command == "]":
                    (self.cur_x, self.cur_y, self.alf) = self.stack.pop()
        
        self.ProcessEvents()
