"""
Class is a TAD Abstract Type of Data
Function return a value inside class
Method isn't return a value inside class.
Class is project object, containing programing code.
Object is a class working.
Instance is the object working.
"""


class Client:
    def __init__(self, name_input_init, phone_input_init):
        self._name_client = name_input_init
        self._phone_client = phone_input_init
        # Is no recommend to create no other constructor method for the class

    @property
    def get_name_client(self):
        return self._name_client

    @property
    def get_phone_client(self):
        return self._phone_client
