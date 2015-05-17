
@profile
def slow():
    s = ""
    with open('/usr/share/dict/words') as f:
        words = []
        for w in f.readlines():
            words.append(w.upper())

        return words
    
@profile
def fast():
    with open('/usr/share/dict/words') as f:
        words = [w.upper() for w in f ]
        # words = (w.upper() for w in f)
        return words

if __name__ == "__main__":
    s1 = slow()
    s2 = fast()
    assert(s1 == s2)
