from lib.todo_list import *
from lib.todo import *
def test_instantiate_todo_list():
    todo = TodoList()
    assert todo.todo_list == []

def test_add_todo_task_to_list():
    todo = TodoList()
    task_1 = Todo("Walk the dog")
    todo.add(task_1)
    #assert todo.todo_list == [Todo]
    assert todo.incomplete() == [task_1]

def test_for_add_task_and_go_complete():
    todo = TodoList()
    task_1 = Todo("Walk the dog")
    task_2 = Todo("Walk the cat")
    task_3 = Todo("Walk the mouse")
    todo.add(task_1)
    todo.add(task_2)
    todo.add(task_3)

    Todo.mark_complete(task_2)
    actual_result = todo.complete()
    expected_result = [task_2]

    assert actual_result == expected_result

