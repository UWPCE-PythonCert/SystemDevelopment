#!/usr/bin/env python

import threading
import time

x = 1

def func():
    global x
    y = x
    time.sleep(0.01)
    y += 1
    x = y

threads = []
# with enough threads, there's sufficient overhead to cause a race
# condition
for i in range(20000):
    thread = threading.Thread(target=func)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(x)
