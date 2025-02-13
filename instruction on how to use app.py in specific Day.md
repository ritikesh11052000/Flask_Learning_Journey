# Step 1: Clone the Repository
```bash
git clone https://github.com/ritikesh11052000/Flask_Learning_Journey.git
```

# Go to the project folder
```bash
cd Flask_Learning_Journey
```

# Step 2: Run the Flask App
```bash
python app_0.py
```
# If you get an error like:
```bash
python: can't open file 'app_0.py': No such file or directory
```
It means the file isn't found in the current folder.

# Step 3: Go to the Correct Folder
```bash
cd Day_0
```

# Step 4: Install Flask (If Needed)
If you see an error like:
```bash
ModuleNotFoundError: No module named 'flask'
```
You need to install Flask. Run this command:
```bash
pip install flask
```

# Step 5: Run the Flask App Again
```bash
python app_0.py
```
You should see something like this:
```bash
* Running on http://127.0.0.1:5000
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser to see your Flask app!

# Step 6: Navigating Directories
Here are some helpful commands to move around:

# Go up one level
```bash
cd ..
```

# Go back to your home directory
```bash
cd ~
```

# See which directory you're in
```bash
pwd
```

# Step 7: Committing Changes to Git
If you made changes and want to save them to GitHub, use these commands:

# Stage your changes
```bash
git add .
```

# Commit your changes
```bash
git commit -m "Add Day_0 folder and app_0.py"
```

# Push your changes to GitHub
```bash
git push origin main
```

---

**Notes:**

- Make sure you're in the correct folder before running any commands.
- Flask usually runs on [http://127.0.0.1:5000](http://127.0.0.1:5000) unless you change it.
- If you see any errors, double-check if you're in the right folder or need to install Flask.
```
