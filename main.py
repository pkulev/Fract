#!/usr/bin/env python

import os
import sys

import pygame
from pygame.locals import *  # noqa

import common
from lsystem import VirtualMachine


def parse_args():
    """Parse incoming args.

    :return argparse.Namespace: args"""

    parser = common.get_default_parser("PyGame fractal viewer")
    parser.add_argument(
        "-t", "--terminate", action="store_true",
        help="terminate window exactly after rendering.")

    return parser.parse_args()


def main(args):
    """Entry point."""

    pygame.init()
    width = 800
    height = 600
    window = pygame.display.set_mode((width, height))

    center_x = width / 2
    center_y = height / 2

    vm = VirtualMachine(
        program=args.program,
        rules=common.parse_rules(args.rules),
        depth=args.depth,
        start_x=center_x,
        start_y=center_y,
        start_angle=args.start_angle,
        delta_angle=args.delta_angle,
        step=args.step
    )

    def draw(cur_x, cur_y, new_x, new_y):
        pygame.draw.line(
            window, (255, 255, 255), (cur_x, cur_y), (new_x, new_y))
        pygame.display.update()

    def finish():
        def _deinit():
            pygame.quit()
            sys.exit(0)

        if args.terminate:
            pygame.image.save(window, "output.png")
            _deinit()

        for event in pygame.event.get():
            if event.type == QUIT:  # noqa
                pygame.image.save(window, "output.png")
                _deinit()
            else:
                print(event)

    vm.cb_draw = draw
    vm.cb_finish = finish

    vm.process()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main(parse_args()))
