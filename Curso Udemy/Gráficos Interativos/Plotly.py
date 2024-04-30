import plotly.graph_objects as go

import flet as ft
from flet.plotly_chart import PlotlyChart
import plotly.express as px

def main(page: ft.Page):

    labels = ["Oxigênio", "Hidrogênio", "Dióxido de Carbono", "Nitrogênio"]
    values = [4500, 2500, 1053, 500]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    chart = PlotlyChart(
        figure=fig,
        isolated=True,
        original_size=True,
    )

    page.add(chart)
    # https://plotly.com/python/

    df = px.data.tips()
    fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug",
                   hover_data=df.columns)

    chart2 = PlotlyChart(
        figure=fig,
        isolated=True,
    )

    page.add(chart2)

if __name__ == '__main__':
    ft.app(target=main)