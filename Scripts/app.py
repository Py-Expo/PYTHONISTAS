#app.py 
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Process login form data here
        # Redirect to the home page after successful login
        return redirect('/home')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process registration form data here
        # For demonstration purposes, let's assume registration is successful
        # Redirect to the home page after successful registration
        return redirect('/home')
    return render_template('register.html')


@app.route('/home')
def home():
    return render_template('home page.html')

if __name__ == "__main__":
    app.run(debug=True)