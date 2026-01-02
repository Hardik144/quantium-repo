import pandas as pd
from dash import Dash, html, dcc, Input, Output
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
    className="container",
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            className="title"
        ),

        html.P(
            "Use the radio buttons below to filter Pink Morsel sales by region. "
            "The price increase occurred on 15 January 2021.",
            className="subtitle"
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            className="radio-group"
        ),

        dcc.Graph(id="sales-line-chart")
    ]
)

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        labels={
            "Date": "Date",
            "Sales": "Total Sales ($)"
        },
        title="Pink Morsel Sales Over Time"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
