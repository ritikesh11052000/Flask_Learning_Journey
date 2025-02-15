1. Dynamic Routes in Flask
Dynamic routes allow you to create routes that can accept variables in the URL. This is useful for building applications where the route depends on a certain input, such as a user ID or product ID.

For example:

python
Copy
Edit
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'
In this example, <username> is a dynamic segment in the URL. Flask will pass the value of username in the URL to the show_user_profile() function.

2. HTTP Methods (GET, POST)
Flask supports various HTTP methods, such as GET (default) and POST, to interact with data. You can specify which methods a route will accept.

Example:
python
Copy
Edit
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"Logged in with {username} and {password}"
    return render_template('login.html')
GET: Used to fetch a page or data.
POST: Used to send data to the server (like from a form).
In this example:

If the request method is GET, Flask renders the login page.
If the request method is POST, Flask processes the form data.
3. Template Inheritance
Template inheritance allows you to create a base template that contains common elements (e.g., header, footer, navigation) and extend it for specific pages.

Base template (base.html):
html
Copy
Edit
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Flask App{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Welcome to My Flask App</h1>
    </header>
    <div>
        {% block content %}{% endblock %}
    </div>
    <footer>
        <p>Footer content</p>
    </footer>
</body>
</html>
Extending template (home.html):
html
Copy
Edit
{% extends "base.html" %}

{% block title %}Home{% endblock %}

{% block content %}
    <h2>Welcome to the homepage!</h2>
    <p>This is the home page content.</p>
{% endblock %}
The {% extends "base.html" %} tag tells Flask that this page extends the base template.
The {% block %} tags define sections where content can be added or overridden.
4. Error Handling in Flask
Flask provides a way to handle errors and display custom error messages. Common HTTP errors like 404 (Page Not Found) or 500 (Internal Server Error) can be caught and customized.

For example, here’s how to handle a 404 error (page not found):

python
Copy
Edit
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
When a 404 error occurs, Flask will render the 404.html template.
Example of a 404 page (404.html):
html
Copy
Edit
<!DOCTYPE html>
<html>
<head>
    <title>404 - Not Found</title>
</head>
<body>
    <h1>Oops! Page Not Found</h1>
    <p>Sorry, we couldn't find the page you're looking for.</p>
</body>
</html>
Similarly, you can create custom error pages for other HTTP status codes like 500 Internal Server Error.
5. Redirects and URL Building
Flask provides functionality to redirect users to another page and also to build dynamic URLs.

Redirect example:
python
Copy
Edit
from flask import redirect, url_for

@app.route('/home')
def home():
    return redirect(url_for('index'))
Here, the redirect(url_for('index')) will redirect the user to the / route (mapped to the index() function).

URL Building example:
python
Copy
Edit
@app.route('/user/<username>')
def user_profile(username):
    return f'Profile of {username}'

@app.route('/redirect_to_user/<username>')
def redirect_to_user(username):
    return redirect(url_for('user_profile', username=username))
In this example, url_for('user_profile', username=username) builds the URL for the user_profile route and passes the username.

Summary of Day 2:
Dynamic Routes: You can create routes that accept variable parts in the URL.
HTTP Methods (GET & POST): Use GET for retrieving data and POST for sending data.
Template Inheritance: You can extend a base template to avoid repeating common elements.
Error Handling: Customize error pages like 404 or 500.
Redirects and URL Building: Redirect users and dynamically generate URLs.
