import json
import sqlite3


with open("../../json_files/crimes.json", "r", encoding="utf-8") as file:
    raw_data = json.load(file)

conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

for entry in raw_data:
    print(f"entry: {entry}")
    for data in entry["Data"]:
        print(data["Anyo"])
        year = data["Anyo"]
        crimes = int(data["Valor"])
        cursor.execute("INSERT OR IGNORE INTO crimes_data (year, crimes) VALUES (?, ?)", (year, crimes))

conn.commit()
conn.close()
