def make_grey(text):
    grey = '\033[90m'
    reset = '\033[0m'
    return grey + text + reset


def make_red(text):
    red = '\033[91m'
    reset = '\033[0m'
    return red + text + reset


def make_green(text):
    green = '\033[92m'
    reset = '\033[0m'
    return green + text + reset


def make_yellow(text):
    yellow = '\033[93m'
    reset = '\033[0m'
    return yellow + text + reset


def make_blue(text):
    blue = '\033[94m'
    reset = '\033[0m'
    return blue + text + reset


def make_magenta(text):
    magenta = '\033[95m'
    reset = '\033[0m'
    return magenta + text + reset


def make_light_blue(text):
    light_blue = '\033[96m'
    reset = '\033[0m'
    return light_blue + text + reset


def make_blink(text):
    blink = '\033[5m'
    reset = '\033[0m'
    return blink + text + reset


def reset_color(text):
    global reset
    reset = '\033[0m'
    return reset + text