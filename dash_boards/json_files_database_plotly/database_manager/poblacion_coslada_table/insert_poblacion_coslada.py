import json
import sqlite3


with open("../../json_files/poblacion_coslada.json", "r", encoding="utf-8") as file:
    raw_data = json.load(file)
    
data_total = raw_data[0]
conn = sqlite3.connect("../projects.db")
cursor = conn.cursor()

for entry in data_total['Data']:
    year = entry['Anyo']
    poblacion = entry['Valor']    
    cursor.execute("INSERT OR IGNORE INTO poblacion_coslada (year, poblacion) VALUES (?, ?)", (year, poblacion))
    
conn.commit()
conn.close()
