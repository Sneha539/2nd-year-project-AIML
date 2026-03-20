import sqlite3

def init_db():
    conn = sqlite3.connect("intrusions.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS intrusions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        status TEXT,
        image_path TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_intrusion(timestamp, status, image_path):
    conn = sqlite3.connect("intrusions.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO intrusions (timestamp, status, image_path)
    VALUES (?, ?, ?)
    """, (timestamp, status, image_path))

    conn.commit()
    conn.close()