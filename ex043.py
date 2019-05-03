'''
    Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo
    com a tabela abaixo:
    - Abaixo de 18.5: Abaixo do Peso | - Entre 18.5 e 25: Peso ideal | 25 até 30: Sobrepeso | 30 até 40: Obesidade
    - Acima de 40: Obesidade Morbida
'''
#Declarando as variáveis
print('\033[31mExemplo: KG 70\033[0;0m')
weight = float(input('Digite seu peso: KG '))
print('\033[31mExemplo: M 1.85\033[0;0m')
height = float(input('Digite sua altura: M '))
imc = weight / (height ** 2)
print('O IMC desta pessoa é {:.1f}'.format(imc))
#Declarando as condições
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está na faixa de peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')

