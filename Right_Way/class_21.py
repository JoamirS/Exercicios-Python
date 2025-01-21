"""
João Papo-de-Fiscador, a good man, bought a microcomputer to monitor the daily output of his work. Every time he brings
in a weight of fish greater than that established by the fishing regulations of the state of São Paulo (50 kilos), he
must pay a fine of R$4.00 per kilo in excess. João needs you to write a program that reads the weight variable
(weight of fish) and calculates the excess. Record in the excess variable the number of kilos over the limit and
in the fine variable the amount of the fine that João must pay. Print the program data with the appropriate messages.
"""

weight_established = 50
tax_to_pay_to_kilo_in_excess = 4.00

input_user_weight_fish = int(input('Qual é o peso do peixe? '))

if input_user_weight_fish > weight_established:
    difference_result_excess = input_user_weight_fish - weight_established
    total_tax_excess_fish = difference_result_excess * 4
    print(f'O valor de quilos é {input_user_weight_fish}, e ultrapassou {difference_result_excess} quilos.\nPor isso, '
          f'terá que pagar R$ {total_tax_excess_fish} reais de taxa.')
