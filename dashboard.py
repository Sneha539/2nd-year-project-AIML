from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import csv
import os

app = Flask(__name__)
app.secret_key = "super_secret_key"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Simple user database (for prototype)
USERS = {
    "admin": {"password": "admin123"}
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

LOG_FILE = "logs.csv"

def read_logs():
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, newline='') as file:
            reader = csv.DictReader(file)
            logs = list(reader)
            logs.reverse()
    return logs

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in USERS and USERS[username]["password"] == password:
            user = User(username)
            login_user(user)
            return redirect(url_for("dashboard"))

        return "Invalid login"

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/")
@login_required
def dashboard():
    logs = read_logs()
    total_intrusions = len(logs)
    return render_template("index.html", logs=logs, total_intrusions=total_intrusions)

@app.route('/intruders/<path:filename>')
@login_required
def intruder_image(filename):
    from flask import send_from_directory
    return send_from_directory('intruders', filename)

if __name__ == "__main__":
    app.run(debug=True)