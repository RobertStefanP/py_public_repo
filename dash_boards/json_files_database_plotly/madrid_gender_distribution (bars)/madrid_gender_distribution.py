import sqlite3
import pandas as pd
import plotly.express as px


conn = sqlite3.connect("../database_manager/projects.db")
df = pd.read_sql_query("""
                       SELECT * FROM madrid_gender_distribution WHERE year IS NOT NULL 
                       AND males IS NOT NULL 
                       AND females IS NOT NULL 
                       ORDER BY year""", conn)
conn.close()

# Convert year to string to skip automaticaly years labels
df['year'] = df['year'].astype('str')

# Reshape from wide to long format
df_melted = df.melt(id_vars=['year'], 
                    value_vars=['males', 'females'], 
                    var_name='gender', 
                    value_name='count')

# Create the grouped bar chart
fig = px.bar(df_melted, 
             x='year', 
             y='count', 
             color='gender', 
             barmode='group', 
             title='Madrid Gender Distribution by Year',
             color_discrete_map={'males': '#1f77b4', 'females': '#ff7f0e'},
             labels={'count': 'Population', 'year': 'Year', 'gender': 'Gender'})

fig.update_layout(xaxis_title='Year',
                  yaxis_title='Population',
                  xaxis=dict(tickangle=-45),
                  legend_title='Gender', 
                  title_font_size=16)

fig.update_yaxes(range=[0, 5000000])
fig.write_html("gender_distrbution_madrid.html")
fig.show()
