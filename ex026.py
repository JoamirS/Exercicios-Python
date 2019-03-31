#   Faça um programa que leia uma frase pelo teclado e mostre:
#   Quantas vezes aparece a letra 'A'| Em que posição ela aparece pela primeira vez | Em que posição ela aparece a última vez

#   Declarando a variável que receberá o valor do teclado -----------------------------|
#Utilizando a função upper para ficar tudo maiusculo e strip para remover espaços laterais ----|
frase = str(input('Digite uma frase: ')).upper().strip()
#   Usando a função count para contar quantas letras 'A' estão na presentes na frase ----------|
print('Aparece a letra A, {} vezes na frase'.format(frase.count('A')))
#   Usando a função find para achar onde aparece pela primeira vez a letra 'A' ----------------|
print('Aparece a letra A pela primeira vez na posição {}'.format(frase.find('A')+1))
#   Usando a função rfind para achar a última letra 'A' da string ------------------------------|
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))
