class Animal(object):
    def run(self):
        print('Animal is running...')


class Student(Animal):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self, a):

        print('%s: %s' % (self.name, self.score))
        print(self)

    def run(self):
        print('Student is running...')


bart = Student('Bart Simpson', 59)
bart.print_score('a')
bart.run()
print(isinstance(bart, Student))
print(isinstance(bart, Animal))

lisa = Student('Lisa Simpson', 87)
lisa.print_score('b')

print(hasattr(bart,'name'))

lisa.a='b'
print(lisa.a);
