'''
    Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''

phrase = str(input('Digite uma frase: ')).upper().strip()
phraseWords = phrase.split()
togetherWordsWithoutSpace = ''.join(phraseWords)
reversePhrase = ''
for lyrics in range(len(togetherWordsWithoutSpace) - 1, -1, -1):
    reversePhrase += togetherWordsWithoutSpace[lyrics]
print(togetherWordsWithoutSpace, reversePhrase)
if togetherWordsWithoutSpace == reversePhrase:
    print('A frase digitada é um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
