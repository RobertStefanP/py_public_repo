import sqlite3


conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employment_rate 
    (year INTEGER PRIMARY KEY,
    rate FLOAT
    )
""")

conn.commit()
conn.close()
