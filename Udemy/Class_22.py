"""
Floating-point format imprecision
"""

import decimal

number_one = decimal.Decimal(0.1)
number_two = decimal.Decimal(0.7)

result_sum_one = number_one + number_two

print(result_sum_one)
print(f'{result_sum_one:.2f}')
print(round(result_sum_one, 3))
