import flet as ft  # Importa a biblioteca flet com o alias ft

# flet -r ShaderMask.py

# Função principal que será executada no aplicativo
def main(page: ft.Page):

    page.padding = 50

    sm = ft.ShaderMask(
        content=ft.Text(value="Programador Kaue", size=30),
        shader=ft.LinearGradient(
            stops=[0, 0.5, 1],
            colors=[ft.colors.DEEP_PURPLE, ft.colors.PINK, ft.colors.CYAN],
        )
    )

    sm2 = ft.ShaderMask(
        content=ft.Image(src="https://svg.io/images/example-10.svg"),
        shader=ft.LinearGradient(
            colors=[ft.colors.PINK, ft.colors.DEEP_PURPLE],
        ),
        # https://api.flutter.dev/flutter/dart-ui/BlendMode.html
        blend_mode=ft.BlendMode.SRC_IN
    )



    page.add(sm, sm2)


# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
