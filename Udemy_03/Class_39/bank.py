import accounts
import people


class Bank:
    def __init__(self, agencies_input: list[int] | None = None,
                 clients_input: list[people.Person] | None = None,
                 accounts_input: list[accounts.Account] | None = None):

        self.agencies = agencies_input or []
        self.clients = clients_input or []
        self.accounts = accounts_input or []

    def check_agency(self, account):
        if account.get_agency in self.agencies:
            return True
        return False

    def check_client(self, client):
        if client in self.clients:
            return True
        return False

    def check_account(self, account):
        if account in self.accounts:
            return True
        return False

    def authenticate(self, client, account):
        return self.check_account(account=account) and self.check_client(client) and self.check_account(account)


if __name__ == '__main__':
    client_1 = people.Client('Joamir', 30)
    account_1 = accounts.CurrentAccount(1111, 222, 0, 0)
    client_1.account = account_1

    client_2 = people.Client('Carlos', 18)
    account_2 = accounts.SavingAccount(2222, 223, 100)
    client_2.account = account_2
