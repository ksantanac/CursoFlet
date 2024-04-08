# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r SafeArea.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    sa = ft.SafeArea(
        content=ft.Container(bgcolor=ft.colors.AMBER),
        expand=True,
        bottom=True,
        left=True,
        right=True,
        top=True,
        minimum=50,
    )

    page.add(sa)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
