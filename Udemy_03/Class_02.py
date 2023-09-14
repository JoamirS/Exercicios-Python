"""
Methods in classes instances Python
Class == Mold
Instance of class (object) - Has data
A class can generate many instances
At class, self is the instance
"""


class Car:
    def __init__(self, name):
        self.name = name

    def accelerate(self):
        print(f'{self.name} está acelerando...')


fusca = Car('Fusca')
celta = Car('Celta')
Car.accelerate(celta)

print(fusca.name)

celta.accelerate()
