# Implementation details for CMS

## Creating new documents

- When user views index page, they should see a link that says "New Document."
    1. Create a new `href` at the bottom of the index page that links to the `/new` route in the `index.html` file
    2. Create the `/new` get route in the `app` file
- When user clicks "New Document" link, taken to page with a text input labeled "Add a new document:" and submit button labeled "Create"
    1. Create a new `new.html` file for the route created above to render
    2. Include a submission form with the appropriate labels in the `new.html` file to be displayed.
- When "Create" is clicked, user is redirected to index page. Display a flash message with the name they entered for the new file saying "X.X has been created."
    1. Create a `POST` route for the `/new` route that creates the new file entered in the submission box
    2. Create flash message
    3. Do error checking so that if a user attempts to submit a new document without a name, the submission form is re-displayed with a flash message "A name is required."
    4. If name meets criteria, redirect to `index` and display flash