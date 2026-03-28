from flask import Flask, render_template, request, redirect, url_for, send_from_directory, abort
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
import sqlite3
import cv2
from flask import Response

camera = cv2.VideoCapture(0)
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

app = Flask(__name__)
app.secret_key = "super_secret_key"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Simple user database (for prototype)
USERS = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "viewer": {
        "password": "viewer123",
        "role": "viewer"
    }
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username
        self.role = USERS[username]["role"]

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

def read_logs():
    conn = sqlite3.connect("intrusions.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT timestamp, status, image_path
    FROM intrusions
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    logs = []

    for row in rows:
        logs.append({
            "timestamp": row[0],
            "status": row[1],
            "image_path": row[2]
        })

    return logs

@app.route('/video_feed')
@login_required
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

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

    return render_template(
        "index.html",
        logs=logs,
        total_intrusions=total_intrusions,
        role=current_user.role
    )

@app.route("/admin")
@login_required
def admin_panel():
    if current_user.role != "admin":
        abort(403)

    return "Admin Panel Access Granted"

@app.errorhandler(403)
def forbidden(e):
    return "Access Denied (Admin Only)", 403
@app.route('/intruders/<path:filename>')
@login_required
def intruder_image(filename):
    from flask import send_from_directory
    return send_from_directory('intruders', filename)

if __name__ == "__main__":
    app.run(debug=True)