"""
Exercise with Abstraction, Heritage, Encapsulation and Polymorphism
Create a banking system (simple) that has clients, accounts and a bank.
The idea is client has an account (savings or current) and that withdraw or deposit in this account.
PS: Current account has an extra limit.

Account(ABC)
    CurrentAccount
    SavingsAccount

Person(ABC)
    Client
        Client -> Account

Bank
    Bank -> Client
    Bank -> Account

Tips:
Create class Client that inherits of Person class (Heritage)
    Person has name and age (with getters)
    Client has account (Aggregation of class CurrentAccount or SavingsAccount)
Create classes SavingAccount and CurrentAccount that inherits of Account
    Current Account must have an extra limit.
    Account has agency, number of account and balance.
    Accounts must be method to deposit.
    Account (super class) must have the method withdraw abstract (Abstract and
    polymorphism - the subclasses that implements withdraw method)
Create class bank to aggregate classes of clients and of accounts (Aggregation)
Bank will responsible to authenticate the client and the following way:
    Bank has accounts and clients (Aggregation)
    Check if the agency is of that bank
    Check if the client is of that bank
    Check if the account is of that bank
It is only possible withdraw if pass bank authentication (describe above)
Bank authenticate for a method.
"""


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def get_name(self):
        return self._name

    @property
    def get_age(self):
        return self._age


class Client(Person):
    ...


class Account:
    def __init__(self, agency, account_number):
        self._extra_limit = 100
        self._agency = agency
        self._account_number = account_number
        self._balance = 0

    def deposit_cash(self, value_to_deposit):
        self._balance += value_to_deposit

    def withdraw_cash(self, value_to_withdraw):
        self._balance -= value_to_withdraw


class Bank:
    ...