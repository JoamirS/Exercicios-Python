"""
Make a shopping list with lists. The User must be able to insert, delete, and list values of his
list. Don't allow the program to break with errors for non-existent indexes in the list.
"""

shopping_list = list()
tuple_choices = (1, 2, 3)
break_while = 'N'


def restriction_empty_shopping_list(length_list):
    if len(length_list) > 1:
        return True
    else:
        return False


def check_index_in_list(list_user, position):
    try:
        index_check_value = list_user[position]
        return True
    except IndexError:
        return False


while break_while != 'S':
    print('Você pode inserir (1), apagar(2), mostrar os produtos da lista(3).')
    input_choice_user = int((input('Selecione uma das três opções: ')))

    if input_choice_user not in tuple_choices:
        print('Você não digitou uma opção válida')
        break

    if input_choice_user == 1:
        insert_input_user = str(input('Insira um produto na lista: '))
        shopping_list.append(insert_input_user)

    if input_choice_user == 2:
        input_remove_user_position = int(input('Escolha uma posição para remover da lista: '))
        if restriction_empty_shopping_list(shopping_list) is False:
            print('A lista está vazia')
            break

        if check_index_in_list(shopping_list, input_remove_user_position):
            shopping_list.pop(input_remove_user_position)
            print('Posição removida')
        else:
            print('Posição não removida')
            break

    if input_choice_user == 3:
        print(f'Aqui está a lista: {shopping_list}')

    break_while = input('Deseja sair do programa: ')
print('Programa finalizado')
