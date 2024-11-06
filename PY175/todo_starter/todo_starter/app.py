from flask import Flask, render_template, redirect, url_for, session, request
from uuid import uuid4


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
    session['lists'].append({'id': str(uuid4()), 'title': title, 'todos': []})
    session.modified = True
    return redirect(url_for('get_lists'))

@app.route("/lists/new")
def add_todo():
    return render_template('new_list.html')

if __name__ == "__main__":
    app.run(debug=True, port=5003)