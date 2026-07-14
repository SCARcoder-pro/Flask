from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))

        conn.commit()
        conn.close()

        return redirect(url_for('success')) 
    return render_template('register.html')

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cur.fetchone()
        conn.close()

        if user:
            return redirect(url_for('dashboard'))
        else:
            return "Invalid username or password"
        
    return render_template('login.html')
@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/resume", methods=["GET", "POST"])
def resume():
    fullname = request.form["fullname"]
    address = request.form["address"]
    email = request.form["email"]
    mobile = request.form["mobile"]
    skills = request.form["skills"]

    image = request.files["image"]
    image_path = "static/ + image.filename"
    image.save(image_path)

    return render_template("resume.html",
                           fullname=fullname,
                           address=address,
                           email=email,
                           mobile=mobile,
                           skills=skills,
                           image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)