""" Manipulando chaves e valores em dicionários """

person = {}

key = 'name'

person[key] = 'Joamir Moraes'
person['sobrenome'] = 'Miranda'

print(person[key])

person[key] = 'Maria'

del person['sobrenome']
print(person)

if person.get('sobrenome') is None:
    print('Não existe')
else:
    print(person['sobrenome'])
