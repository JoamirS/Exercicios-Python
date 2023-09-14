# Class scope and class methods

class Animal:
    def __init__(self, name):
        self.name = name

    def action(self):
        return f'{self.name} está executando uma ação.'


lion = Animal(name='Leão')
print(lion.name)
print(lion.action())