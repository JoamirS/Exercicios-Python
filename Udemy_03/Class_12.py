"""
Relationship between classes: Association.
Association is a kind of relation where objects are connected within the system
This is the most common relationship between objects and subgroups like aggregation and composition.
In general, we have an association when an object has an attribute that references another object.
The association has not specify like an object control the life circle of another object
"""


class Writer:
    def __init__(self, name):
        self.name = name
        self._tool = None

    @property
    def tool(self):
        return self._tool

    @tool.setter
    def tool(self, value):
        self._tool = value


class WriteTool:
    def __init__(self, name):
        self.name = name

    def write(self):
        return f'{self.name} está escrevendo'


writer_01 = Writer('Luiz')
pen_01 = WriteTool('Caneta Bic')
writer_01.tool = pen_01
# print(writer_01.tool)
# print(writer_01.tool.write())
typewriter_01 = WriteTool('Máquina de Escrever')
writer_01.tool = typewriter_01
print(writer_01.tool.write())
