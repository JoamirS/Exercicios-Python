#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
n = int(input('Digite um número inteiro: '))
an = n - 1
su = n + 1
print('O sucessor de {} é {} e o seu antecessor é {}.'.format(n, su, an))
#Outra de fazer o mesmo código é o seguinte:
n = int(input('Digite um número inteiro: '))
print('Analizando o número {}, seu antecessor é: {} e o seu sucessor é: {}'.format(n, (n -1), (n + 1)))
