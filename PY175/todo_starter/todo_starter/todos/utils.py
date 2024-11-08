
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

def delete_list_by_id(session_lists, lst_id):
    lst_to_delete = find_list_by_id(session_lists, lst_id)
    session_lists.remove(lst_to_delete)
    return None

def todos_remaining(lst):
    return sum(1 for todo in lst['todos'] if not todo['completed'])

def is_list_completed(lst):
    return len(lst['todos']) > 0 and todos_remaining(lst) == 0

def is_todo_completed(todo):
    return todo['completed']


def sort_items(items, select_completed):
    sorted_items = sorted(items, key=lambda item: item['title'].lower())

    incomplete_items = [item for item in sorted_items
                        if not select_completed(item)]
    complete_items = [item for item in sorted_items
                      if select_completed(item)]

    return incomplete_items + complete_items
