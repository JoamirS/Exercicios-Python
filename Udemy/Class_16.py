"""
Faça um jogo para o usuário advinhar qual a palavra secreta.
    Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
    Quando o usuário digitar uma letra digitada está na palavra secreta:
        Se a letra digitada estiver na palavra secreta; exiba e letra;
        Se a letra digitada não estiver na palavra secreta;.
    Faça a contagem de tentativas de seu usuário.
"""


def restriction_only_one_letter(input_letter_user):
    if len(input_letter_user) > 1:
        return False
    else:
        return True


def check_letter_in_secret_word(input_letter_user, secret_word_input):
    if input_letter_user in secret_word_input:
        return True
    else:
        return False


secret_word = 'Joamir'
break_program = 'N'
counter_attempt = 0

while break_program != 'S':
    print('Digite uma letra que acredita estar na palavra secreta.')
    attempt_user = input(': ')

    counter_attempt += 1

    check_input_length = restriction_only_one_letter(attempt_user)
    if check_input_length:
        print('Seu valor digitado é apenas uma letra.')
    else:
        print('Seu valor digitado é mais de uma letra')
        break

    check_letter_is_valid = check_letter_in_secret_word(attempt_user, secret_word)
    if check_letter_is_valid:
        print(f"A letra '{attempt_user}' está na palavra secreta.")
    else:
        print(f"A letra '{attempt_user}' não está na palavra secreta.")

    break_program = input('Deseja encerrar o programa? ')
print('Programa encerrado')
print(f'Você tentou {counter_attempt} vezes')
