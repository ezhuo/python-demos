def fun():
    print('start...')
    a = yield 5
    # a = 3
    print('a==', a)
    print('middle...')
    d = yield 12
    print('d==', d)
    print('end...')


m = fun()

m.__next__()
m.send('message111111111111111..........................................')

m.__next__()
m.send('message222222222222')
