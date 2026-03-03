from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

LOG_FILE = "logs.csv"

def read_logs():
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, newline='') as file:
            reader = csv.DictReader(file)
            logs = list(reader)
            logs.reverse()  # Show latest first
    return logs

@app.route("/")
def index():
    logs = read_logs()
    total_intrusions = len(logs)
    return render_template("index.html", logs=logs, total_intrusions=total_intrusions)

if __name__ == "__main__":
    app.run(debug=True)