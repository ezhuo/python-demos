def g():
    print('1')
    x = yield 'hello'
    print('2', 'x=', x)
    x += 1
    x += 1
    idx = 7
    while (idx > 0):
        idx -= 1
    d = yield x
    y = 5 + (d)
    print('3', 'y=', y)
    yield y


f = g()
# print(dir(f))
print('1.__next__ =', f.send(None))
# print('2.__next__ =', f.__next__())
# print('3.__next__ =', f.__next__())

print('2.send=', f.send(5))
print('3.send=', f.send(2))
