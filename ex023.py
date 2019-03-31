#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834 Resposta: Unidade: 4, Dezena: 3, centena: 8, milhar: 1

# #Declarando a variável a ser armazenada --------------------|
# num = str(input('Digite um número de 0 a 9999: '))
# #Declarando as varíaveis indicando os vetores ----------------|
# posicao0 = num[0]
# posicao1 = num[1]
# posicao2 = num[2]
# posicao3 = num[3]
# #Printando as unidades de medida do número -------------------|
# print('Unidade: {}'.format(posicao3))
# print('Dezena: {}'.format(posicao2))
# print('Centena: {}'.format(posicao1))
# print('Unidade: {}'.format(posicao0))
# #Obs: Essa maneira está correta, mas quando eu digito um número abaixo de 4 casas decimais, dá erro
#=========================================================================================================
#Outra maneira de fazer a mesma questão, matematicamente
#Declarando a variável a ser armazenada, quando o usuário for digitar
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número: {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
