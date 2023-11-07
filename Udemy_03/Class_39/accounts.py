import abc


class Account(abc.ABC):
    def __init__(self, agency, account_number, balance):
        self._agency = agency
        self._account_number = account_number
        self._balance = balance

    @abc.abstractmethod
    def withdraw_cash(self, value_to_withdraw):
        self._balance -= value_to_withdraw

    def deposit_cash(self, value_to_deposit):
        self._balance += value_to_deposit

    def details(self, msg=''):
        print(f'Your balance is {self._balance:2f} {msg}')


class SavingAccount(Account):
    def withdraw_cash(self, value_to_withdraw):
        balance_after_withdraw = self._balance - value_to_withdraw

        if balance_after_withdraw <= 0:
            self._balance -= value_to_withdraw
            print('Não foi possível sacar o valor desejado.')
            self.details(f'Saque negado {value_to_withdraw}')
            return self._balance



class CurrentAccount(Account):
    ...


if __name__ == '__main__':
    account_saving = SavingAccount(111, 222, 0)
    account_saving.withdraw_cash(10)
    acco