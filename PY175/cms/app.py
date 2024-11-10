from flask import Flask, render_template, send_from_directory, flash, redirect, url_for, request, session
import os
from markdown import markdown

app = Flask(__name__)
app.secret_key = 'secret'

@app.route("/")
def index():

    root = os.path.abspath(os.path.dirname(__file__))
    data_dir = os.path.join(root, "cms/data")
    files = [os.path.basename(path) for path in os.listdir(data_dir)]
    return render_template('index.html', files=files)

@app.route("/<file_name>")
def get_file(file_name):
    root = os.path.abspath(os.path.dirname(__file__))
    data_dir = os.path.join(root, "cms/data/")
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
    root = os.path.abspath(os.path.dirname(__file__))
    data_dir = os.path.join(root, "cms/data")
    with open(data_dir + f'/{file_name}', 'r') as file:
        contents = file.read()
    return render_template('edit_file.html', content=contents, file_name=file_name, title=file_name)

@app.route("/<file_name>/edit", methods=["POST"])
def save_changes(file_name):
    root = os.path.abspath(os.path.dirname(__file__))
    data_dir = os.path.join(root, "cms/data")
    with open(data_dir + f'/{file_name}', 'w') as file:
        modified_data = request.form['file_content'].strip()
        file.write(modified_data)
        flash(f"{file_name} has been updated.")
        session.modified = True
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True, port=5003)