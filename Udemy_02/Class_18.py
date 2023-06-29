"""
Truthy e Falsy, immutable and mutable types
Mutable [] {} set()
Immutable () "" 0 0.0 None False range(0, 10)
"""

list_one = []
dictionary_one = {}
set_one = set()
tuple_one = ()
string_one = ''
integer = 0
float_one = 0.0
nothing = None
false = False
interval = range(0)


def falsy(value):
    return 'falsy' if not value else 'truthy'


print(f'Teste', falsy('Teste'))
print(f'{list_one}', falsy(list_one))
print(f'{dictionary_one}', falsy(dictionary_one))
print(f'{set_one}', falsy(set_one))
print(f'{tuple_one}', falsy(tuple_one))
print(f'{string_one}', falsy(string_one))
print(f'{integer}', falsy(integer))
print(f'{float_one}', falsy(float_one))
print(f'{nothing}', falsy(nothing))
print(f'{false}', falsy(false))
print(f'{interval}', falsy(interval))
