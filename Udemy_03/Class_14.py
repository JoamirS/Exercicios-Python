"""
Relationship between classes: composition.
Composition is a specialization of aggregation.
But in her, when an object 'parent' is deleted, all references of child objects also are deleted.
"""


class Client:
    def __init__(self, name):
        self.name = name
        self.address_list = []

    def insert_address(self, street, number):
        self.address_list.append(Address(street, number))

    def list_address(self):
        for address in self.address_list:
            print(address.street, address.number)


class Address:
    def __init__(self, street, number):
        self.street = street
        self.number = number


client_01 = Client('Maria')
client_01.insert_address('Gonçalves', 30)
client_01.insert_address('Avenida 5', 2)

print(client_01.address_list)
print(client_01.address_list[0].street)
print(client_01.address_list[1].street)
#
client_01.list_address()