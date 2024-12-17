"""
Calculate bonus

Create a program that calculates and gives a bonus print about employees must be received according the rule:

The goal is a hundred sales.
In case of the sales bigger or equal the goal, the value of employee bonus is ten percent of sale value.
Otherwise, the bonus value will be 0.
"""

the_goal = 1000
list_input_sales = list()

counter_input_sales_value = 0

while counter_input_sales_value < 3:
    input_sales_value = int(input('Qual é o valor vendido pela equipe? '))
    list_input_sales.append(input_sales_value)
    counter_input_sales_value += 1

for index, value_input_sale in enumerate(list_input_sales):
    if value_input_sale >= the_goal:
        result_percentual_bonus = value_input_sale * 0.1
        print(f'A {index + 1}º equipe ganhou um bônus de {result_percentual_bonus:.2f}')
    else:
        print(f'A {index + 1}º equipe não ganhou bônus')
