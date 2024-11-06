from flask import Flask, render_template, redirect, url_for, session, request, flash
from uuid import uuid4
from todos.utils import error_for_list_title, find_list_by_id
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
def get_todo_list(list_id):
    lists = session['lists']
    todo_list = find_list_by_id(lists, list_id)
    if todo_list:
        return render_template("list.html", lst=todo_list)
    raise NotFound(description="List not Found")

# @app.errorhandler(404)
# def todo_list_not_found(_error):
#     return redirect(url_for("/lists"))
    

if __name__ == "__main__":
    app.run(debug=True, port=5003)