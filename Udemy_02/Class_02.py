"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex: 746.824.890-70 (746824890)
10 9 8 7 6 5 4 3 2
7 4 6 8 2 4 8 9 0
70 36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado for maior que 9:
resultado é 0
contrário disso:
resultado é o valor da conta

O primeiro dígito do CPF é
"""


def slice_CPF_and_convert_to_int(string_CPF):
    list_slice_string_int = list()

    for string_number in string_CPF:
        list_slice_string_int.append(int(string_number))

    return list_slice_string_int


def multiply_CPF_decreasing_to_ten(list_int_CPF):
    list_regressive_ten_to_two = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    result_list_multiply_to_ten = list()

    for position_list_int_CPF, position_list_regressive_ten_two in zip(list_int_CPF, list_regressive_ten_to_two):
        result_list_multiply_to_ten.append(position_list_int_CPF * position_list_regressive_ten_two)
    return result_list_multiply_to_ten


def sum_all_numbers_in_CPF(list_int_CPF):
    sum_all_numbers = 0
    for digit_in_CPF in list_int_CPF:
        sum_all_numbers += digit_in_CPF

    return sum_all_numbers


CPF = '746.824.890-70'
CPF_without_dot_and_hyphen = CPF.replace('.', '').replace('-', '')

selecting_first_nine_digits = (CPF_without_dot_and_hyphen[:9])

result_slice_list_convert_int = slice_CPF_and_convert_to_int(selecting_first_nine_digits)

result_multiply_every_number_individually = multiply_CPF_decreasing_to_ten(result_slice_list_convert_int)

result_sum_every_number_in_CPF = sum_all_numbers_in_CPF(result_multiply_every_number_individually)

multiply_for_ten_result_of_sum_every_numbers = result_sum_every_number_in_CPF * 10

result_module_multiplication_for_eleven = multiply_for_ten_result_of_sum_every_numbers % 11

if result_module_multiplication_for_eleven > 9:
    print('0')
else:
    print(result_module_multiplication_for_eleven)

print(f'O primeiro dígito é: {result_slice_list_convert_int[0]}')
