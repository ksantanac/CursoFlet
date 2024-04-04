# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r Stack.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    st = ft.Stack(
        controls=[
            # ft.Image(src="https://hackersec.com/wp-content/uploads/2020/11/port-scan-python-hackersec-min.png")
            ft.Container(
                image_src="https://hackersec.com/wp-content/uploads/2020/11/port-scan-python-hackersec-min.png",
                image_fit=ft.ImageFit.COVER,
            ),

            ft.Container(
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[ft.colors.TEAL, ft.colors.CYAN]
                ),
                opacity=0.5,
            ),

            ft.Text(
                value="Texto Sobreposto",
                style=ft.TextThemeStyle.HEADLINE_LARGE
            ),

            ft.Column(
                top=200,
                left=0,
                right=0,
                # bottom=0,
                controls=[
                    ft.Text(value="Curso de Flet", style=ft.TextThemeStyle.HEADLINE_LARGE),
                    ft.Text(value="Aprenda e desenvolva seus próprios apps com python", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                    ft.FilledButton(text="Saiba Mais")
                ]
            )
        ],
        # expand=True,
        aspect_ratio=0.6,
    )

    page.add(st)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
