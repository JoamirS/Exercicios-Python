"""
@property + @setter - Getter and setter on pythonic way
- Like Getter
- To avoid broke client code
- To enable setter
- To execute actions to get an attribute
"""


class Pen:
    def __init__(self, color):
        self._color_ink = color
        self._color_cap = None

    @property  # getter
    def color(self):
        print('chamando property getter')
        return self._color_ink

    @color.setter  # setter
    def color(self, value):
        print('Estou no setter', value)
        self._color_ink = value

    @property
    def color_cap(self):
        return self._color_cap

    @color_cap.setter
    def color_cap(self, value):
        self._color_cap = value


pen_01 = Pen('Blue')
pen_01.color = 'Red'
get_color = pen_01.color
print(get_color)
get_color_cap = pen_01.color_cap
print(get_color_cap)
