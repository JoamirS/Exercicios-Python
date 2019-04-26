#Escolhendo uma senha segura atrvés de alguns requisitos.
#   - Letras maiúsculas de A -> Z
#   - Letras minúsculas de a -> z
#   - Números de 0 -> 9
#   - símbolos e caracteres especiais. Exemplo: ! @ & *
# Importando a biblioteca random para fazer a escolha aleatória dos caracteres
from random import choice
#incluindo a lista com todos os caracteres a serem sorteados
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'(', ')', '`', '^', '~', '!', '@', '#', '$', '%', '¨', '&', '*', '{', '}', '[', ']', '/', '?', ':', '<', '>', ';','.',',', '+','-',
         '|', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
         '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
         ]
escolhido = choice(lista)
print('Considerando uma senha de 16 caracteres, sorteie 16 vezes')
print('A letra escolhida foi: {}'.format(escolhido))

