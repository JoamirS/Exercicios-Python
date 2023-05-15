"""
Class about lists on python
"""


list_test = [10, 20, 30, 40]

list_test.append('Joamir')
copied_list = list_test.pop()

list_test.append(1233)
print(list_test)

del list_test[-1]
print(list_test)

# list_test.clear
list_test.insert(0, 5)
# print(list_test[5])


# Extend and +
list_a = [1, 2, 3]
list_b = [4, 5, 6]

# The symbol '+' concatenates both lists
list_c = list_a + list_b
print(list_c)

# the extend works directly in the list_a
list_d = list_a.extend(list_b)
