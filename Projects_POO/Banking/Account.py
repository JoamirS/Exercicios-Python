from abc import ABC, abstractmethod


# Single Responsibility Principle - Validação separada da classe Account
class BalanceValidator:
    @staticmethod
    def validate_balance(balance):
        if balance < 0:
            raise ValueError('Balance cannot be negative')

    @staticmethod
    def validate_amount(amount):
        if amount <= 0:
            raise ValueError('Amount must be greater than zero')


# Open/Closed Principle - Abstraí a classe Account para permitir extensão no futuro
class Account(ABC):
    def __init__(self, titular_input, number_account_input, balance_account_input):
        BalanceValidator.validate_balance(balance_account_input)
        self._titular_account = titular_input
        self._number_account = number_account_input
        self._balance_account = balance_account_input

    @property
    def titular_account(self):
        return self._titular_account

    @property
    def number_account(self):
        return self._number_account

    @property
    def balance_account(self):
        return self._balance_account

    @abstractmethod
    def withdraw(self, amount_cash):
        pass

    @abstractmethod
    def deposit(self, amount_cash):
        pass


# Liskov Substitution Principle - Subclasses devem ser intercambiáveis com a classe base
class BasicAccount(Account):
    def withdraw(self, amount):
        BalanceValidator.validate_amount(amount)
        if self.balance_account >= amount:
            self._balance_account -= amount
            print(f"Withdrawal successful: {amount}. Current balance: {self.balance_account}")
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        BalanceValidator.validate_amount(amount)
        self._balance_account += amount
        print(f"Deposit successful: {amount}. Current balance: {self.balance_account}")


# Dependency Inversion Principle - Dependa de abstrações
class AccountPrinter:
    @staticmethod
    def print_extract(account: Account):
        print(f"Client: {account.titular_account}, Current balance: {account.balance_account}")


'''
Interface Segregation Principle - Não se aplica diretamente neste exemplo, pois temos apenas 
uma interface principal (Account)
'''

if __name__ == "__main__":
    account = BasicAccount("Alice", "12345678", 1000)
    account.deposit(200)
    account.withdraw(500)
    AccountPrinter.print_extract(account)
