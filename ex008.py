#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
# Km HM DAM M DM CM MM
# 0  0   0  1 0  0  0
medida = float(input('Uma lista em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = 10 * medida
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm e dm {:.0f}'.format(medida, cm, mm, dm))
print('A medida em km é: {:}. Em hm é : {:}. Em dam é: {:}'.format(km, hm, dam))
