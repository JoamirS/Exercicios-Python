# Make a program to ask two numbers and print the bigger one.
# First_number = int(input('Primeiro número: '))
# second_number = int(input('Segundo número: '))
#
# if first_number > second_number:
#     print(f'O {first_number} é maior que {second_number}')
# else:
#     print(f'O segundo número é maior')

# Make a program to ask a value and show if the value is negative or positive.
# input_negative_or_positive = int(input('Digite um número: '))
# if input_negative_or_positive >= 0:
#     print('O número é positivo')
# else:
#     print('O número é negativo')

# Make a program to check the civil state of a person. If a character is 'M' (Married), 'S' (Single), 'D' (Divorced),
# 'W' (Widower) or 'O' (Other). According to the written letter for user, your program must be to write the state of
# civil state.
# input_civil_state = input('Qual é o seu estado de relacionamento? ')
# if input_civil_state == 'M':
#    print('Seu estado civil é casado.')
# elif input_civil_state == 'S':
#    print('Seu estado civil é solteiro.')
# elif input_civil_state == 'D':
#    print('Você é divorciado')
# elif input_civil_state == 'W':
#    print('Você é viúvo')
# elif input_civil_state == 'O':
#    print('Descreva seu estado civil')


# Make a program to check if the inputted email is in e-mails spam.
# emails_spam = "fulano@gmail.com, beltrano@gmail.com, ciclano@gmail.com"
# input_email_user = input('Digite seu email: ')
# if input_email_user in emails_spam:
#     print('Seu email está em blacklist')

# Make a program to read partial two grades a student. The program must calculate the average achieved by the student.
# Approved => 7 | Reproved < 7 | Excellent approval = 10
input_grade_student_first_grade = int(input('Qual é a primeira nota? '))
input_grade_student_second_grade = int(input('Qual é a segunda nota? '))
average_two_grades_student = (input_grade_student_second_grade + input_grade_student_first_grade) / 2
if average_two_grades_student == 10:
    print('Você foi excelente e foi aprovado.')
elif 7 <= average_two_grades_student < 10:
    print('O estudante foi aprovado.')
elif average_two_grades_student < 7:
    print('Você foi reprovado')