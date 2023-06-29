"""
Pack and unpacking of dict
"""

option_a, option_b = 1, 2
option_a, option_b = option_b, option_a

# print(option_a, option_b)

person = {
    'name': 'Aline',
    'Sobrenome': 'Sousa',
}

# option_a, option_b = person.values()
# print(option_a, option_b)

person_age_and_height = {
    'Age': 16,
    'Height': 1.6,
}

complete_person = {**person}
print(complete_person)


def show_named_argument(*args, **kwargs):
    print('Não nomeados:', args)

    for key, value in kwargs.items():
        print(key, value)


show_named_argument(nome='Joana', qualquer=123)
