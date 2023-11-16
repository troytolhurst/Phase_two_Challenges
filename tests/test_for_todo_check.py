from lib.todo_check import *

def test_for_todo_empty_string():
    result = todo_check(" ")
    assert result == "You have no task"

def test_for_todo_lowercase():
    result = todo_check("you have to make breakfast #todo")
    assert result == "You have a task to do"

def test_for_todo_with_no_hashtag():
    result = todo_check(" you have so much todo")
    assert result == "You have no task"

def test_for_todo_with_task_todo():
    result = todo_check("make world domination plans #TODO")
    assert result == "You have a task to do"