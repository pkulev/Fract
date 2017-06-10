import argparse


BACKENDS = [
    "pygame-sdl",
    "pil",
]


def parse_rules(rules):
    """Parse incoming packed rules.

    X=X+YF;Y=FX-Y turns into {"X": "X+YF", "Y": "FX-Y"}

    :param str rules: rules to parse

    :return dict: parsed rules
    """

    return dict([it.split("=") for it in rules.split(";")])


def get_default_parser(description):
    """Common parser arguments.

    :param str description: program description

    :return argparse.ArgumentParser: parser
    """

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-b", "--backend", choices=BACKENDS, default=BACKENDS[0])
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

    return parser
