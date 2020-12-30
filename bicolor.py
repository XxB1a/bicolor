import sys
import os

def color(text, color_code):
    if sys.platform == "win32" and os.getenv("TERM") != "xterm":
        return text

    return '\x1b[%dm%s\x1b[0m' % (color_code, text)


def red(text): # bicolor.red()
    return color(text, 31)


def blink(text): # bicolor.blink()
    return color(text, 5)


def green(text): # bicolor.green()
    return color(text, 32)


def blue(text): # bicolor.blue()
    return color(text, 34)
