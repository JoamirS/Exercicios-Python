#   Faça um programa que faça o computador 'Pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
#   número escolhido pelo computador.
#   O programa deverá escrever na tela se o usuário venceu ou perdeu.
#    ----- Outra maneira de declarar a variável ------|
#   ------ from randon import randit -----------------|
#   ------ computador = randit(0, 5) | Coloca-se o intervalo em que se buscar uma informação -----|
#   ------ print('Pensei no número {}'.format(computador) ------|
#   Importando a biblioteca de escolha aleatória
from random import choice
from time import sleep
#   Criando a lista de 0 a 5
lista = ['0', '1', '2', '3', '4', '5']
choose = choice(lista)
num = str(input('Digite um número de 0 a 5: '))
print('Processando sua resposta...')
sleep(3)
if choose == num:
    print('Você venceu! Acertou o número escolhido pelo programa')
else:
    print('Você errou! Não acertou o número escolhido pelo programa.')
    print('O número escolhido pelo programa foi {} e o seu foi {}'.format(choose, num))
#   Outra maneira de declarar a variável
#   from randon import randit
#   computador = randit(0, 5) | Coloca-se o intervalo em que se buscar uma informação
#   print('Pensei no número {}'.format(computador)