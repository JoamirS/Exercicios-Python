"""
Exercise - Join list
Create a zipper function (like clothes zipper)
Your job of this function will be join two list in that order.
Ex.:
['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']
Result
[('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
"""


def zipper(list_one, list_two):
    maximum_interval = min(len(list_one), len(list_two))
    return [i for i in range(maximum_interval)]


list_01 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_02 = ['BA', 'SP', 'MG', 'RJ']

print(zipper(list_01, list_02))

zip_two_list = zip(list_01, list_02)
print(list(zip_two_list))
