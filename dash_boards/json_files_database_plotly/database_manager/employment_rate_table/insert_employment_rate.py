import json
import sqlite3


with open("../../json_files/employment_rate.json", "r", encoding="utf-8") as file:
    raw_data = json.load(file)

data_total = raw_data[0]   

conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

for entry in data_total["Data"]:
    year = entry["Anyo"]
    rate = entry["Valor"]
    cursor.execute("INSERT OR IGNORE INTO employment_rate (year, rate) VALUES (?, ?)", (year, rate))
    
conn.commit()
conn.close()
