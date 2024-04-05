# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r VerticalDivider.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    page.add(
        ft.Row(
            expand=True,
            spacing=0,
            controls=[
                ft.Container(
                    bgcolor=ft.colors.AMBER,
                    expand=True,
                ),

                ft.VerticalDivider(),

                ft.Container(
                    bgcolor=ft.colors.PINK,
                    expand=True,
                ),

                ft.VerticalDivider(
                    width=1,
                    color=ft.colors.WHITE,
                ),

                ft.Container(
                    bgcolor=ft.colors.BLUE,
                    expand=True,
                ),

                ft.VerticalDivider(
                    width=50,
                    thickness=10,
                ),

                ft.Container(
                    bgcolor=ft.colors.DEEP_PURPLE,
                    expand=True,
                ),
            ]
        )
    )

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
