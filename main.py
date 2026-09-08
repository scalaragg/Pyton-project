"""## Версия 0.0.2

-[x] реализовать место хранения задач
-[x] сделать функцию - показать задачи
- [x] сделать функцию - создать задачу
-[x] сделать функцию - редактировать задачу
- [x] сделать функцию -  удалить задачу

"""

collection = [] #list

task_number = 0

is_start = True #flag

while is_start:

    print("1 - показать задачи | 2 - добавить задачу | 3 - редактировать задачу | 4 - удалить задачу")

    choice_user = input('Введите ваш выбор ( 1 | 2 | 3 | 4 )')

    if choice_user == '1' or choice_user == '2' or choice_user == '3' or choice_user == '4':
        match int(choice_user):
            case 1:

                print(collection)

            case 2:
                task_name = input('Название задачи (или оставьте пустым): ')
                match (task_name):
                    case "":
                        task_name: str = 'task'
                        task_number += 1
                        collection.append(f"{task_name} {task_number}")
                    case _:
                        collection.append(f"{task_name}")
                print(collection)

            case 3:

                edit_task = input('Какую задачу вы хотите редактировать (введите название задачи): ')
                if edit_task in collection:
                    task_pos = collection.index(edit_task)
                    collection.pop(task_pos)
                    new_task = input('Новое название задачи: ')
                    collection.insert(task_pos, new_task)
                else:
                    print('такой задачи нет')
                print(collection)

            case 4:
                delete_task = input('Какую задачу вы хотите удалить (введите название задачи): ')
                if delete_task in collection:
                    collection.remove(delete_task)
                print(collection)

            case _:

                print('такого пункта нет!')

    elif choice_user != '1' or choice_user != '2' or choice_user != '3' or choice_user != '4':
        pass