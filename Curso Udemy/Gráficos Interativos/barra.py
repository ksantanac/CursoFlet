# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r barra.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):
    # page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = ft.padding.all(80)

    def chart_events(e: ft.BarChartEvent):
        chart.bar_groups[e.group_index].bar_space = 20
        chart.bar_groups[e.group_index].bar_rods[e.rod_index].color = ft.colors.PURPLE

        if chart.bar_groups[e.group_index].bar_rods[e.rod_index].gradient:
            chart.bar_groups[e.group_index].bar_rods[e.rod_index].to_y += 20
        chart.update()

    chart = ft.BarChart(
        expand=True,
        animate=ft.Animation(duration=1000, curve=ft.AnimationCurve.ELASTIC_IN_OUT),
        bar_groups=[
            ft.BarChartGroup(
                x=0,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=80,
                        width=40,
                        color=ft.colors.PINK,
                        tooltip="Teste",
                        border_radius=0,
                        show_tooltip=True,
                    ),

                    ft.BarChartRod(
                        from_y=0,
                        to_y=40,
                        width=40,
                        color=ft.colors.GREEN,
                        tooltip="Verde",
                        border_radius=0,
                        border_side=ft.BorderSide(width=2, color=ft.colors.WHITE)
                    )
                ],

                bars_space=5,
                group_vertically=False,
            ),

            ft.BarChartGroup(
                x=1,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=100,
                        width=40,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.center_left,
                            end=ft.alignment.center_right,
                            colors=[ft.colors.DEEP_ORANGE, ft.colors.AMBER]
                        ),
                        tooltip="Orange",
                        border_radius=ft.border_radius.vertical(top=10),
                        border_side=ft.BorderSide(width=2, color=ft.colors.WHITE)
                    )
                ]
            ),

            ft.BarChartGroup(
                x=2,
                bar_rods=[
                    ft.BarChartRod(
                        from_y=0,
                        to_y=30,
                        width=40,
                        color=ft.colors.RED,
                        border_radius=0,
                        bg_color=ft.colors.GREY_300,
                        bg_from_y=0,
                        bg_to_y=100,
                    )
                ],
            ),

            ft.BarChartGroup(
                x=3,
                bar_rods=[
                    ft.BarChartRod(
                        rod_stack_items=[
                            ft.BarChartRodStackItem(
                                from_y=10,
                                to_y=30,
                                color=ft.colors.YELLOW
                            ),

                            ft.BarChartRodStackItem(
                                from_y=0,
                                to_y=10,
                                color=ft.colors.CYAN,
                                border_side=ft.BorderSide(width=5, color=ft.colors.BLUE)
                            ),
                        ],
                        from_y=0,
                        to_y=60,
                        width=40,
                        color=ft.colors.ORANGE,
                        border_radius=0,
                        tooltip="Laranja"
                    )
                ]
            )
        ],
        border=ft.border.all(width=5, color=ft.colors.GREY_400),
        interactive=True,
        tooltip_bgcolor=ft.colors.WHITE,
        horizontal_grid_lines=ft.ChartGridLines(
            interval=20,
            color=ft.colors.WHITE12,
            width=3,
            # dash_pattern=[3, 20] # 3 parte pintada e 20 branco
        ),
        vertical_grid_lines=ft.ChartGridLines(
            interval=0.1,
            color=ft.colors.WHITE12,
            width=1
        ),
        left_axis=ft.ChartAxis(
            labels_size=40,
            show_labels=True,
            labels_interval=10,
            title=ft.Text(value="Preço das frutas (R$)"),
            title_size=100
        ),
        top_axis=ft.ChartAxis(
            show_labels=False,
            title=ft.Text(value="Preço médio das frutas em SP", size=30),
            title_size=100
        ),
        right_axis=ft.ChartAxis(show_labels=False),
        bottom_axis=ft.ChartAxis(
            labels=[
                ft.ChartAxisLabel(
                    value=0,
                    label=ft.Container(ft.Text("Maça"), padding=10),
                ),
                ft.ChartAxisLabel(
                    value=1,
                    label=ft.Container(ft.Text("Jabuticaba"), padding=10),
                ),
                ft.ChartAxisLabel(
                    value=2,
                    label=ft.Container(ft.Text("Morango"), padding=10),
                ),
                ft.ChartAxisLabel(
                    value=3,
                    label=ft.Container(ft.Text("Laranja"), padding=10),
                ),
            ],
            labels_size=40
        ),
        min_y=0,
        max_y=120,
        on_chart_event=chart_events
    )

    
    page.add(chart)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
