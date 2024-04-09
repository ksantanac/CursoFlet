# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r Tooltip
# .py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    tp = ft.Tooltip(
        message="Tooltip",
        content=ft.Text(value="Passe o mouse aqui"),
        bgcolor=ft.colors.BLACK,
        border=ft.border.all(width=5, color=ft.colors.WHITE),
        border_radius=ft.border_radius.all(5),
        height=100,
        margin=ft.margin.all(20),
        padding=ft.padding.all(10),
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(color=ft.colors.WHITE, italic=True, size=30),
        wait_duration=1000,
        gradient=ft.LinearGradient(
            begin=ft.alignment.bottom_right,
            end=ft.alignment.top_right,
            colors=[ft.colors.CYAN, ft.colors.TEAL]
        )

    )

    page.add(tp)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
