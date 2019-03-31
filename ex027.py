# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# Declarando a variável nome, e tirando todos os espaços laterais (.strip) e colocando as letras iniciais em maiúsculo (title)
name = str(input('Digite seu nome completo: ')).strip().title()
# Dividindo o nome através do seus espaços
div = name.split()
# Saudação
print('Muito prazer em te conhecer!')
#   Dizendo seu primeiro nome
print('O primeiro nome: {}'.format((div[0])))
# Comando para ler o tamanho de o tamanho de split, menos 1 para selecionar o último nome digitado ---------|
#Esse comando é para retornar o último nome deletado --------------------|
print('O último nome: {}'.format(div[len(div)-1]))
