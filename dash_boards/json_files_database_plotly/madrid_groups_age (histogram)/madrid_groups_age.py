import sqlite3
import pandas as pd
import plotly.express as px


conn = sqlite3.connect("../database_manager/projects.db")

# Select the age group to show 
age_group = "20-30"

df = pd.read_sql_query(f"""
                       SELECT * FROM madrid_groups_age 
                       WHERE age_group = "{age_group}"
                       AND year IS NOT NULL
                       AND age_group IS NOT NULL
                       AND gender IS NOT NULL
                       AND population IS NOT NULL
                       ORDER BY year""", conn)
conn.close()

fig = px.bar(df,
             x="year",
             y="population",
             color="gender",
             barmode="group",  # bars side by side
             title=f"Población {age_group} años en Madrid por sexo")

fig.update_layout(xaxis=dict(type='category'))

fig.update_layout(xaxis_title='Year',
                  yaxis_title='Population',
                  xaxis=dict(tickangle=-45, type='category'),
                  legend_title='Gender', 
                  title_font_size=16)

fig.write_html("madrid_groups_age.html")
fig.show()
