from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from csv import reader
from datetime import datetime

app = Dash("SoulFood Visualisation", external_stylesheets=[dbc.themes.CYBORG])

app.title = "SoulFood Visualisation"

sales, date, region = [], [], []
with open("data/cumulative_sales_data.csv", "r", newline="") as data_file:
    CSVReader = reader(data_file)
    for data_line in CSVReader:
        sales.append(float(data_line[0]))
        date.append(datetime(*[int(i) for i in data_line[1].split('-')]))
        region.append(data_line[2])
        

data = pd.DataFrame({
    "Sales": sales,
    "Date": date
})


line_graph = px.line(data, x="Date", y="Sales")


app.layout = html.Div(children=[
    html.H1(children="SoulFood pink morsel data visualisation"),
    html.Div(children="Sales before and Sales after price change"),
    dcc.Graph(
        id="Pink Morsel Sales",
        figure=line_graph
    )
])



if __name__ == "__main__":
    app.run(debug=True)