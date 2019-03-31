#   Crie um programa que leia o nome completo de uma pessoa e mostre
# O nome com todas as letras maiúsculas | * O nome com todas minúsculas | * Quantas letras ao todo(sem considerar espaços).
#   * Quantas letras tem o primeiro nome
# --------------- Declarando uma string como input, e colocando a função split para remover espaços indesejados -------|
nome = str(input('Qual é o seu nome completo? ')).strip()
print('Analisando...')
# Utilizando a função upper para ficar tudo maiúsculo -------------------------------|
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
# Utilizando a função lower para ficar tudo minúsculo -------------------------------|
print('Seu nome em minúsculas é {}'.format(nome.lower()))
# Utilizando o método len para descobrir qual o tamanho da minha lista, menos a contagem de todos os espaços em branco --|
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# Há duas maneiras de mostrar quantas letras tem o primeiro nome --------------------|
# ------------ Primeira forma--------------------------------------------------------|
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
# ------------ Segunda forma --------------------------------------------------------|
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
