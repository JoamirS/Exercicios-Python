"""
List comprehension in Python
Is a way too fast to create list using iterables
"""

import pprint

print(list(range(10)))

list_two = [number * 2 for number in range(10)]
print(list_two)

# Data mapping in list comprehension
products = [
    {'Name': 'Product_01', 'Price': 20, },
    {'Name': 'Product_02', 'Price': 10, },
    {'Name': 'Product_03', 'Price': 30, }
]

# new_products = [product for product in products]
new_products = [
    {**product, 'Price': product['Price'] * 1.05} for product in products
]

print(*new_products, sep='\n')

pprint.pprint(new_products, sort_dicts=True, width=40)
