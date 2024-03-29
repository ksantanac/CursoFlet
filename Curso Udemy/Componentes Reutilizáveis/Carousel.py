# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r Carousel.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.bgcolor = ft.colors.BLACK

    def expand_img(e):
        for c in carousel.controls:
            c.col = 1

        e.control.col = 12 - len(carousel.controls) + 1
        carousel.update()

    carousel = ft.ResponsiveRow(
        columns=12,
        spacing=5,
        controls=[
            ft.Container(
                col=1,
                image_src=f"https://picsum.photos/250/300?{num}",
                image_fit=ft.ImageFit.COVER,
                border_radius= ft.border_radius.all(5),
                on_click=expand_img
            )
            for num in range(10, 18)

        ]
    )

    carousel.controls[0].col = 12 - len(carousel.controls) + 1


    layout = ft.Container(
        width=700,
        height=300,
        shadow= ft.BoxShadow(blur_radius=500, color=ft.colors.AMBER),
        border_radius= ft.border_radius.all(10),
        bgcolor=ft.colors.GREY_200,

        padding= ft.padding.all(5),
        content=carousel

    )

    page.add(layout)

# Verifique se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abra a página da web e execute a função principal nela
    ft.app(target=main)
