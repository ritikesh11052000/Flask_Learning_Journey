Flask - Week 1, Day 1: Setup & Basics
Today, we'll cover:
✅ Installing Flask
✅ Creating a basic Flask app (app.py)
✅ Running the Flask server
✅ Understanding debug mode

1️⃣ Install Flask
First, ensure you have Python 3.8+ installed.
Then, create a virtual environment (recommended for Flask projects):

bash
Copy
Edit
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
Now, install Flask:

bash
Copy
Edit
pip install flask
2️⃣ Creating Your First Flask App (app.py)
Now, create a simple Flask web server.

📌 Steps:
1️⃣ Create a file app.py
2️⃣ Add the following code:

python
Copy
Edit
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
3️⃣ Running the Flask Server
Now, run your Flask app:

bash
Copy
Edit
python app.py
You will see output like:

bash
Copy
Edit
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
👉 Open your browser and go to http://127.0.0.1:5000/
✅ You should see: "Hello, Flask! Your server is running!"

4️⃣ Understanding Debug Mode (debug=True)
With debug=True, Flask automatically:
✅ Restarts the server when you edit the code
✅ Shows error messages if something breaks

📌 Try modifying the message in return "Hello, Flask!" and save the file. Flask will automatically restart the server!

