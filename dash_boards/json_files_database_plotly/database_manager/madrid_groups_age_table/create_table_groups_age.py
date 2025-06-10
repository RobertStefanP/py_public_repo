import sqlite3


conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS madrid_groups_age(
                age INTEGER PRIMARY KEY,
                males INTEGER, females INTEGER)""")
conn.commit()
conn.close()
