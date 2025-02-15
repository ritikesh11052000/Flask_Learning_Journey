from flask import Flask
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/hello/<name>')  # Dynamic route with a variable <name>
def hello_user(name):
    return f"Hello, {name}!"
#How it Works:
#If a user visits http://127.0.0.1:5000/hello/Ritikesh, the page will display "Hello, Ritikesh!".
#The <name> part in @app.route('/hello/<name>') acts as a placeholder for any string value.

@app.route('/user/<int:user_id>')
def show_user(user_id):
    return f"User ID: {user_id}"

#Valid URLs: /user/42, /user/123
#Invalid URL: /user/abc (causes a 404 error because "abc" is not an integer)

@app.route('/profile/<string:username>/<int:age>')
def user_profile(username, age):
    return f"User: {username}, Age: {age}"

#Visiting /profile/Ritikesh/20 will display "User: Ritikesh, Age: 20".

@app.route('/download/<path:filepath>')
def download(filepath):
    return f"Downloading file from: {filepath}"

#Visiting /download/images/pic.jpg will return "Downloading file from: images/pic.jpg".

@app.route('/square/<int:number>')
def square(number):
    return f"The square of {number} is {number**2}"

@app.errorhandler(404)
def page_not_found(error):
    return "Oops! This page doesn't exist.", 404

#/square/5 → "The square of 5 is 25"
#/square/abc → 404 error page


if __name__ == "__main__":
    app.run(debug=True)
#Summary
#✅ Dynamic routes allow you to accept variables in URLs.
#✅ You can specify types like int, float, and path.
#✅ Multiple parameters can be passed in a single route.
#✅ Dynamic routes can be used for redirection and file paths.
#✅ Handling errors properly improves user experience.



