import json

# person = {
#     'Name': 'Oscar Fletcher',
#     'Surname': 'Miranda',
#     'Address': [
#         {'Street': 'S1', 'Number': 32},
#         {'Street': 'S2', 'Number': 55}
#     ],
#     'Height': 1.8,
#     'Prefer_numbers': (2, 4, 6, 8, 10),
#     'Dev': True,
#     'Nothing': None,
# }
#
# with open('Class_47.json', 'w') as file:
#     json.dump(
#         person, file, ensure_ascii=False, indent=2
#     )

with open('Class_47.json', 'r', encoding='utf-8') as file:
    person = json.load(file)
    print(person)
    print(person['Name'])
