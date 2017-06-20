#!/usr/bin/env python
"""Pillow-based fractal viewer."""

import os
import sys

from PIL import Image, ImageDraw

import common
from lsystem import VirtualMachine


def parse_args():
    parser = common.get_default_parser("Pillow fractal viewer")
    parser.add_argument("-o", "--output", default="output.png", help="output")
    parser.add_argument(
        "-v", "--view", action="store_true", help="show picture after drawing")
    return parser.parse_args()


def main(args):
    """Entry point."""

    width = 800
    height = 600

    center_x = width / 2
    center_y = height / 2

    im = Image.new("RGBA", (800, 600), (0, 0, 0, 0))
    draw = ImageDraw.Draw(im)

    vm = VirtualMachine(
        program=args.program,
        rules=common.parse_rules(args.rules),
        depth=args.depth,
        start_x=center_x,
        start_y=center_y,
        start_angle=args.start_angle,
        delta_angle=args.delta_angle,
        step=args.step)

    def cb_draw(cur_x, cur_y, new_x, new_y):
        draw.line((cur_x, cur_y, new_x, new_y), fill=(255, 255, 255, 128))

    def cb_finish():
        if args.view:
            im.show()
        else:
            im.save(args.output, "PNG")

    vm.cb_draw = cb_draw
    vm.cb_finish = cb_finish

    vm.process()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main(parse_args()))
