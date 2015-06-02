from timer import timer

@timer
def slow():
    s = ""
    with open('/usr/share/dict/words') as f:
        for l in f:
            s += l
    return s
    
@timer
def fast():
    with open('/usr/share/dict/words') as f:
        s = "".join(f)
        return s

if __name__ == "__main__":
    s2 = fast()
    s1 = slow()
    assert(s1 == s2)
