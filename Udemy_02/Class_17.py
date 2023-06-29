"""
isinstance - know what is the type of object
"""

list_instance = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'name': 'Joamir'}
]

# for item in list_instance:
#     print(item, isinstance(item, set))


for item in list_instance:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print(item, isinstance(item.upper(), set))
