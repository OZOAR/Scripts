import os
from time import *


def get_last_line(filename, encod='ansi'):
    """Returns last line of file with <filename>
    0000609a035b03906e8b57939d46d99764af52210909d4990542dc380c4e9812"""
    with open(filename, encoding=encod) as file:
        file.seek(0, os.SEEK_END)
        position = file.tell()
        line = ''
        while position >= 0:
            file.seek(position)
            next_char = file.read(1)
            if next_char == "\n":
                return line[::-1]
            line += next_char
            position -= 1
        return line[::-1]



def time_sec_ago(delta):
    """Accepts <delta> seconds and returns
    current time - delta"""
    t = time()-delta
    return strftime('%H:%M:%S', localtime(t))

