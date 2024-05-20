import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_dark"

# Load data
df = pd.read_csv("data/SampleSuperstore.csv")

# Clean data and create new feature
df = df.drop("Country", axis=1).drop_duplicates()

df["Postal Code"] = df["Postal Code"].astype(str).str.zfill(5)
df["Discount"] = df["Discount"] * 100

# Mapping full state names to abbreviations
state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Add State Abbreviations to the dataset
df["State Abbrev"] = df["State"].map(state_abbrev)

app = dash.Dash(__name__)
app.title = "Superstore Dashboard"

app.layout = html.Div(
    children=[
        html.H1(children="Superstore Dashboard", className="header-title"),
        html.P(
            children=(
                "Explore detailed insights into sales performance, profitability, and key business metrics"
                " across different categories, regions, and customer segments to drive informed decisions"
                " and strategic growth."
            ),
            className="header-description",
        ),
        # Overview Section
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.H3(
                            id="total-sales",
                            style={"textAlign": "center"},
                        ),
                        html.P("Total Sales"),
                    ],
                    className="card col-md-4",
                ),
                html.Div(
                    children=[
                        html.H3(id="total-profit", style={"textAlign": "center"}),
                        html.P("Total Profit"),
                    ],
                    className="card col-md-4",
                ),
                html.Div(
                    children=[
                        html.H3(id="profit-margin", style={"textAlign": "center"}),
                        html.P("Profit Margin"),
                    ],
                    className="card col-md-4",
                ),
            ],
            className="row",
        ),
        # Category and Sub-Category Profitability
        html.Div(
            children=[
                dcc.Graph(
                    id="category-profit-bar",
                    className="graph",
                ),
                dcc.Graph(id="subcategory-profit-lolipop-bar", className="graph"),
            ],
            className="row",
        ),
        # Discount Analysis and Regional Analysis
        html.Div(
            children=[
                dcc.Graph(
                    id="discount-profit-scatter",
                    className="graph",
                ),
                dcc.Graph(
                    id="region-profit-map",
                    className="graph",
                ),
            ],
            className="row",
        ),
        # Segment and Ship Mode Analysis
        html.Div(
            children=[
                dcc.Graph(
                    id="segment-profit-pie",
                    className="graph",
                ),
                dcc.Graph(
                    id="shipmode-profit-bar",
                    className="graph",
                ),
            ],
            className="row",
        ),
    ],
    className="container-fluid",
)


@app.callback(
    [
        Output("total-sales", "children"),
        Output("total-profit", "children"),
        Output("profit-margin", "children"),
    ],
    [Input("total-sales", "id")],
)
def update_overview(_):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    profit_margin = (total_profit / total_sales) * 100
    return f"${total_sales:,.2f}", f"${total_profit:,.2f}", f"{profit_margin:.2f}%"


@app.callback(
    Output("category-profit-bar", "figure"), [Input("category-profit-bar", "id")]
)
def update_category_profit(_):
    category_profit = df.groupby("Category")["Profit"].mean().reset_index().round(2)
    fig = px.bar(
        category_profit, x="Category", y="Profit", title="Average Profit by Category"
    ).update_layout(title_x=0.5, font_color="grey")
    return fig


@app.callback(
    Output("subcategory-profit-lolipop-bar", "figure"),
    [Input("subcategory-profit-lolipop-bar", "id")],
)
def update_subcategory_profit(_):
    subcategory_profit = (
        df.groupby("Sub-Category")["Profit"].mean().reset_index().round(2)
    )

    # Create the lollipop chart
    fig = px.scatter(
        subcategory_profit,
        x="Profit",
        y="Sub-Category",
        # text="Profit",
        color="Profit",
        color_continuous_scale="RdYlGn",
    )

    # Customize the trace appearance
    fig.update_traces(mode="markers+text", marker=dict(size=10))

    # Customize the layout
    fig.update_layout(
        title="Average Profit by Sub-Category",
        xaxis_title="Profit",
        yaxis_title="Sub-Category",
        showlegend=False,
        hovermode="closest",
        xaxis_range=[-100, 900],
        title_x=0.5,
        font_color="grey",
    )

    # Add horizontal lines
    for y_val, mean_val in zip(
        subcategory_profit["Sub-Category"], subcategory_profit["Profit"]
    ):
        fig.add_shape(
            type="line",
            x0=0,
            y0=y_val,
            x1=mean_val,
            y1=y_val,
            line=dict(color="white", width=2),
        )

    return fig


@app.callback(
    Output("discount-profit-scatter", "figure"),
    [Input("discount-profit-scatter", "id")],
)
def update_discount_profit(_):
    fig = px.scatter(
        df, x="Discount", y="Profit", trendline="ols", title="Discount vs Profit"
    ).update_layout(title_x=0.5, font_color="grey", xaxis_title="Discount (%)")
    return fig


@app.callback(Output("region-profit-map", "figure"), [Input("region-profit-map", "id")])
def update_region_profit(_):
    # Calculate total and average profit by State Abbrev
    state_profit = df.groupby("State Abbrev")["Profit"].mean().reset_index().round(2)
    fig = px.choropleth(
        state_profit,
        locations="State Abbrev",
        locationmode="USA-states",
        color="Profit",
        scope="usa",
        title="Average Profit by State",
    ).update_layout(
        title_x=0.5,
        font_color="grey",
    )
    return fig


@app.callback(
    Output("segment-profit-pie", "figure"), [Input("segment-profit-pie", "id")]
)
def update_segment_profit(_):
    segment_profit = df.groupby("Segment")["Profit"].sum().reset_index().round(2)
    fig = px.pie(
        segment_profit,
        names="Segment",
        values="Profit",
        title="Total Profit by Customer Segment",
    ).update_layout(title_x=0.5, font_color="grey")
    return fig


@app.callback(
    Output("shipmode-profit-bar", "figure"), [Input("shipmode-profit-bar", "id")]
)
def update_shipmode_profit(_):
    shipmode_profit = df.groupby("Ship Mode")["Profit"].mean().reset_index().round(2)
    fig = px.bar(
        shipmode_profit,
        x="Ship Mode",
        y="Profit",
        title="Average Profit by Shipping Mode",
    ).update_layout(title_x=0.5, font_color="grey")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
