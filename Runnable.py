import  subprocess as sp
import time
def open_exe(path):
    pass

def open_bat(path):
    object = sp.Popen(path)
    print('{} Opened'.format(path))
    time.sleep(5)
    object.kill()
    
open_bat('cut.bat')
