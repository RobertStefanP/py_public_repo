import sqlite3

conn = sqlite3.connect("projects.db")
cursor = conn.cursor()

#cursor.execute("DROP TABLE madrid_gender_distribution")

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

cursor.execute("PRAGMA table_info(births_data);")
print(cursor.fetchall())

cursor.execute("PRAGMA table_info(crimes_data);")
print(cursor.fetchall())

cursor.execute("PRAGMA table_info(crimes_comparison_data);")
print(cursor.fetchall())

cursor.execute("PRAGMA table_info(employment_rate);")
print(cursor.fetchall())

cursor.execute("PRAGMA table_info(poblacion_coslada);")
print(cursor.fetchall())

cursor.execute("PRAGMA table_info(madrid_gender_distribution);")
print(cursor.fetchall())

cursor.execute("PRAGMA table_info(madrid_groups_age);")
print(cursor.fetchall())




conn.close()