import subprocess as sp
from os import startfile, remove
import time
import datetime
EXE = 'EthDcrMiner64.exe'
BAT = 'start.bat'
FILE = 'loggg.noappend.txt'
KILLER = 'close_ethdcrminer.bat'
task = sp.Popen(EXE)
task.kill()

while True:
    startfile(BAT)
    while True:
        time.sleep(5)
        with open(FILE) as file:
            buffer = ''.join((s for s in file))
        if buffer.find('exit'):
            startfile(KILLER)
            remove(FILE)
            print('Miner is restarting: '.format(datetime.datetime.now()))
            break
        else:
            pass

