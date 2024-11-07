def error_for_list_title(title, lists):
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique."
    elif not 1 <= len(title) <= 100:
        return "The title must be between 1 and 100 characters"
    else:
        return None
    
def error_for_todo_title(title):
    if not 1 <= len(title) <= 100:
        return "The todo name must be between 1 and 100 characters"
    return None
    
def find_list_by_id(lists, list_id):
    for lst in lists:
        if lst['id'] == list_id:
            return lst
    return {}

def find_todo_by_id(todo_lst, todo_id):
    for todo in todo_lst:
        if todo['id'] == todo_id:
            return todo
    return {}

"""
Deletes a todo item from a todo list by re-assigning the list of todo items except for the item specified for deletion.
"""
def delete_todo_by_id(lst, todo_id):
    lst['todos'] = [todo for todo in lst['todos'] if todo['id'] != todo_id]
    return None
