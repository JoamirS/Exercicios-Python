"""
Free Local + nonlocal
"""


def out_scope(x):
    variable_a = x

    def in_scope():
        return variable_a
    return in_scope


inside_1 = out_scope(10)
inside_2 = out_scope(20)

print(inside_1())
print(inside_2())
