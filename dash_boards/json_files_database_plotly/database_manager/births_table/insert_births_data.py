import json
import sqlite3

# 1. Load JSON from file
with open("../../json_files/births.json", "r", encoding="utf-8") as file:
    raw_data = json.load(file)

# 2. Extract the "Data" list (first item, then ["Data"])
data_list = raw_data[0]["Data"]

# 3. Connect to database
conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

# 4. Insert each row
for entry in data_list:
    year = entry["Anyo"]
    births = int(entry["Valor"])
    cursor.execute("INSERT OR IGNORE INTO births_data (year, births) VALUES (?, ?)", (year, births))

# 5. Commit and close
conn.commit()
conn.close()
