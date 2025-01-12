"""
Make a program to calculate payroll, knowing that the discounts are from income tax, which depends on the gross
salary and that the FGTS corresponds to 11% of the gross salary, but is not discounted. The gross salary is minus
the discounts. The program should ask the user for the value of their hour, and the number of hours worked in the
month.

Income tax:
<= 900 - Free
<= 1500 - discount 5%
<= 2500 - discount 10%
> 2500 - discount 20%

Example: Hour value is 5 and hour amount is 220
Gross salary: (5 * 220) = $ 1100,00
(-) IR (%5): $ 55,00
(-) INSS (10%): $ 110,00
FGTS (11%): 121,00
All taxes: $ 165,00
Liquid salary: $ 935,00
"""

input_hour_value = float(input('Qual é o valor da sua hora? '))
input_amount_hour = float(input('Quantas horas você trabalhou? '))

gross_salary = input_hour_value * input_amount_hour
total_income_tax = float

if gross_salary <= 900:
    total_income_tax = 0
if 900 < gross_salary <= 1500:
    total_income_tax = gross_salary * 0.05
elif 1500 < gross_salary <= 2500:
    total_income_tax = gross_salary * 0.10
elif gross_salary > 2500:
    total_income_tax = gross_salary * 0.20

INSS_contribution_total = gross_salary * 0.10

FGTS_contribution_total = gross_salary * 0.11

all_discount = INSS_contribution_total + total_income_tax

liquid_salary = gross_salary - all_discount

print(f'Salário bruto: {gross_salary}')
print(f'IR: {total_income_tax}')
print(f'INSS: {INSS_contribution_total}')
print(f'FGTS: {FGTS_contribution_total}')
print(f'Todos os descontos: {all_discount}')
print(f'Salário líquido: {liquid_salary}')
