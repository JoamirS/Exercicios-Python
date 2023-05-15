"""
Exercicio
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:

Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Seu nome contém (ou não) espaços
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {letra}

Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios"
"""


def string_scroller(nome):
    space_counter = 0
    for check_string_space in nome:
        if check_string_space == ' ':
            space_counter += 1
    return space_counter


def space_counter(nome):
    result_counter = 0
    if ' ' in nome:
        result_counter = string_scroller(nome)
        return result_counter
    else:
        return result_counter


input_name = input('Digite seu nome: ')
input_age = input('Digite sua idade: ')

if input_age and input_name:
    print(f'Seu nome é {input_name}')
    print(f'Seu nome invertido é {input_name[::-1]}')
    print(f'Seu nome contém {space_counter(input_name)} espaços ')
    print(f'A primeira letra do seu nome é {input_name[:1].strip()}')
    print(f'A última letra do seu nome é {input_name[len(input_name) - 1:]}')
else:
    print('Desculpe, você deixou campos vazios')
