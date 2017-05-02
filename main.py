#!/usr/bin/env python

import sys
import argparse

import pygame
from pygame.locals import *  # noqa

from lsystem import VirtualMachine


def parse_args():
    parser = argparse.ArgumentParser(description="some description")
    parser.add_argument("-d", "--depth", type=int, default=10, help="depth")
    parser.add_argument(
        "-p", "--program", default="FX", help="program to execute")
    parser.add_argument(
        "-r", "--rules", default="X=X+YF;Y=FX-Y", help="set of rules")
    parser.add_argument(
        "-sa", "--start-angle", type=float, default=0, help="start angle")
    parser.add_argument(
        "-da", "--delta-angle", type=float, default=90, help="delta angle")
    parser.add_argument("-s", "--step", type=int, default=10, help="step")
    parser.add_argument(
        "-t", "--terminate", action="store_true",
        help="terminate window exactly after rendering.")

    return parser.parse_args()


def parse_rules(rules):
    """Parse incoming packed rules.

    X=X+YF;Y=FX-Y turns into {"X": "X+YF", "Y": "FX-Y"}

    :param str rules: rules to parse

    :return dict: parsed rules
    """

    return dict([it.split("=") for it in rules.split(";")])


def main():
    args = parse_args()
    pygame.init()
    width = 800
    height = 600
    window = pygame.display.set_mode((width, height))

    center_x = width / 2
    center_y = height / 2

    vm = VirtualMachine(
        program=args.program,
        rules=parse_rules(args.rules),
        depth=args.depth,
        start_x=center_x,
        start_y=center_y,
        start_angle=args.start_angle,
        delta_angle=args.delta_angle,
        step=args.step
    )

    def draw_cb(cur_x, cur_y, new_x, new_y):
        pygame.draw.line(window, (255, 255, 255), (cur_x, cur_y), (new_x, new_y))
        pygame.display.update()

    def event_cb():
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

    vm.draw = draw_cb
    vm.events = event_cb

    vm.process()


if __name__ == "__main__":
    sys.exit(main())
