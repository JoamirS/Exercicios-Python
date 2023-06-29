"""
Dictionary comprehension and Set comprehension
"""

product = {
    'Name': 'Caneta Azul',
    'Price': 2.5,
    'Category': 'Escritório'
}

dictionary_for = {
    key: value.upper()
    if isinstance(value, str) else value
    for key, value
    in product.items()
}
print(dictionary_for)

set_comprehension = {
    number ** 2 for number in range(10)
}
print(set_comprehension)
