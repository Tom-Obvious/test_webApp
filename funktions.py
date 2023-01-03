import os

FILEPATH: str = "todos.txt"

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w') as file:
        pass


# simple function to
# import the To-Do list
def import_todo_list(filepath=FILEPATH) -> list:
    with open(filepath, 'r') as file:
        todo_list = file.readlines()
    return todo_list


# simple function to
# save the To-Do list
def save_todo_list(todo_list, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todo_list)


# simple function to print out
# the To-Do list
def show_todo_list(todo_list):
    for index, item in enumerate(todo_list):
        print(f"{index + 1}: {item}"[:-1])


# simple function to
# check the To-Do list
def item_in_todo_list(todo_list) -> bool:
    if len(todo_list) == 0:
        return False
    else:
        return True


def check_for_command(usr_npt, command) -> bool:
    if not usr_npt.lower().startswith(command):
        return False
    else:
        return True
