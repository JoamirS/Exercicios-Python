"""
Create a code than calculate and give a print of employees bonus.
The goal is 1000.
Whether employees sales is bigger or equal 2000, so the bonus is 15% over sales value.
Whether employees sales is less than 2000 and bigger than 1000, so the bonus is 10% over sales value.
Whether employees sales is less than 1000, so the employee bonus will be 0.
"""

the_goal = 1000
list_three_employees = []
counter_input_sales_value = 0

while counter_input_sales_value < 3:
    list_three_employees.append(int(input('Qual é o valor vendido do funcionário? ')))
    counter_input_sales_value += 1

for index, value_sale_employee in enumerate(list_three_employees):
    if value_sale_employee > 2000:
        print(f'O valor do bônus do funcionário é {value_sale_employee * 0.15}')
    elif value_sale_employee < 1000:
        print('O funcionário não terá bônus')
    else:
        print(f'O valor do bônus do funcionário é {value_sale_employee * 0.10}')
