import plotly.express as px
# Melt data for Plotly
df_melt = df_country.reset_index().melt(id_vars="index", var_name="Country", value_name="Cases")
fig = px.line(df_melt, x="index", y="Cases", color="Country", 
              title="COVID-19 Cases by Country", log_y=True)
fig.write_html("interactive_plot.html")  
