from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
from csv import reader
from datetime import datetime

app = Dash("SoulFood Visualisation")

app.title = "SoulFood Visualisation"

sales, date, regions = [], [], []
with open("data/cumulative_sales_data.csv", "r", newline="") as data_file:
    CSVReader = reader(data_file)
    for data_line in CSVReader:
        sales.append(float(data_line[0]))
        date.append(datetime(*[int(i) for i in data_line[1].split('-')]))
        regions.append(data_line[2])
        

def region_filter(region: str):
    """
    all | north | south | east | west
    """
    if region == "all":
        return pd.DataFrame({
            "Sales": sales,
            "Date": date
            })
    
    filtered_sales, filtered_date = [], []
    for idx, val in enumerate(regions):
        if val == region:
            filtered_sales.append(sales[idx])
            filtered_date.append(date[idx])
    return pd.DataFrame({
            "Sales": filtered_sales,
            "Date": filtered_date
            })

initial_line_graph = px.line(region_filter("all"), x="Date", y="Sales", title="Pink Morsel Sale Data")

app.layout = html.Div(style={
        "textAlign": "center",
        "fontFamily": "Cursive"
    }, children=[
    html.H1(children="SoulFood pink morsel data visualisation", id="header"),
    html.Div(children="Sales before and Sales after price change"),
    dcc.Graph(
        id="Pink_Morsel_Sales",
        figure=initial_line_graph
    ),
    dcc.RadioItems(["all", "north", "south", "east", "west"], "all", id="GraphInput", inline=True)
])

@callback(
    Output("Pink Morsel Sales", "figure"),
    Input("GraphInput", "value")
)
def update_figure(arg: str):
    return px.line(region_filter(arg), x="Date", y="Sales")

if __name__ == "__main__":
    app.run(debug=True)