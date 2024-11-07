from flask import Flask, render_template, redirect, url_for, session, request, flash
from uuid import uuid4
from todos.utils import error_for_list_title, find_list_by_id, error_for_todo_title, find_todo_by_id, delete_todo_by_id
from werkzeug.exceptions import NotFound


app = Flask(__name__)
app.secret_key='secret1'

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
    return render_template('lists.html', lists=session['lists'])

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
def show_list(list_id):
    lists = session['lists']
    todo_list = find_list_by_id(lists, list_id)
    if todo_list:
        return render_template("list.html", lst=todo_list)
    raise NotFound(description="List not Found")

@app.route("/lists/<list_id>/todos", methods=["POST"])
def add_todo_item(list_id):
    todo_name = request.form['todo'].strip()
    error = error_for_todo_title(todo_name)
    lst = find_list_by_id(session['lists'], list_id)
    if not lst:
        raise NotFound(description="List not found")
    
    if error:
        flash(error, "error")
        return render_template("list.html", lst=lst)
    
    lst['todos'].append({'id': str(uuid4()), 'title': todo_name, 'completed': False})
    flash("Item added!", "success")
    session.modified = True
    return redirect(url_for('show_list', list_id=list_id))

@app.route("/lists/<list_id>/todos/<todo_id>/toggle", methods=['POST'])
def toggle_todo(list_id, todo_id):
    todo_lst = find_list_by_id(session['lists'], list_id)['todos']
    if not todo_lst:
        raise NotFound(description="List not found")
    
    todo_item = find_todo_by_id(todo_lst, todo_id)
    if not todo_item:
        raise NotFound(description="Todo not found")
    
    if todo_item['completed']:
        todo_item['completed'] = False
    else:
        todo_item['completed'] = True
    session.modified=True
    flash("The todo has been updated.", "success")
    return redirect(url_for('show_list', list_id=list_id))

@app.route("/lists/<list_id>/todos/<todo_id>/delete", methods=["POST"])
def delete_todo(list_id, todo_id):
    todo_lst = find_list_by_id(session['lists'], list_id)
    if not todo_lst:
        raise NotFound(description="List not found")
    delete_todo_by_id(todo_lst, todo_id)
    flash("The todo item has been deleted.", "success")
    session.modified = True
    return redirect(url_for("show_list", list_id=list_id))
    
@app.route("/lists/<list_id>/complete_all", methods=["POST"])
def complete_all(list_id):
    todo_list = find_list_by_id(session['lists'], list_id)
    if not todo_list:
        raise NotFound(description="List not found")
    for items in todo_list['todos']:
        items['completed'] = True
        
    session.modified = True
    
    flash("All todos completed.", "success")
    return redirect(url_for("show_list", list_id=list_id))

if __name__ == "__main__":
    app.run(debug=True, port=5003)