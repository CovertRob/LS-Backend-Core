def error_for_list_title(title, lists):
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique."
    elif not 1 <= len(title) <= 100:
        return "The title must be between 1 and 100 characters"
    else:
        return None
    
def find_list_by_id(lists, list_id):
    for lst in lists:
        if lst['id'] == list_id:
            return lst
    return {}
