'''
    Crie um programa que leia duas notas de um aluno e calcule sua média,
    mostrando uma mensagem no final,
    de acordo com a média atingida:
    - Média abaixo de 5.0: Reprovado
    - Média entre 5.0 e 6.9: Recuperação
    - Média 7.0 ou superior: Aprovado
'''
#Declarando as variáveis
name = str(input('Digite seu primeiro nome: '))
num = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
avg = (num + num2) / 2
#Condições
if avg < 5.0:
    print('Você está reprovado, estude mais no próximo semestre.')
elif 6.9 >= avg >= 5.0:
    print('Você está de recuperação. Se prepare para a prova.')
elif avg >= 7.0:
    print('Parabéns, {}\nVocê passou de ano!'.format(name))
