import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK

    # Precisa definir os pixeis de começo e fim, porém pode aplicar gradientes diferentes em partes do texto
    texto = ft.Text(
        text_align=ft.TextAlign.CENTER,
        size=80,
        weight=ft.FontWeight.BOLD,
        spans=[
            ft.TextSpan(
                text='Programador Aventureiro',
                style=ft.TextStyle(
                    foreground=ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            begin=ft.Offset(x=0, y=0),
                            end=ft.Offset(x=600, y=0),
                            colors=[ft.colors.CYAN, ft.colors.PURPLE, ft.colors.PINK],
                            color_stops=[0, 0.8, 1],
                        )
                    ),
                )
            )
        ]
    )

    # Sempre começa no início do texto e termina no final
    texto2 = ft.ShaderMask(
        content=ft.Text(
            value='Shadow Mask', 
            size=170, 
            weight=ft.FontWeight.BOLD, 
            text_align=ft.TextAlign.CENTER,
        ),
        shader=ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=[ft.colors.CYAN, ft.colors.PURPLE, ft.colors.PINK],
            stops=[0, 0.8, 1],
        )
    )

    # Exemplo com diversos gradientes
    texto3 = ft.Text(
        text_align=ft.TextAlign.CENTER,
        size=80,
        weight=ft.FontWeight.BOLD,
        spans=[
            ft.TextSpan(
                text='Programador ',
                style=ft.TextStyle(
                    foreground=ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            begin=ft.Offset(x=0, y=0),
                            end=ft.Offset(x=600, y=0),
                            colors=[ft.colors.RED, ft.colors.DEEP_ORANGE, ft.colors.AMBER],
                            color_stops=[0, 0.5, 1],
                        )
                    ),
                )
            ),

            ft.TextSpan(
                text='Aventureiro',
                style=ft.TextStyle(
                    foreground=ft.Paint(
                        gradient=ft.PaintLinearGradient(
                            begin=ft.Offset(x=0, y=0),
                            end=ft.Offset(x=600, y=0),
                            colors=[ft.colors.TEAL, ft.colors.LIME],
                            color_stops=[0, 1],
                        )
                    ),
                )
            ),

            ft.TextSpan(
                text='\n As melhores aventuras do mundo Tech!',
                style=ft.TextStyle(
                    color=ft.colors.CYAN_100,
                    size=30,
                    shadow=ft.BoxShadow(
                        blur_radius=40,
                        spread_radius=10,
                        blur_style=ft.ShadowBlurStyle.OUTER,
                        color=ft.colors.CYAN
                    ),
                ),
            ),
        ]
    )

    page.add(texto, texto2, texto3)

if __name__ == '__main__':
    ft.app(target=main)