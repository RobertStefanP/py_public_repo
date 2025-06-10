import sqlite3


conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS madrid_gender_distribution
               (year INTEGER PRIMARY KEY,
               males FLOAT, females FLOAT
               )""")
conn.commit()
conn.close()
