import os
import sys

# You can basically do `import bicolor` and then `print(f"{bicolor.red("This is red!")} | This is normal!")`

def color(text, color_code):
    if sys.platform == "win32" and os.getenv("TERM") != "xterm":
        return text

    return '\x1b[%dm%s\x1b[0m' % (color_code, text)

def red(text):
    return color(text, 31)


def blink(text):
    return color(text, 5)


def green(text):
    return color(text, 32)

def blue(text):
    return color(text, 34)
