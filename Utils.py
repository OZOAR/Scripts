import os
from time import *


def get_last_line(filename):
    with open(filename) as file:
        file.seek(0, os.SEEK_END)
        position = file.tell()
        line = ''
        while position >= 0:
            file.seek(position)
            next_char = file.read(1)
            if next_char == "\n":
                return reversed(line)
            line += next_char
            position -= 1
        return reversed(line)


def time_sec_ago(delta):
    t = time()-delta
    return strftime('%H:%M:%S', localtime(t))

