import json
import sqlite3


with open("../../json_files/crimes.json", "r", encoding="utf-8") as file:
    raw_data = json.load(file)

conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

for entry in raw_data:
    if entry["Nombre"] == "Total Nacional. Dato base. Delitos. Hombres. ":
        for data in entry["Data"]:
            year = data["Anyo"]
            males = int(data["Valor"])
            cursor.execute("INSERT OR IGNORE INTO crimes_comparison_data (year, males) VALUES (?, ?)", (year, males))
            
    elif entry["Nombre"] == "Total Nacional. Dato base. Delitos. Mujeres. ":
        for data in entry["Data"]:
            year = data["Anyo"]
            women = int(data["Valor"])
            cursor.execute("UPDATE crimes_comparison_data SET women = ? WHERE year = ?", (women, year))
            
conn.commit()
conn.close()
