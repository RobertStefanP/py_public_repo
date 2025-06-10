import sqlite3

# Step 1: Connect to DB (it will be created if not exists)
conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

# Step 2: Create the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS births_data (
        year INTEGER PRIMARY KEY,
        births INTEGER
    )
""")

# Step 3: Save and close
conn.commit()
conn.close()
