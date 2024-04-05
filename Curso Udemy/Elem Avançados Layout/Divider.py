# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r Divider.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    page.add(
        ft.Column(
            spacing=0,
            expand=True,
            controls=[
                ft.Container(
                    bgcolor=ft.colors.AMBER,
                    expand=True,
                ),

                ft.Divider(),

                ft.Container(
                    bgcolor=ft.colors.BLUE,
                    expand=True,
                ),

                ft.Divider(
                    height=5,
                    color=ft.colors.WHITE,

                ),

                ft.Container(
                    bgcolor=ft.colors.DEEP_PURPLE,
                    expand=True,
                ),

                ft.Divider(
                    height=50,
                    thickness=10,
                    color=ft.colors.INDIGO
                ),

                ft.Container(
                    bgcolor=ft.colors.DEEP_PURPLE,
                    expand=True,
                )
            ]
        )
    )

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
