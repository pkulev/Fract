"""Fractal L-system virtual machine.

Set 'event' and 'draw' callbacks to draw result.
"""

from math import sin, cos, pi


class VirtualMachine(object):
    """L-System virtual machine."""

    def __init__(
            self, program, rules, depth, start_x, start_y,
            start_angle, delta_angle, step
    ):
        self._program = program
        self._rules = rules
        self._depth = depth

        self._cur_x = start_x
        self._cur_y = start_y
        self._alf = start_angle
        self._d_alf = delta_angle
        self._step = step
        self._draw_cb = None
        self._event_cb = None
        self._stack = []

    @property
    def events(self):
        return self._event_cb

    @events.setter
    def events(self, callback):
        self._event_cb = callback

    @property
    def draw(self):
        return self._draw_cb

    @draw.setter
    def draw(self, callback):
        self._draw_cb = callback

    def _forward(self):
        new_x = cos(self._alf) * self._step + self._cur_x
        new_y = sin(self._alf) * self._step + self._cur_y
        self._draw_cb(self._cur_x, self._cur_y, new_x, new_y)
        self._cur_x = new_x
        self._cur_y = new_y

    def _turn_right(self):
        """Turn right.

        alf and d_alf are ints or floats
        returns alf decreases by d_alf.
        """
        self._alf += pi / 180.0 * self._d_alf

    def _turn_left(self):
        """Turn left.

        alf and d_alf are ints or floats
        returns alf decreases by d_alf
        """
        self._alf -= pi / 180.0 * self._d_alf

    def _process_events(self):
        while True:
            self._event_cb()

    def _draw(self):
        self._stack = (self._cur_x, self._cur_y, self._alf)
        for command in self._program:
            if command == "F":
                self._forward()
            elif command == "+":
                self._turn_right()
            elif command == "-":
                self._turn_left()
            elif command == "[":
                self._stack.append(self._cur_x, self._cur_y, self._alf)
            elif command == "]":
                (self._cur_x, self._cur_y, self._alf) = self._stack.pop()

    def process(self):
        def _make_new_program(self):  # TODO: function name
            cur_program = ""
            for command in self._program:
                if command in self._rules:
                    cur_program += self._rules[command]
                else:
                    cur_program += command
            self._program = cur_program

        while self._depth > 0:
            _make_new_program(self)
            self._draw()
            self._depth -= 1

        self._process_events()
