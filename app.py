import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

df = pd.read_csv("data/final_output.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

fig = px.line(
    df,
    x="Date",
    y="Sales",
    color="Region",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Total Sales ($)"
    }
)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            style={"textAlign": "center"}
        ),

        html.P(
            "This chart shows Pink Morsel sales over time. "
            "The price increase occurred on 15 January 2021.",
            style={"textAlign": "center"}
        ),

        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
