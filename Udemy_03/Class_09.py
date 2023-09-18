"""
@property - A getter on python mode
getter - A method o get an attribute
python mode - A way python to make things
@property is a propriety of object, she is a method that has a behavior like an attribute
In general, is usually at follow situations:
Like getter
To avoid broke the client code
To enable setter
To execute actions to get an Attribute
"""


class Pen:
    def __init__(self, color):
        self.color_pen = color

    @property
    def get_color(self):
        return self.color_pen

    @property
    def get_color_cap(self):
        return 'Blue Sky'


pen_01 = Pen('Blue')
print(pen_01.get_color)
print(pen_01.get_color)
print(pen_01.get_color)
print(pen_01.get_color)
print(pen_01.get_color)
print(pen_01.get_color_cap)
