"""
Split and join with list and str
split - cut a string
join - inite a string
"""


frase = 'Olha só, que coisa interessante'
# separate the frase with comma
list_words = frase.split(',')

print(list_words)

for i, frase in enumerate(list_words):
    print(list_words[i].strip())


frase_with_join = ','.join(list_words)
print(frase_with_join)
