# Importe a biblioteca flet com o alias ft
import matplotlib
import matplotlib.pyplot as plt
import flet as ft
from flet.matplotlib_chart import MatplotlibChart

matplotlib.use("svg")

# flet -r MatplotLib.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    fig, ax = plt.subplots()

    fruits = ["Maça", "Mirtilo", "Cereja", "Laranja"]
    counts = [40, 100, 30, 55]
    bar_labels = ["Vermelho", "Azul", "Vermelho", "Laranja"]
    bar_colors = ["tab:red", "tab:blue", "tab:red", "tab:orange",]

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel("Suprimento de Frutas")
    ax.set_title("Fornecimento de frutas por tipo e cor")
    ax.legend(title="Cor da Fruta")

    chart = MatplotlibChart(
        figure=fig,
        isolated=True,
        original_size=False,
        transparent=True,
    )

    page.add(chart)

    import time

    time.sleep(3)
    ax.legend(title="Cores")

    page.update()
    # chart.update()
    print("UPDATE")

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
