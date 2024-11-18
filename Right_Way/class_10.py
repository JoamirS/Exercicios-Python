# Create a program that show the message (print) Hello World
print('Hello World')

# Create a program that ask a number then show the message: The number informed is []
input_number = int(input('Informe um número: '))
print(f'O número informado foi {input_number}')

# Create a program to ask two numbers and print the sum
first_number = int(input('Qual é o primeiro número: '))
second_number = int(input('Qual é o segundo número: '))
sum_first_number_second_number = first_number + second_number
print(f'O resultado da soma foi: {sum_first_number_second_number}')

# Create a program to ask four grades of a student, then show the average of them.
first_grade = int(input('Qual é a primeira nota? '))
second_grade = int(input('Qual é a segunda nota? '))
third_grade = int(input('Qual é a terceira nota? '))
fourth_grade = int(input('Qual é a quarta nota? '))

average_all_grades = (first_grade + second_grade + third_grade + fourth_grade) / 4
print(f'A média é {average_all_grades}')

# Create a program that convert meters for centimeters
input_meter_value = int(input('Quantos metros deseja converter para centímetros? '))
result_conversion_meter_to_centimeters = input_meter_value * 100
print(f'O valor em centímetros é {result_conversion_meter_to_centimeters}')
