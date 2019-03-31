#   Crie um programa que leia um número inteiro e mostre na tela se é PAR ou ÍMPAR.

#   Declarando a variável que irá receber o número a ser recebido
number = int(input('Digite um número: '))
result = number % 2
print('O resultado foi {}'.format(result))
if result == 0:
    print('O número {} é PAR'.format(number))
else:
    print('O número {} é IMPAR'.format(number))
