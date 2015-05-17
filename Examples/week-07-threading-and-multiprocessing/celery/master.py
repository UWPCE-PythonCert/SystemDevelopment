from tasks import add

results = []
results.append(add.delay(4,4))
results.append(add.delay(1,0))
results.append(add.delay(37337,1))

for result in results:
    print result.get()
