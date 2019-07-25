'''
    Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
    o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre
    eles(desconsiderando o flag).
'''
# Declarando minhas variáveis
NumberFlag = 0
CountNumber = 0
SumNumbers = 0
# Criando meu laço condiconal
while NumberFlag != 999:
    NumberEnter = int(input('Digite um número inteiro: '))
    if NumberEnter == 999:
        break
    SumNumbers += NumberEnter
    CountNumber += 1
print(f'O número de números digitados foi de {CountNumber}\n e a soma entre todos eles é de {SumNumbers}')
