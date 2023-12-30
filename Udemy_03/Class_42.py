# Implementing Iterator protocol in Python

class MyList:
    def __init__(self):
        self._data = {}

    @property
    def append(self):
        return self._data

    @append.setter
    def append(self, value):
        self._data[0] = value


if __name__ == '__main__':
    list_test = MyList()
