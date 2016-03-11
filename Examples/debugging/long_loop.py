
def long_loop():
    for i in range(int(1e04)):
        i+1
        if i == 777:
            raise Exception("terrible bug")
    result = 1 + 1
    return result

print long_loop()

s = "next statement"        
print s
