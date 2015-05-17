import time
import timer

x = 0

# @profile
@timer.timer
def slow():
    x = 0
    def doit1(i):
        global x
        x = x + i

    list = range(100000)
    for i in list:
        doit1(i)

# @profile
@timer.timer
def fast():
    x = 0
    def doit2(list):
        global x
        for i in list:
            x = x + i
    list = range(100000)
    doit2(list)

if __name__ == "__main__":
    s1 = slow()
    s2 = fast()
    assert(s1 == s2)
