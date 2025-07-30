import sqlite3

CONN = sqlite3.connect('databse.db')
CURSOR = CONN.cursor()

with open('setup.sql', 'r') as f:
    CURSOR.executescript(f.read())

CONN.commit()
CONN.close()

print("✅ database.db initialized from setup.sql")