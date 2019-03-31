#   Escreva um programa que leia a velocidade de um carro.
#   Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#       A multa vai custar R$ 7,00 por cada Km acimda do limite

#   Declarando a variável que vai ler a entrada do usuário
velocity = float(input('Digite a valocidade em que você estava: '))
#   Se a velocidade for maior que 80 Km, ele irá ser multado
if velocity > 80:
    print('Você foi multado por excesso de velocidade.')
#   Velocidade
    ticket = (velocity - 80) * 7
    print('Você irá pagar R${:.2f} de multa por excesso de velocidade na pista. '.format(ticket))
