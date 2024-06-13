import sys
import termios
import tty

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def get_arrow_key():
    first_char = getch()
    if first_char == '\x1b':  # ESC
        second_char = getch()
        if second_char == '[':
            third_char = getch()
            return second_char + third_char
    return first_char