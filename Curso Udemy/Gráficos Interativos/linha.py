# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r linha.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = ft.padding.all(80)

    chart = ft.LineChart(
        data_series=[
            ft.LineChartData(
                data_points=[
                    ft.LineChartDataPoint(x=1, y=1),
                    ft.LineChartDataPoint(
                        x=3,
                        y=2,
                        show_tooltip=True,
                        tooltip="O valor é 2",
                        tooltip_align=ft.TextAlign.CENTER,
                        tooltip_style=ft.TextStyle(italic=True, color=ft.colors.WHITE),
                        point=ft.ChartCirclePoint(
                            color=ft.colors.AMBER,
                            radius=20,
                            stroke_width=5
                        ),
                        # point=ft.ChartSquarePoint(
                        #     color=ft.colors.AMBER,
                        #     size=20,
                        # )
                        # point=ft.ChartCrossPoint(
                        #     color=ft.colors.AMBER,
                        #     size=20,
                        #     width=10,
                        # ),
                        selected_point=ft.ChartCrossPoint(
                            color=ft.colors.RED,
                            size=20,
                            width=10
                        ),
                        selected_below_line=ft.ChartPointLine(
                            color=ft.colors.GREEN,
                            width=1,
                            dash_pattern=[50, 10]

                        )
                    ),
                ]
            )
        ]
    )

    page.add(chart)



# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
