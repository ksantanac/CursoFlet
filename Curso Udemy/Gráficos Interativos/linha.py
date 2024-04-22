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
                            dash_pattern=[50, 10, 10]
                        )
                    ),
                    ft.LineChartDataPoint(x=5, y=1),
                    ft.LineChartDataPoint(x=6, y=2),
                    ft.LineChartDataPoint(x=7, y=5),
                    ft.LineChartDataPoint(x=8, y=3),
                ],
                curved=True,
                color= ft.colors.BLACK,
                gradient=ft.LinearGradient(
                    begin=ft.alignment.center_left,
                    end=ft.alignment.center_right,
                    colors=[ft.colors.DEEP_ORANGE, ft.colors.AMBER]
                ),
                stroke_width=5,
                stroke_cap_round=True,
                # dash_pattern=[5, 50, 10, 20]
                # above_line_bgcolor= ft.colors.AMBER_100,
                # above_line_gradient=ft.LinearGradient(
                #     begin=ft.alignment.center_left,
                #     end=ft.alignment.center_right,
                #     colors=[ft.colors.DEEP_ORANGE_100, ft.colors.AMBER_100]
                # ),
                # below_line_bgcolor=ft.colors.LIME_100,
                # below_line_gradient=ft.LinearGradient(
                #     begin=ft.alignment.top_center,
                #     end=ft.alignment.bottom_center,
                #     colors=[ft.colors.DEEP_ORANGE, ft.colors.with_opacity(0, ft.colors.LIME_100)]
                # ),
                # above_line_cutoff_y= 3,
                # below_line_cutoff_y=2,
                point=ft.ChartCrossPoint(
                    color=ft.colors.AMBER,
                    size=20,
                    width=10
                ),
                selected_point=ft.ChartCrossPoint(
                    color=ft.colors.RED,
                    size=20,
                    width=10
                ),
                above_line=ft.ChartPointLine(color=ft.colors.BLACK, width=3),
                below_line=ft.ChartPointLine(color=ft.colors.BLACK, width=3),
                selected_below_line=ft.ChartPointLine(color=ft.colors.WHITE, width=3)

            )
        ],

        interactive=True,

        bgcolor=ft.colors.GREY_200,

        tooltip_bgcolor=ft.colors.BLACK,

        horizontal_grid_lines=ft.ChartGridLines(
            interval=1,
            color=ft.colors.BLACK,
            width=1,
            dash_pattern=[10,10]
        ),

        vertical_grid_lines=ft.ChartGridLines(
            interval=1,
            color=ft.colors.BLACK,
            width=1,
            dash_pattern=[10, 10]
        ),

        left_axis=ft.ChartAxis(
            title=ft.Text(value="Eixo Y"),
            title_size=100,
            show_labels=True,
            labels=[
                ft.ChartAxisLabel(value=1, label=ft.Text(value="R$ 1")),
                ft.ChartAxisLabel(value=2, label=ft.Text(value="R$ 2")),
                ft.ChartAxisLabel(value=3, label=ft.Text(value="R$ 3")),
                ft.ChartAxisLabel(value=4, label=ft.Text(value="R$ 4")),
                ft.ChartAxisLabel(value=5, label=ft.Text(value="R$ 5"))
            ],
            labels_interval=1,
            labels_size=50,

        ),

        bottom_axis=ft.ChartAxis(
            title=ft.Text(value="Eixo X"),
            title_size=50,
            show_labels=True,
            labels=[
                ft.ChartAxisLabel(value=1, label=ft.Text(value="Jan")),
                ft.ChartAxisLabel(value=2, label=ft.Text(value="Fev")),
                ft.ChartAxisLabel(value=3, label=ft.Text(value="Mar")),
                ft.ChartAxisLabel(value=4, label=ft.Text(value="Abr")),
                ft.ChartAxisLabel(value=5, label=ft.Text(value="Maio")),
                ft.ChartAxisLabel(value=6, label=ft.Text(value="Jun")),
                ft.ChartAxisLabel(value=7, label=ft.Text(value="Jul")),
                ft.ChartAxisLabel(value=8, label=ft.Text(value="Ago")),
            ],
            labels_interval=1,
            labels_size=50,
        ),
        # right_axis=ft.ChartAxis(),
        # top_axis=ft.ChartAxis(),
        # min_x=3,
        # max_x=5,
        # min_y=2,
        # max_y=5
    )

    page.add(chart)

    import random

    data = [
        ft.LineChartData(
            data_points=[ft.LineChartDataPoint(x=x, y=random.randint(0, 5)) for x in range(10)],
            curved= True
        ),
        ft.LineChartData(
            data_points=[ft.LineChartDataPoint(x=x, y=random.randint(0, 5)) for x in range(10)],
            color=ft.colors.AMBER,
            stroke_width=5
        ),
        ft.LineChartData(
            data_points=[ft.LineChartDataPoint(x=x, y=random.randint(0, 5)) for x in range(10)],
            curved=True,
            color=ft.colors.BLACK,
        ),
    ]

    page.add(
        ft.LineChart(data_series=data)
    )


# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
