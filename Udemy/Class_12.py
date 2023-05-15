"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva, "Seu nome é curto";
se tiver entre 5 e 6 letras, escreva "Seu nome é normal; maior que 6 escreva "Seu nome é muito grande""
"""

input_name_user = input('Digite seu nome: ')


def check_length_name(input_user_name):
    result_length_string_name = len(input_user_name)
    return result_length_string_name


value_length_input_name_user = check_length_name(input_name_user)

if value_length_input_name_user <= 4:
    print('Seu nome é muito curto.')
elif 5 == value_length_input_name_user <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande ')
