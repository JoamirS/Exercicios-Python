first_variable = 'Joamir'
second_variable = 'Maria'
third_variable = 'José'

string = f'a={first_variable} b={second_variable} a={third_variable} c={first_variable}'
formato = string.format(first_variable, second_variable, third_variable)
print(formato)
