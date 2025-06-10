import sqlite3


conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS poblacion_coslada
               (year INTEGER PRIMARY KEY,
               poblacion INTEGER
               )""")

conn.commit()
conn.close()
