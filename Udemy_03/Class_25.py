"""
Python Special Methods, Magic Method ou Dunder Methods
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name} (x={self.x}), y=({self.y})'

    def __add__(self, other):
        new_x = self.x + other.x
        return new_x

    def __gt__(self, other):
        self_result = self.x + self.y
        result_other = other.x + other.y
        return self_result > result_other


point_01 = Point(1, 2)
point_02 = Point(300, 400)
print(point_02)
print(repr(point_01))
print(f'{point_02!r}')

point_03 = point_01 + point_02
print(point_03)

print(f'{point_01} é maior que {point_02}? ', point_01 > point_02)
