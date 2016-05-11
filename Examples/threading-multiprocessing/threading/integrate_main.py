#!/usr/bin/env python

import argparse
import os
import sys
import threading
import queue

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from integrate.integrate import integrate, f
from decorators.decorators import timer


@timer
def threading_integrate(f, a, b, N, thread_count=2):
    """break work into two chunks"""
    N_chunk = int(float(N) / thread_count)
    dx = float(b - a) / thread_count

    results = queue.Queue()

    def worker(*args):
        results.put(integrate(*args))

    threads = []
    for i in range(thread_count):
        x0 = dx * i
        x1 = x0 + dx
        thread = threading.Thread(target=worker, args=(f, x0, x1, N_chunk))
        thread.start()
        print("Thread %s started" % thread.name)
        # thread1.join()

    return sum((results.get() for i in range(thread_count)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='integrator')
    parser.add_argument('a', nargs='?', type=float, default=0.0)
    parser.add_argument('b', nargs='?', type=float, default=10.0)
    parser.add_argument('N', nargs='?', type=int, default=10**7)
    parser.add_argument('thread_count', nargs='?', type=int, default=2)

    args = parser.parse_args()
    a = args.a
    b = args.b
    N = args.N
    thread_count = args.thread_count

    print("Numerical solution with N=%(N)d : %(x)f" %
          {'N': N, 'x': threading_integrate(f, a, b, N, thread_count=thread_count)})

