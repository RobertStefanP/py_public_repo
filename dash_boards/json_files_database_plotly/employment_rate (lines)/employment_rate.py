import sqlite3
import pandas as pd
import plotly.express as px


conn = sqlite3.connect("../db_manager/projects.db")

df = pd.read_sql_query("SELECT * FROM employment_rate ORDER BY year", conn) 
conn.close()

fig = px.line(df, x="year", y="rate", title="Employment rate on Spain during the last years.", markers=True)
fig.update_xaxes(tickmode="linear")
fig.update_layout(xaxis=dict(dtick=1))

fig.write_html("employment_rate.html")
fig.show()
