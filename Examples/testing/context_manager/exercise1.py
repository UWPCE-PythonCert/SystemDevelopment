

class YourExceptionHandler(object):
    def __enter__(self):
        pass

    def __exit__(self, ex_type, value, traceback):
        print("there was a {} error".format(ex_type))
        if ex_type is ZeroDivisionError:
            return True
        else:
            return False


with YourExceptionHandler():
    print("do some stuff here")
    1 / 0

print("should still reach this point")

with YourExceptionHandler():
    print("do more")
    fasldkj

print("you should not get here")

