from flask import Flask, request, redirect, session, render_template

app = Flask(__name__)
app.secret_key = "secret"

# Store users
users = {}

import os
print("Templates Folder Path:", os.path.abspath("templates"))

@app.route('/')
def home():
    # if "user" in session:
    #     #return render_template("dashboard.html", username=session['user'], user_data=users[session['user']])
    return render_template("splash.html")
    #return "Hello, Flask is running!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['email']
        pwd = request.form['password']
        if name in users and users[name]["password"] == pwd:
            session['user'] = name
            return redirect('/dashboard')
        return render_template("login.html", error="Incorrect login!")
    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['email']
        pwd = request.form['password']
        users[name] = {
            "password": pwd,
            "name": request.form['name'],
            "mobile": request.form['mobile'],
            "university": request.form['university']
        }
        return redirect('/login')
    return render_template("register.html")

@app.route('/dashboard')
def dashboard():
    if "user" not in session:
        return redirect('/login')
    user_data = users[session['user']]
    return render_template("dashboard.html", username=session['user'], user_data=user_data)

@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
