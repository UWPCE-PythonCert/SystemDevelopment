import traceback

class YourExceptionHandler(object):
    def __enter__(self):
        pass
    def __exit__(self, _type, value, _traceback):
        print("type: %s" % _type)
        print("value: %s" % value)
        print("traceback: %s" % traceback.format_tb(_traceback))
        return True

with YourExceptionHandler():
    print("do some stuff here")
    1/0

print("should still reach this point")
