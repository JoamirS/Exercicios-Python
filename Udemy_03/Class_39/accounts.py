import abc


class Account(abc.ABC):
    def __init__(self, agency, account_number, balance=0):
        self._agency = agency
        self._account_number = account_number
        self._balance = balance

    @property
    def get_agency(self):
        return self._agency

    @abc.abstractmethod
    def withdraw_cash(self, value_to_withdraw):
        self._balance -= value_to_withdraw

    def deposit_cash(self, value_to_deposit):
        self._balance += value_to_deposit

    def details(self, msg=''):
        print(f'Seu saldo é {self._balance:.2f} {msg}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self._agency}, {self._account_number}, {self._balance})'
        return f'{class_name}, {attrs}'


class SavingAccount(Account):
    def withdraw_cash(self, value_to_withdraw):
        balance_after_withdraw = self._balance - value_to_withdraw

        if balance_after_withdraw >= 0:
            self._balance -= value_to_withdraw
            self.details(f'(Saque {value_to_withdraw})')
            return self._balance

        print('Não foi possível sacar o valor desejado.')
        self.details(f'Saque negado {value_to_withdraw}')


class CurrentAccount(Account):
    def __init__(self, agency, account_number, balance=0, limit=0):
        super().__init__(agency, account_number, balance)
        self.limit = limit

    def withdraw_cash(self, value_to_withdraw):
        balance_after_withdraw = self._balance - value_to_withdraw

        if balance_after_withdraw >= 0:
            self._balance -= value_to_withdraw
            self.details(f'(Saque {value_to_withdraw})')
            return self._balance

        print('Não foi possível sacar o valor desejado.')
        self.details(f'Saque negado {value_to_withdraw:.2f}')
