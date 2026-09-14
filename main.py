"""## Версия 0.0.4

    Точка входа в пиложение Task Manadger
    --- decsription ---
    приложение сохраняет
"""

collection = [] #list

task_number = 0

is_start = True #flag

def show_collection(task_collection):
    print('=' * 30)
    for task_number, j in enumerate(collection):
        print(f"{task_number + 1}. {j}")
    print('=' * 30)

while is_start:

    print("1 - показать задачи | 2 - добавить задачу | 3 - редактировать задачу | 4 - удалить задачу")

    choice_user = input('Введите ваш выбор ( 1 | 2 | 3 | 4 )')

    if choice_user == '1' or choice_user == '2' or choice_user == '3' or choice_user == '4':
        match int(choice_user):

            case 1:
                show_collection(collection)
            case 2:
                task_name = input('Название задачи (или оставьте пустым): ')
                match (task_name):
                    case "":
                        task_name: str = 'task'
                        task_number += 1
                        collection.append(f"{task_name} {task_number}")
                    case _:
                        collection.append(f"{task_name}")
                show_collection(collection)

            case 3:
                show_collection(collection)
                edit_task = input('Какую задачу вы хотите редактировать (введите название задачи): ')
                if edit_task in collection:
                    task_pos = collection.index(edit_task)
                    collection.pop(task_pos)
                    new_task = input('Новое название задачи: ')
                    collection.insert(task_pos, new_task)
                else:
                    print('такой задачи нет')
                show_collection(collection)

            case 4:
                show_collection(collection)
                delete_task = input('Какую задачу вы хотите удалить (введите название задачи): ')
                if delete_task in collection:
                    collection.remove(delete_task)
                show_collection(collection)
            case _:

                print('такого пункта нет!')

    elif choice_user != '1' or choice_user != '2' or choice_user != '3' or choice_user != '4':
        pass