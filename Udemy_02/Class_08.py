"""
Métodos úteis para o dicionário
"""
import copy

person = {
    'nome': 'Joamir',
    'sobrenome': 'Moraes'
}

# return how many keys in the dictionary
print(person.__len__())

print(list(person.items()))

# add value if key not exist
person.setdefault('idade', '30')
print(person['idade'])

# Shallow copy and Deep copy

data = {
    'big_01': 1,
    'big_02': 2,
    'big_03': [0, 1, 2]
}

data_two = data.copy()

data_two['big_01'] = 1000
data_two['big_03'][1] = 9999


print(data)
print(data_two)

# applying deepcopy
data_three = copy.deepcopy(data_two)
data_three['big_01'] = 10
print(data_three)
