''' Entrar no sistema '''

enter_into_system = input('[E]ntrar [S]air: ')
typed_password = input('Senha: ')

login_password = '123456'

if enter_into_system == 'E' and typed_password == login_password:
    print('Você entrou com sucesso no sistema')
else:
    print('Você não entrou no sistema')
