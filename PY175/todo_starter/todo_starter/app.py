from flask import Flask, render_template, redirect, url_for, session, request, flash
from uuid import uuid4
from todos.utils import error_for_list_title, find_list_by_id, error_for_todo_title, find_todo_by_id, delete_todo_by_id, todos_remaining, is_list_completed, sort_items, is_todo_completed
from werkzeug.exceptions import NotFound
from functools import wraps
import os


app = Flask(__name__)
app.secret_key='secret1'

def require_list(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        list_id = kwargs.get('list_id')
        lst = find_list_by_id(session['lists'], list_id)
        if not lst:
            raise NotFound(description="List not found")
        return f(lst=lst, *args, **kwargs)

    return decorated_function

def require_todo(f):
    @wraps(f)
    @require_list
    def decorated_function(lst, *args, **kwargs):
        todo_id = kwargs.get('todo_id')
        todo = find_todo_by_id(lst['todos'], todo_id)
        if not todo:
            raise NotFound(description="Todo not found")
        return f(lst=lst, todo=todo, *args, **kwargs)

    return decorated_function

@app.before_request
def initialize_session():
    if 'lists' not in session:
        session['lists'] = []

@app.route("/")
def index():
    return redirect(url_for('get_lists'))

# Render the list of todo lists
@app.route("/lists", methods=["GET"])
def get_lists():
    lists = sort_items(session['lists'], is_list_completed)
    return render_template('lists.html', lists=lists)

@app.route("/lists", methods=["POST"])
def create_list():
    title = request.form["list_title"].strip()
    error = error_for_list_title(title, session['lists'])
    if error:
        flash(error, "error")
        return render_template('new_list.html', title=title)
    
    session['lists'].append({'id': str(uuid4()), 'title': title, 'todos': []})
    flash("The list has been created.", "success")
    session.modified = True
    return redirect(url_for('get_lists'))

@app.route("/lists/new")
def add_todo():
    return render_template('new_list.html')

@app.route("/lists/<list_id>", methods=["GET"])
@require_list
def show_list(lst, list_id):
    # lst = find_list_by_id(session['lists'], list_id)
    # lst['todos'] = sort_items(lst['todos'], is_todo_completed)
    # adding the wrapper makes it so that we are now passing the specific list we want instead of all lists
    lst['todos'] = sort_items(lst['todos'], is_todo_completed)
    return render_template('list.html', lst=lst)

@app.route("/lists/<list_id>/todos", methods=["POST"])
@require_list
def add_todo_item(lst, list_id):
    todo_name = request.form['todo'].strip()
    error = error_for_todo_title(todo_name)
    if error:
        flash(error, "error")
        return render_template("list.html", lst=lst)
    
    lst['todos'].append({'id': str(uuid4()), 'title': todo_name, 'completed': False})
    flash("Item added!", "success")
    session.modified = True
    return redirect(url_for('show_list', list_id=list_id))

@app.route("/lists/<list_id>/todos/<todo_id>/toggle", methods=['POST'])
@require_todo
def toggle_todo(lst, todo, list_id, todo_id):
    if todo['completed']:
        todo['completed'] = False
    else:
        todo['completed'] = True
    session.modified=True
    flash("The todo has been updated.", "success")
    return redirect(url_for('show_list', list_id=list_id))

@app.route("/lists/<list_id>/todos/<todo_id>/delete", methods=["POST"])
@require_todo
def delete_todo(lst, todo, list_id, todo_id):
    delete_todo_by_id(lst, todo_id)
    flash("The todo item has been deleted.", "success")
    session.modified = True
    return redirect(url_for("show_list", list_id=list_id))
    
@app.route("/lists/<list_id>/complete_all", methods=["POST"])
@require_list
def complete_all(lst, list_id):
    for items in lst['todos']:
        items['completed'] = True  
    session.modified = True
    flash("All todos completed.", "success")
    return redirect(url_for("show_list", list_id=list_id))

@app.route("/lists/<list_id>/edit", methods=["GET"])
@require_list
def edit_list(lst, list_id):
    return render_template("edit_list.html", lst=lst)

@app.route("/lists/<list_id>/delete", methods=["POST"])
@require_list
def delete_list(lst, list_id):
    # refactored to no longer need delete function from utils
    session['lists'] = [lst for lst in session['lists'] if lst['id'] != list_id]
    session.modified = True
    return redirect(url_for('get_lists'))

@app.route("/lists/<list_id>/edit", methods=["POST"])
@require_list
def update_list(lst, list_id):
    title = request.form["list_title"].strip()
    error = error_for_list_title(title, session['lists'])
    if error:
        flash(error, "error")
        return render_template('edit_list.html', lst=lst, title=title)

    lst['title'] = title
    flash("The list has been updated.", "success")
    session.modified = True
    return redirect(url_for('get_lists'))

@app.context_processor
def list_utilities_processor():
    return dict(todos_remaining = todos_remaining, is_list_completed=is_list_completed)

if __name__ == "__main__":
    if os.environ.get('FLASK_ENV') == 'production':
        app.run(debug=False)
    else:
        app.run(debug=True, port=5003)