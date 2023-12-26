# named tuples - immutable tuples with names for values

from collections import namedtuple

Card = namedtuple('Carta', ['valor', 'Tipo_carta'])
the_sword = Card('A', 'Naipe')
print(the_sword)
print(the_sword.Tipo_carta)
print(the_sword.valor)
