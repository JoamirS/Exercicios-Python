"""
Filter in list comprehension
"""

list_one = [number for number in range(10) if number < 5]
# print(list_one)

list_two = []
for variable_a in range(3):
    for variable_b in range(3):
        list_two.append((variable_a, variable_b))


# The list below, has that same effect list above
list_three = [
    (variable_c, variable_d)
    for variable_c in range(3)
    for variable_d in range(3)
]

print(list_three)
