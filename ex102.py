''' Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
 retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''

from datetime import date


def vote(YearOfBirth):
    currentAge = date.today().year - YearOfBirth
    if currentAge < 16:
        print(f'Com {currentAge}, você ainda não pode votar!')
    elif 16 <= currentAge < 18 or currentAge > 65:
        print(f'Com {currentAge}, seu voto é opcinal!')
    else:
        print(f'Com {currentAge}, seu voto é obrigatório bas próximas eleições!')


YearOfBirth = int(input('Qual é o seu ano de nascimento? '))
while YearOfBirth > date.today().year or YearOfBirth < 1900:
    print('Digite um valor válido!')
    YearOfBirth = int(input('Qual é o seu ano de nascimento? '))

vote(YearOfBirth)
