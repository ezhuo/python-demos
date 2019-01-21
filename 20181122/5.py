def g():
    x, y = 1, 2
    c = yield x+y
    c += 10
    print(c)
    d = yield x + y + c


f = g()
a = f.send(None)
print(a)
b = f.send(5)
print(b)