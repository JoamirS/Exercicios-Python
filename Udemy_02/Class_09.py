"""
Sistema de perguntas e respostas
"""
import sys

questions = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4'
    },

    {
        'Pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25'
    },

    {
        'Pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5'
    }
]


def validate_options_input(input_option):
    tuple_options = (1, 2, 3)
    if input_option not in tuple_options:
        return False


def select_question(input_option):
    correct_index_question = input_option - 1
    get_question = questions[correct_index_question]['Pergunta']
    return get_question


def give_options(input_option):
    correct_index_options = input_option - 1
    get_options = questions[correct_index_options]['Opções']
    return get_options


def check_answer(input_answer, correct_answer):
    if input_answer == correct_answer:
        return True


print('Selecione uma das três perguntas abaixo')
number_of_options = 1
for question in questions:
    print(question['Pergunta'] + ' ' + f'Opção de número {number_of_options}')
    number_of_options += 1

select_question_to_be_answer = int(input('Qual pergunta quer responder? '))

result_validation_option_input = validate_options_input(select_question_to_be_answer)

if result_validation_option_input is False:
    print('Escolha uma opção válida')
    sys.exit()

result_selection = select_question(select_question_to_be_answer)
print(result_selection)

options_question_selection = give_options(select_question_to_be_answer)
print(f'As opções são: {options_question_selection}')

input_answer_attempt = input('Selecione uma resposta: ')
correct_answer_to_question = questions[select_question_to_be_answer - 1]['Resposta']

if input_answer_attempt not in options_question_selection:
    print('A sua resposta não está entre as opções.')
    sys.exit()

result_check_alternative = check_answer(input_answer_attempt, correct_answer_to_question)
if result_check_alternative:
    print('Resposta correta')
else:
    print('Opção errada')
