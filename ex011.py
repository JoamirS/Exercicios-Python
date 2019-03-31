#Faça um programa que leia a largura e  aaltura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta, pinta uma área de 2m²
larg = float(input('Largura da Parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {} X {} e sua área é de {}m²'.format(larg, alt, area))
tinta = area/2
print('Para pintar essa essa parede, você precisará de {}l de tinta'.format(tinta))
