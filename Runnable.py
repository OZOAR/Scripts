import subprocess as sp
import time


def open_exe(path):
    task = sp.Popen(path)
    print('Opened {}'.format(path))
    time.sleep(5)
    task.kill()
    print('Task killed')
    pass


def open_bat(path):
    pass

open_exe('oaip.exe')
