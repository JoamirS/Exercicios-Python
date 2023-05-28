"""
ternary operator (One line condition )
<value> if <condicao> else <outro valor>
"""

print('Valor' if True else 'Outro valor')

digit = 10
new_digit = 0 if digit > 9 else digit
print(new_digit)
