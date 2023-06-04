"""
Closure e funçoes que retornam outras funções
"""


def create_salutation(salutation):
    def salute(name):
        return f'{salutation}, {name}'
    return salute


speak_good_morning = create_salutation('Bom dia')
speak_good_night = create_salutation('Boa noite')

for name in ['João', 'Maria', 'José']:
    print(speak_good_morning(name))
