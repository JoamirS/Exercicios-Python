import json
import os

NAME_FILE = 'class_12.json'
FILE_PATH_ABSOLUTE = os.path.abspath(os.path.join(os.path.dirname(__file__), NAME_FILE))

string_json = '''
{
    "title": "O Senhor dos Anéis: A sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boroming"],
    "budget": null
}
'''
print(__file__)
print(json.loads(string_json))

with open(FILE_PATH_ABSOLUTE, 'w') as file:
    json.dump(string_json, file)

with open(FILE_PATH_ABSOLUTE, 'r') as file:
    movie_of_json = json.load(file)
    print(movie_of_json)
