import random
import sys
import threading
import time

lock = threading.Lock()

def write():
    lock.acquire()
    sys.stdout.write( "%s writing.." % threading.current_thread().name)
    time.sleep(random.random())
    sys.stdout.write( "..done\n")
    lock.release()


while True:
    thread = threading.Thread(target=write)
    thread.start()
    time.sleep(.1)

