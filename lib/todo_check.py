def todo_check(string):
    if "#TODO" in string or "#todo" in string:
        return "You have a task to do"
    else: 
        return "You have no task"
