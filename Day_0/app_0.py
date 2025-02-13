from flask import Flask

# Initialize Flask app
app = Flask(__name__)

# Define a basic route
@app.route('/')
def home():
    return "Hello, Flask! Your server is running!"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
