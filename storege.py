##===========================================================
##      Модуль который загружает и сохраняет задачи
##===========================================================
def load_tasks(task_list, name_file):
    with open(name_file, "w", encoding="utf-8") as file:
        file.writelines(task_list)

def save_tasks(name_file):
    try:
        with open(name_file, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        return []