import sqlite3

conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

# Get all rows
cursor.execute("SELECT * FROM crimes_comparison_data")
rows = cursor.fetchall()

# Print
for row in rows:
    print(row)

conn.close()
