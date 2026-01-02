import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# -----------------------------
# Load and prepare data
# -----------------------------
df = pd.read_csv("data/final_output.csv")

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# -----------------------------
# Create Dash app
# -----------------------------
app = Dash(__name__)

# -----------------------------
# App Layout
# -----------------------------
app.layout = html.Div(
    className="container",
    children=[
        html.H1(
            "Pink Morsel Sales Visualiser",
            id="app-header",
            className="title"
        ),

        html.P(
            "Use the radio buttons below to filter Pink Morsel sales by region. "
            "The price increase occurred on 15 January 2021.",
            className="subtitle"
        ),

        dcc.RadioItems(
            id="region-picker",
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

# -----------------------------
# Callback
# -----------------------------
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-picker", "value")
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
        title="Pink Morsel Sales Over Time",
        labels={
            "Date": "Date",
            "Sales": "Total Sales ($)"
        }
    )

    return fig

# -----------------------------
# Run app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
