import plotly.graph_objects as go
import flet as ft
from flet.plotly_chart import PlotlyChart
import plotly.express as px

# flet -r Plotly.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    labels = ["Oxigênio", "Hidrogênio", "Dióxido de Carbono", "Nitrogênio"]
    values = [4500, 2500, 1053, 500]

    fig = go.Figure(data=[go.Pie(labels= labels, values=values)])

    chart = PlotlyChart(
        figure=fig,
        isolated=True,
        original_size=True

    )

    page.add(chart)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
