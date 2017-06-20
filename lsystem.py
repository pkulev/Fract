"""Fractal L-system virtual machine.

Set 'cb_finish' and 'cb_draw' callbacks to draw result.
Set 'cb_before' and 'cb_after' callbacks to do something in loop.
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

        self.cb_before = None
        self.cb_after = None
        self.cb_finish = None
        self.cb_draw = None

        self._stack = []

    def process(self):
        """Main loop of L-System."""

        while self._depth > 0:
            if self.cb_before:
                self.cb_before()

            self._expand_step()
            self._draw()
            self._depth -= 1

            if self.cb_after:
                self.cb_after()

        if self.cb_finish:
            self.cb_finish()

    def _forward(self):
        """Move forward."""

        new_x = cos(self._alf) * self._step + self._cur_x
        new_y = sin(self._alf) * self._step + self._cur_y
        self.cb_draw(self._cur_x, self._cur_y, new_x, new_y)
        self._cur_x = new_x
        self._cur_y = new_y

    def _turn_right(self):
        """Turn right.

        alf and d_alf are ints or floats
        returns alf decreased by d_alf.
        """
        self._alf += pi / 180.0 * self._d_alf

    def _turn_left(self):
        """Turn left.

        alf and d_alf are ints or floats
        returns alf decreased by d_alf
        """
        self._alf -= pi / 180.0 * self._d_alf

    def _push(self):
        """Push position and angle to stack."""

        self._stack.append((self._cur_x, self._cur_y, self._alf))

    def _pop(self):
        """Pop to stack and update position and angle."""

        self._cur_x, self._cur_y, self._alf = self._stack.pop()

    def _draw(self):
        """Do action by command."""

        commands = {
            "F": self._forward,
            "+": self._turn_right,
            "-": self._turn_left,
            "[": self._push,
            "]": self._pop,
        }

        for command in self._program:
            if command in commands:
                commands[command]()

    def _expand_step(self):
        """Dig one step into program by rules."""

        program = ""
        for command in self._program:
            if command in self._rules:
                program += self._rules[command]
            else:
                program += command
            self._program = program
