FILEPATH = "do.txt"


def get_todo(filepath=FILEPATH):
    """ This function read a text file and return a list"""
    with open(filepath, "r") as file:
        todo_local = file.readlines()
    return todo_local


def write_todo(todo_arg, filepath=FILEPATH):
    """ This function write the list into a text file"""
    with open(filepath, "w") as file:
        file.writelines(todo_arg)
