# map - to map data
from functools import partial


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


products = [
    {'Name': 'Produto 5', 'Price': 10.00},
    {'Name': 'Produto 1', 'Price': 22.32},
    {'Name': 'Produto 3', 'Price': 10.11},
    {'Name': 'Produto 2', 'Price': 105.87},
    {'Name': 'Produto 4', 'Price': 69.90}
]


def sum_percentage(value_input, percentage_input):
    return round(value_input * percentage_input, 2)


increase_ten_percent = partial(sum_percentage, percentage_input=1.1)

new_products = [
    {**product, 'Price': increase_ten_percent(product['Price'])} for product in products
]

print_iter(products)
print_iter(new_products)
