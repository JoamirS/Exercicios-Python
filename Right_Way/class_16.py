# Create a program to create adjustment of the employees.
# Receive the employee salary and adjustment according to this criterion:
# salary >= 280 -> 0.20 | between 280 and 700 -> 0.15 | between 700 and 1500 -> 0.10 | salary > 1500 -> 0.05
# Display on screen: salary before, increase percent, increase value, new salary

input_salary = float(input('Qual é o seu salário a ser reajustado? '))
value_increase = float

if input_salary <= 280:
    print(f'O salario anterior era R$ {input_salary}, e teve um reajuste de 20%')
    value_increase = input_salary * 0.20
    print(f'O valor do aumento foi de R${value_increase} e o novo salário será de R${input_salary + value_increase}')

if 280 <= input_salary <= 700:
    print(f'O salário anterior era de R$ {input_salary}, e teve um reajuste de 15%')
    value_increase = input_salary * 0.15
    print(f'O valor do aumento foi de R${value_increase}, e o novo salário será de R$ {input_salary + value_increase}')

if 700 <= input_salary <= 1500:
    print(f'O salário anterior era de R${input_salary}, e teve um reajuste de 10%')
    value_increase = input_salary * 0.10
    print(f'O valor do aumento foi de R${value_increase}, e o novo salário será de R$ {input_salary + value_increase}')

if input_salary >= 1500:
    print(f'O salário anterior era de R${input_salary}, e teve um reajuste de 5%')
    value_increase = input_salary * 0.05
    print(f'O valor do aumento foi de R${value_increase}, e o novo salário será de R$ {input_salary + value_increase}')
