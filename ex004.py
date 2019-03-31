#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele
v = input('Digite algo: ')
print('Ele é alfanumérico?\n', v.isalnum(), '\nEle é do alphabeto?\n', v.isalpha(), '\nEle é númerico? \n',v.isnumeric())
print('Está em maiúsculas? ', v.isupper())
print('Está em minúsculas? ', v.islower())
print('Está capitalizada? ', v.istitle()) #Capitalizada é quando começa com a letra maiúscula e o resto continua com minúscula

