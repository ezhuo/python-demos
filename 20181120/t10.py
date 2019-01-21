def MyGenerator():
    print('start')
    value = (yield 10)
    print('MyGenerator', value)
    print('b')
    value = (yield value)
    print('value212', value)


gen = MyGenerator()
result = gen.__next__()
print(result)

result = gen.send(2)
print(result)

# result = gen.__next__()
# print(result)

result = gen.send(3)
print(result)
