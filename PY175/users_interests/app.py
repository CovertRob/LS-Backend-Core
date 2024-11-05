'''
Problem: Create a webpage that manages and displays users and their interests

    Requirements:
    1. User loads home page, redirect to a page that lists all of the users' names. (Loaded from the users.yaml file)
        - users' names should be a link to a page for that user
    2. Each user's page dispay: email address, interests with a comma appearing between each interest
        - At bottom of each user's page, list links to all of the other users pages - not including the current user's page
    3. Add a layout to the application - bottom of every page display a message like: "There are 3 users with a total of 9 interests."
        - Update to be dynamic based on the number of users and interests based on the content of the YAML file
        - Use a view helper method, count_interests, to determine the total numer of interests across all users
    4. Add a new user to the YAML file and ensure the site updates accordingly

    # Combine links to other users and the dynamic amount of users and interests footer display into one

Examples / Test Cases:

Data Structures:

Algorithm:

Code:
'''

from flask import Flask, g, redirect, render_template
import yaml

app = Flask(__name__)

@app.before_request
def load_users():
    with open("users.yaml", "r") as file:
        g.users = yaml.safe_load(file)
        
        
@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def users():
    return render_template('users.html', users=g.users)

@app.route("/users/<name>")
def individual_user(name):
    try:
        user = g.users[name]
        email = user['email']
        interests = user['interests']
        return render_template('individual_user.html', person=name, email=email, interests=interests, users=g.users, num_users=len(g.users), num_interests=count_interests())
    except KeyError:
        return redirect("/")
    
    
@app.errorhandler(404)
def page_not_found(_error):
    return redirect("/")

@app.template_filter('list_interests')
def list_interests(interests):
    return ', '.join(interests)

def count_interests():
    num_interests = 0
    for user in g.users.values():
        num_interests += len(user['interests'])
    return num_interests

if __name__ == "__main__":
    app.run(debug=True, port=5003)