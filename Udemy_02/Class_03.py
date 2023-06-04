"""
Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável
Crie uma função fala se um número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""


tuple_input = (1, 1, 3, 7, 9)


def multiply_all_arguments(args):
    result_product = args[0]  # get first position of args
    for factor in args:
        result_product *= factor

    return result_product


def even_or_odd(input_number):
    if input_number % 2 == 0:
        return True


result_multiplication_all_numbers = multiply_all_arguments(tuple_input)
print(result_multiplication_all_numbers)

check_even_or_odd = even_or_odd(result_multiplication_all_numbers)
if check_even_or_odd:
    print('O número é par')
else:
    print('O número é impar')
