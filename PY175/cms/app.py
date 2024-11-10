from flask import Flask, render_template, send_from_directory, flash, redirect, url_for, request, session
import os
from markdown import markdown

app = Flask(__name__)
app.secret_key = 'secret'

def get_data_path():
    if app.config['TESTING']:
        return os.path.join(os.path.dirname(__file__), 'tests', 'data')
    else:
        return os.path.join(os.path.dirname(__file__), 'cms/data')

@app.route("/")
def index():

    data_dir = get_data_path()
    files = [os.path.basename(path) for path in os.listdir(data_dir)]
    return render_template('index.html', files=files)

@app.route("/<file_name>")
def get_file(file_name):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, file_name)
    _name, ext = os.path.splitext(file_name)

    if os.path.isfile(file_path):
        if ext == '.md':
            with open(file_path, 'r') as file:
                return markdown(file.read())
        else:
            return send_from_directory(data_dir, file_name)
    else:
        flash(f"{file_name} does not exist")
        return redirect(url_for('index'))
    
@app.route("/<file_name>/edit", methods=["GET"])
def edit_file(file_name):
    data_dir = get_data_path()
    with open(data_dir + f'/{file_name}', 'r') as file:
        contents = file.read()
    return render_template('edit_file.html', content=contents, file_name=file_name, title=file_name)

@app.route("/<file_name>/edit", methods=["POST"])
def save_changes(file_name):
    data_dir = get_data_path()
    with open(data_dir + f'/{file_name}', 'w') as file:
        modified_data = request.form['content'].strip()
        file.write(modified_data)
        flash(f"{file_name} has been updated.")
        session.modified = True
    return redirect(url_for('index'))

@app.route("/new", methods=["GET"])
def enter_new_document():
    return render_template('new_file.html')

@app.route("/new", methods=["POST"])
def save_new_document():
    new_doc = request.form['new_file']
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, new_doc)
    if len(new_doc) == 0:
        flash("A name is required.")
        session.modified = True
        return render_template("new_file.html"), 422
    elif os.path.exists(file_path):
        flash(f"{new_doc} already exists.")
        return render_template('new_file.html'), 422
    else:
        with open(os.path.join(data_dir, new_doc), 'w') as file:
                file.write('')
        flash(f"{new_doc} has been created.")
        session.modified = True
        return redirect(url_for('index'))
        

if __name__ == '__main__':
    app.run(debug=True, port=5003)