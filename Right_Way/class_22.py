"""
Make a program for an ATM.
The program will ask the user to withdraw value and then display how much money bill for each value will be
provided. The money bill available is 1, 5, 10, 50 and 100. The minimum value is 10 and the maximum 600.
The program must not worry about the amount of money bill in the ATM.
"""
import sys

input_user_withdrawal = int(input('Qual é o valor a ser sacado? '))

if input_user_withdrawal < 10:
    print('Você digitou um valor abaixo de 10 reais.')
    sys.exit()

if input_user_withdrawal > 600:
    print('Você excedeu o valor máximo de 600 reais.')
    sys.exit()

divisor_tuple = (100, 50, 10, 5, 1)
list_counter_money_bill = [0, 0, 0, 0, 0, 0]

position_in_tuple_in_divisor_tuple = 0

if input_user_withdrawal >= divisor_tuple[position_in_tuple_in_divisor_tuple]:
    list_counter_money_bill[position_in_tuple_in_divisor_tuple] = (input_user_withdrawal //
                                                                   divisor_tuple[position_in_tuple_in_divisor_tuple])
    print(f'Serão utilizadas {list_counter_money_bill[position_in_tuple_in_divisor_tuple]} '
          f'notas de R$ {divisor_tuple[position_in_tuple_in_divisor_tuple]}')

    input_user_withdrawal -= divisor_tuple[position_in_tuple_in_divisor_tuple] * list_counter_money_bill[position_in_tuple_in_divisor_tuple]

if input_user_withdrawal % divisor_tuple[position_in_tuple_in_divisor_tuple] >= divisor_tuple[position_in_tuple_in_divisor_tuple + 1]:
    list_counter_money_bill[position_in_tuple_in_divisor_tuple + 1] = (
        input_user_withdrawal - list_counter_money_bill[position_in_tuple_in_divisor_tuple]
        *
        list_counter_money_bill[position_in_tuple_in_divisor_tuple]) // divisor_tuple[position_in_tuple_in_divisor_tuple + 1]

    print(f'Serão utilizadas {list_counter_money_bill[position_in_tuple_in_divisor_tuple + 1]} notas de '
          f'{divisor_tuple[position_in_tuple_in_divisor_tuple + 1]}')
