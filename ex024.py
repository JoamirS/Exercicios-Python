#Faça um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

#Declarando a varíavel que irá receber o input -------------------------------------------------|
#Definindo como string, tirando os espaços laterais e colocando tudo em maiúsculo --------------|
city = str(input('Digite o nome da sua cidade: ')).upper().strip()
#Fatiando a string para selecionar o ponto [0]
separate = city.split()
#Se o vetor na posição [0] for SANTO retornará 'True' senão 'False'
if separate[0] == 'SANTO':
    print('A cidade começa com Santo')
else: print('A cidade não começa com Santo')
