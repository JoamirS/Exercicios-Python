"""
method vs @classmethod vs @staticmethod
method - self, method od instance
@classmethod - cls, class method
@staticmethod - static method (x self, x cls)
"""


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def soma(x, y):
        return x + y


connection_01 = Connection.create_with_auth('Joamir', '1234')
# connection = Connection()
# connection.set_user('Luiz')
# connection.set_password('123456')
print(connection_01.user)
print(connection_01.password)
