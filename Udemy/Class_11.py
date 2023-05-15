"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação adequada.
Exemplo: Bom dia 0-11, Boa tarde 12-17 e Boa noite
"""
import sys

list_good_morning = range(0, 12)
list_good_afternoon = range(12, 18)
list_good_night = range(18, 25)


def number_check(input_user):
    check_input = input_user.isdigit()
    return check_input


input_user_clock = input('Digite o horário do dia: ')

check_if_is_a_number_or_not = number_check(input_user_clock)

if check_if_is_a_number_or_not is False:
    print('Você não digitou um número inteiro, tente novamente')
    sys.exit()

convert_int_input_user = int(input_user_clock)

if convert_int_input_user in list_good_morning:
    print('Bom dia')
elif convert_int_input_user in list_good_afternoon:
    print('Boa tarde')
elif convert_int_input_user in list_good_night:
    print('Boa noite')
else:
    print('Você não digitou um número correto')
