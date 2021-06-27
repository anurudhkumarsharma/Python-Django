def number(n):
    for x in range(n):
        yield x             #yield variable is a generator
for x in number(11):
    print(x)
