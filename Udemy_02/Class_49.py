"""
List tasks with undo and redo
all = [] -> list of tasks
all = ['Make coffee'] -> Add make coffee
all = ['make coffee', 'to walk'] -> Add to walk
undo = ['make coffee',] -> redo ['walk']
undo = [] -> redo ['walk', 'make coffee']
undo = all['make coffee']
undo = all['make coffee', 'to walk']
"""


def show_tasks(input_list=None):
    if not input_list:
        print('Sem tarefas para mostrar')
    else:
        print(f'As tarefas são: {input_list}')


def delete_last_command_and_return_deleted(list_task_delete_input):
    if not list_task_delete_input:
        return []
    return [list_task_delete_input.pop()]


list_with_tasks = []
list_with_command_deleted = []
immutable_commands_actions_in_list = ('listar', 'desfazer', 'refazer')

while True:
    print('Comandos: listar, desfazer, refazer')
    input_user = input('Digite uma tarefa ou comando: ')

    if input_user in immutable_commands_actions_in_list[0]:
        show_tasks(list_with_tasks)

    elif input_user in immutable_commands_actions_in_list[1]:
        if not list_with_tasks:
            print('Nada a desfazer')
        else:
            list_with_command_deleted.append(delete_last_command_and_return_deleted(list_with_tasks))
            print(list_with_command_deleted)

    elif input_user in immutable_commands_actions_in_list[2]:
        if not list_with_command_deleted:
            print('Nada a refazer')
        else:
            list_with_tasks.append(list_with_command_deleted.pop())

    else:
        list_with_tasks.append(input_user)
