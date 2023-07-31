"""
Combinations, permutations and product - Itertools
Combination = Order does matter - iterable + group length
Permutation = Order matter
Product = Order matter and repeat unique values
"""
from itertools import combinations, permutations, product

people = ['João', 'Joana', 'Luiz', 'Letícia']

shirts = ['Preta', 'Branca'], ['P', 'M']

print(list(combinations(people, 2)))
print(list(permutations(people, 2)))
print(list(product(*shirts)))
