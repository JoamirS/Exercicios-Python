"""
dir, hasattr e getattr in Python
"""

string = 'Joamir'
method = 'upper'

# hasattr show if exist the name on the object
if hasattr(string, method):
    print('Existe upper')
    print(getattr(string, method)())
else:
    print('Não existe o método', method)

