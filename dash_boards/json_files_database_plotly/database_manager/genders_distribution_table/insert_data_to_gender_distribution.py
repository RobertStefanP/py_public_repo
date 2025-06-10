import json
import sqlite3


with open("../../json_files/madrid_gender_distribution.json", "r", encoding="utf-8") as file:
    raw_data = json.load(file)
    
conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

for entry in raw_data:
    gender = entry['MetaData'][1]['Nombre']
    for detail in entry['Data']:
        year = detail['Anyo']
        value = detail['Valor']
        if gender == "Hombres":
            cursor.execute("INSERT INTO madrid_gender_distribution (year, males) VALUES (?, ?) ON CONFLICT(year) DO UPDATE SET males = excluded.males", (year, value))           
        elif gender == "Mujeres":        
            cursor.execute("INSERT INTO madrid_gender_distribution (year, females) VALUES (?, ?) ON CONFLICT(year) DO UPDATE SET females = excluded.females", (year, value))
            
conn.commit()
conn.close()
