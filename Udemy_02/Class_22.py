"""
Try, except, else and finally
"""

# variable_a = 18
# variable_b = 0
# division_by_zero = variable_a / variable_b

try:
    variable_a = 18
    variable_b = 0
    division_by_zero = variable_a / variable_b
except ZeroDivisionError:
    print('Dividiu por 0')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
