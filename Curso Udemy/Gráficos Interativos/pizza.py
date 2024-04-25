# Importe a biblioteca flet com o alias ft
import flet as ft


# flet -r pizza.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    page.bgcolor = ft.colors.BLACK

    def on_chart_event(e: ft.PieChartEvent):
        for i, section in enumerate(chart.sections):
            if i == e.section_index:
                section.radius = 110,
                section.title_style = ft.TextStyle(
                    size=16,
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54)
                )
            else:
                section.radius = 100
                section.title_style = ft.TextStyle(
                    size=12,
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                )

        chart.update()

    chart = ft.PieChart(
        expand=True,
        animate=ft.Animation(duration=1000, curve=ft.AnimationCurve.ELASTIC_IN_OUT),
        sections=[
            ft.PieChartSection(
                value=40,
                title="40%",
                title_style=ft.TextStyle(
                    size=30,
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD
                ),
                radius=200,
                title_position= 0.2, # 0.0 -- 1
                color=ft.colors.CYAN,
                border_side=ft.BorderSide(width=5, color=ft.colors.WHITE),
                badge=ft.Container(
                    content=ft.Icon(name=ft.icons.AC_UNIT, color=ft.colors.WHITE),
                    width=50,
                    height=50,
                    border=ft.border.all(width=2, color=ft.colors.WHITE),
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=ft.colors.BLACK
                ),
                badge_position=0.98
            ),

            ft.PieChartSection(
                value=30,
                title="30%",
                title_style=ft.TextStyle(
                    size=30,
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD
                ),
                radius=200,
                title_position=0.2,  # 0.0 -- 1
                color=ft.colors.RED,
                border_side=ft.BorderSide(width=5, color=ft.colors.WHITE),
                badge=ft.Container(
                    content=ft.Icon(name=ft.icons.ACCESS_ALARM, color=ft.colors.WHITE),
                    width=50,
                    height=50,
                    border=ft.border.all(width=2, color=ft.colors.WHITE),
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=ft.colors.BLACK
                ),
                badge_position=0.98
            ),

            ft.PieChartSection(
                value=15,
                title="15%",
                title_style=ft.TextStyle(
                    size=30,
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD
                ),
                radius=200,
                title_position=0.2,  # 0.0 -- 1
                color=ft.colors.PURPLE,
                border_side=ft.BorderSide(width=5, color=ft.colors.WHITE),
                badge=ft.Container(
                    content=ft.Icon(name=ft.icons.APPLE, color=ft.colors.WHITE),
                    width=50,
                    height=50,
                    border=ft.border.all(width=2, color=ft.colors.WHITE),
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=ft.colors.BLACK
                ),
                badge_position=0.5,
            ),

            ft.PieChartSection(
                value=15,
                title="15%",
                title_style=ft.TextStyle(
                    size=30,
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD
                ),
                radius=200,
                title_position=0.2,  # 0.0 -- 1
                color=ft.colors.GREEN,
                border_side=ft.BorderSide(width=5, color=ft.colors.WHITE),
                badge=ft.Container(
                    content=ft.Icon(name=ft.icons.PEDAL_BIKE, color=ft.colors.WHITE),
                    width=50,
                    height=50,
                    border=ft.border.all(width=2, color=ft.colors.WHITE),
                    shape=ft.BoxShape.CIRCLE,
                    bgcolor=ft.colors.BLACK
                ),
                badge_position=0.5,
            ),

        ],
        sections_space=10,
        center_space_radius=100,
        center_space_color=ft.colors.WHITE,
        start_degree_offset=90,
        on_chart_event=on_chart_event

    )

    page.add(chart)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
