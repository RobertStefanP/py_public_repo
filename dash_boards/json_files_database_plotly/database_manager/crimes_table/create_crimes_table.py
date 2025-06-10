import sqlite3


conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS crimes_data (
        year INTEGER PRIMARY KEY,
        crimes INTEGER
    )
""")

conn.commit()
conn.close()
