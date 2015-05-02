class FibIter(object):
    def __init__(self,N):
        self.vals = [0,1]
        self.N = N
        self.i = 0

    def __iter__(self): return self

    def next(self):
        if self.i > self.N-1:
            raise StopIteration

        self.i += 1
        if self.i == 1:
            return self.vals[0]
        elif self.i == 2:
            return self.vals[1]
        else:
            new_val = sum(self.vals)
            self.vals.pop(0)
            self.vals.append(new_val)
            return new_val

for x in FibIter(20):
    print x
