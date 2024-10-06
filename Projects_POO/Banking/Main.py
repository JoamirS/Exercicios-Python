from Projects_POO.Banking.Client import Client
from Projects_POO.Banking.Account import BasicAccount


class Main:
    pass


# print('Teste Projeto')

client_01 = Client('Joamir', '114444-2222')
print(client_01)
print(f'{client_01.get_name_client} e {client_01.get_phone_client}')

account_01 = BasicAccount(client_01.get_name_client, 6565, 0)
print(f'{account_01.titular_account}, Número: {account_01.number_account}, '
       f'Seu saldo: {account_01.balance_account}')
