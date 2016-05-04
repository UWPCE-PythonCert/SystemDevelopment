class CoolMeta(type):
    def __new__(meta, name, bases, dct):
        print('Creating class', name)
        return super(CoolMeta, meta).__new__(meta, name, bases, dct)
    def __init__(cls, name, bases, dct):
        print('Initializing class', name)
        super(CoolMeta, cls).__init__(name, bases, dct)
    def __call__(cls, *args, **kw):
        print('calling CoolMeta to instantiate ', cls)
        return type.__call__(cls, *args, **kw)
    
class CoolClass(metaclass=CoolMeta):
    def __init__(self):
        print('And now my CoolClass object exists')
        
print('everything loaded, instantiate a coolclass object now')
foo = CoolClass()
