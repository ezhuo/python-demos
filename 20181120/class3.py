from class2 import Student

Student('fdsa')()

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except Exception as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
