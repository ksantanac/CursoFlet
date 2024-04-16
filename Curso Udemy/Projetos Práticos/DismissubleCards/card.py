# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r card.py

# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    images = [
        "https://a-static.mlcdn.com.br/450x450/poster-cartaz-homem-aranha-sem-volta-para-casa-c-pop-arte-poster/poparteskins2/15938541960/01e21ac5db78cdb615cfec87d0dabfcd.jpeg",
        "https://a-static.mlcdn.com.br/450x450/poster-cartaz-homem-aranha-sem-volta-para-casa-b-pop-arte-poster/poparteskins2/15938541948/2246288f2e70a4d68461f0bb14693b91.jpeg",
        "https://img.elo7.com.br/product/main/3FFB785/poster-homem-aranha-sem-volta-para-casa-adesivo-42-5x60cm-adesivo.jpg",
        "https://m.media-amazon.com/images/I/71f7iZ3F6HL._AC_UF894,1000_QL80_.jpg",
        "https://m.media-amazon.com/images/I/81BP1OHGwkL._AC_UF894,1000_QL80_.jpg",
        "https://a-static.mlcdn.com.br/450x450/poster-cartaz-homem-aranha-spider-man-2-c-pop-arte-poster/poparteskins2/15938524045/2fd03f73140e1d62809ced7a7822769f.jpeg",
        "https://cdn.awsli.com.br/600x700/1610/1610163/produto/177685039/poster-vingadores-era-de-ultron-f-fe1eac82.jpg",
        "https://img.elo7.com.br/product/zoom/23646C7/big-poster-filme-capita-marvel-tamanho-90x60-cm-presente-geek.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUdxRrKYRtuvOnXVr-yxfRTriW_fWMx5eoTtumV94Crg&s",
        "https://i0.wp.com/nerdizmo.uai.com.br/wp-content/uploads/sites/29/2019/08/Todos-os-p%C3%B4steres-de-filmes-da-Marvel-sem-texto-GEEKNESS-1.jpg?fit=683%2C1024",
    ]

    def change_posters():
        for poster in posters.controls:
            poster.content.offset.x += poster.data * 0.2
            poster.content.scale.scale -= poster.data * 0.1
            poster.content.opacity -= poster.data * 0.3

        posters.update()
    def handle_dismiss(e):
        for num, poster in enumerate(posters.controls):

            if e.control == posters.controls[0]:
                posters.controls.clear()
                posters.controls.extend(
                    [
                        ft.Dismissible(
                            content=ft.Container(
                                image_src=img,
                                border_radius=ft.border_radius.all(10),
                                image_fit=ft.ImageFit.COVER,
                                aspect_ratio=9 / 16,
                                offset=ft.Offset(x=0, y=0),
                                scale=ft.Scale(scale=1),
                                opacity=1,
                                shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.BLACK),
                                animate=ft.Animation(duration=300, curve=ft.AnimationCurve.DECELERATE),
                                animate_offset=True,
                                animate_opacity=True,
                                animate_scale=True
                            ),
                            data=pos,
                            on_dismiss=handle_dismiss
                        ) for pos, img in reversed(list(enumerate(images)))
                    ]
                )

            poster.data -= 1
            poster.content.offset.x = 0
            poster.content.opacity = 1
            poster.content.scale.scale = 1

        change_posters()

    posters = ft.Stack(
        height=500,
        controls=[
            ft.Dismissible(
                content=ft.Container(
                    image_src=img,
                    border_radius=ft.border_radius.all(10),
                    image_fit=ft.ImageFit.COVER,
                    aspect_ratio=9/16,
                    offset=ft.Offset(x=0, y=0),
                    scale=ft.Scale(scale=1),
                    opacity=1,
                    shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.BLACK),
                    animate=ft.Animation(duration=300, curve=ft.AnimationCurve.DECELERATE),
                    animate_offset=True,
                    animate_opacity=True,
                    animate_scale=True
                ),
                data=pos,
                on_dismiss=handle_dismiss
            ) for pos, img in reversed(list(enumerate(images)))
        ]
    )

    layout = ft.Row(controls=[posters], alignment=ft.MainAxisAlignment.CENTER)
    page.add(layout)

    change_posters()


# Verifique se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abra a página da web e execute a função principal nela
    ft.app(target=main)
