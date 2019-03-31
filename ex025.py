#Faça um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.

#Declarando a variável que vai receber o nome da pessoa
name = str(input('Digite seu nome: ')).strip().upper()
if 'SILVA' in name:
    print('Há o nome SILVA em seu nome completo')
else:
    print('Não há o nome SILVA em seu nome completo')
