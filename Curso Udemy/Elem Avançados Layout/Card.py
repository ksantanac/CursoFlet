# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r Card.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    card = ft.Card(
        content=ft.Column(
            controls=[
                ft.Text(value="Titulo card", style=ft.TextThemeStyle.HEADLINE_LARGE),
                ft.Text(value="Conteudo card", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                ft.FilledButton(text="Salvar"),
            ]
        ),
        color=ft.colors.GREY_900,
        elevation=5,
        margin=ft.margin.all(30),
        shadow_color=ft.colors.WHITE
    )


    page.add(card)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
