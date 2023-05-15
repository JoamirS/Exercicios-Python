"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""
import sys
input_number_user = (input('Digite um número inteiro: '))


def number_check(input_user):
    check_input = input_user.isdigit()
    return check_input


def calculation_whether_even_or_not_(input_user):
    if input_user % 2 == 0:
        result_calculation_even_or_not = True
    else:
        result_calculation_even_or_not = False

    return result_calculation_even_or_not


check_if_is_a_number_or_not = number_check(input_number_user)

if check_if_is_a_number_or_not is False:
    print('Você não digitou um número inteiro, tente novamente')
    sys.exit()
else:
    convert_string_input = int(input_number_user)
    result_even_or_not = calculation_whether_even_or_not_(convert_string_input)
    if result_even_or_not is True:
        print('O número é par')
    else:
        print('O número é impar')
