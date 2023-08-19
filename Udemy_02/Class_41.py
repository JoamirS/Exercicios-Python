# reduce - make reduction of iterable at a value
from functools import reduce

products = [
    {'Name': 'Product 5', 'Price': 10.00},
    {'Name': 'Product 1', 'Price': 22.32},
    {'Name': 'Product 3', 'Price': 10.11},
    {'Name': 'Product 2', 'Price': 105.87},
    {'Name': 'Product 4', 'Price': 69.90}
]


def function_reduce(total, product):
    print('Acumulador', total)
    print('Produto', product)
    return total + product['Price']


total = reduce(function_reduce, products, 0)
