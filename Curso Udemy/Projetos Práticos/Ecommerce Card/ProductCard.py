# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r ProductCard.py

# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    page.bgcolor = ft.colors.BLACK
    page.scroll= ft.ScrollMode.AUTO

    def change_main_image(e):
        for elem in options.controls:
            if elem == e.control:
                elem.opacity = 1
                main_image.src = elem.image_src
            else:
                elem.opacity = 0.5

        main_image.update()
        options.update()

    product_images = ft.Container(
        col={"xs": 12, "md": 6},
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(9),
        aspect_ratio=9/16,                 #Largura seja a metada da altura
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := ft.Image(
                    src="https://images.kabum.com.br/produtos/fotos/486306/iphone-15-apple-pro-max-256gb-titanio-"
                        "preto-tela-de-6-7-camera-dupla-de-48mp-ios-mu773be-a_1699651983_gg.jpg",
                ),

                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src="https://images.kabum.com.br/produtos/fotos/486306/iphone-15-apple-pro-max-256gb-titanio-"
                        "preto-tela-de-6-7-camera-dupla-de-48mp-ios-mu773be-a_1699651983_gg.jpg",
                            width=75,
                            height=75,
                            opacity=1,
                            on_click=change_main_image
                        ),

                        ft.Container(
                            image_src="https://images.kabum.com.br/produtos/fotos/486306/iphone-15-apple-pro-max-"
                                      "256gb-titanio-preto-tela-de-6-7-camera-dupla-de-48mp-ios-mu773be-a_1699651984_gg.jpg",
                            width=75,
                            height=75,
                            opacity=0.5,
                            on_click=change_main_image
                        ),

                        ft.Container(
                            image_src="https://images.kabum.com.br/produtos/fotos/486306/iphone-15-apple-pro-"
                                      "max-256gb-titanio-preto-tela-de-6-7-camera-dupla-de-48mp-ios-mu773be-"
                                      "a_1699651985_gg.jpg",
                            width=75,
                            height=75,
                            opacity=0.5,
                            on_click=change_main_image
                        ),

                        ft.Container(
                            image_src="https://images.kabum.com.br/produtos/fotos/486306/iphone-15-apple-pro-max-"
                                      "256gb-titanio-preto-tela-de-6-7-camera-dupla-de-48mp-ios-mu773be"
                                      "-a_1699651986_gg.jpg",
                            width=75,
                            height=75,
                            opacity=0.5,
                            on_click=change_main_image
                        ),
                    ]
                )

            ]
        )
    )


    product_details = ft.Container(
        col={"xs": 12, "md": 6},
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/16,

        content=ft.Column(
            controls=[
                ft.Text(
                    value="Smartphone",
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD
                ),

                ft.Text(
                    value="iPhone 15 Apple Pro Max 256GB Titânio Preto, Tela de 6.7, Câmera Dupla de 48MP, iOS - "
                          "MU773BE/A",
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=23
                ),

                ft.Text(
                    value="Iphone",
                    color=ft.colors.GREY,
                    italic=True
                ),

                ft.ResponsiveRow(
                    columns=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(
                            col={"xs": 12, "sm": 6},
                            value="R$ 8.299,99",
                            color=ft.colors.WHITE,
                            size=30
                        ),
                        ft.Row(
                            col={"xs": 12, "sm": 6},
                            spacing=5,
                            wrap=False,
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.YELLOW if star < 4 else ft.colors.WHITE
                                ) for star in range(5)
                            ]
                        )
                    ]
                ),

                ft.Tabs(
                    selected_index=0,
                    height=480,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text="Descrição",
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value="IPhone 15 Pro Max Apple 256 GB Titânio Preto\n\n"
                                          "Forjado em Titânio\n"
                                          "O iPhone 15 Pro Max tem design robusto e leve em titânio aeroespacial. "
                                          "Na parte de trás, vidro matte texturizado e, na frente, Ceramic Shield mais "
                                          "resistente que qualquer vidro de smartphone. Ele também é durão contra "
                                          "respingos, água e poeira.\n\n"
                                          "Tela Avançada\n"
                                          "A tela Super Retina XDR de 6,7 pol. com ProMotion aumenta as taxas de "
                                          "atualização para 120 Hz quando você precisa de gráficos mais impressionantes."
                                          " A Dynamic Island mostra alertas e Atividades ao Vivo. Além disso, com a tela"
                                          " Sempre Ativa, você nem precisa tocar na Tela Bloqueada para ficar de olho em"
                                          " tudo.\n\n"
                                          "Chip A17 Pro Revolucionário\n"
                                          "Com GPU de categoria Pro, os games para celular ficam mais imersivos, "
                                          "com ambientes detalhados e personagens muito realistas. O chip A17 Pro é "
                                          "incrivelmente eficiente e ajuda a garantir bateria para o dia todo.\n\n"
                                          "Sistema de Câmera Pro Poderoso\n"
                                          "Aumente suas possibilidades de enquadramento com sete lentes Pro. Fotografe"
                                          " em altíssima resolução e tenha mais cores e detalhes com a câmera "
                                          "grande-angular de 48 MP. Os closes vão ficar mais nítidos a uma distância "
                                          "ainda maior com a câmera teleobjetiva de 5x no iPhone 15 Pro Max.",

                                    color=ft.colors.GREY,
                                    # size=12
                                )
                            )
                        ),
                        ft.Tab(
                            text="Detalhes",
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value="Informações Técnicas\n\n"
                                          "Características:\n"
                                          "- Marca: Apple\n"
                                          "- Modelo: iPhone 15 Pro Max\n\n"
                                          "Principal:\n"
                                          "- Memória Interna: 256GB\n"
                                          "- Processador: A17 Pro\n"
                                          "- Sistema Operacional: iOS 17\n"
                                          "- Cor: Titanium Preto\n\n"
                                          "Chip:\n"
                                          "- A17 Pro\n"
                                          "- Nova CPU de 6 núcleos (2 de desempenho e 4 de eficiência)\n"
                                          "- Nova GPU de 6 núcleos\n"
                                          "- Novo Neural Engine de 16 núcleos\n\n"
                                          "Tela:\n"
                                          "- Super Retina XDR\n"
                                          "- OLED sem bordas de 6,7 polegadas (na diagonal)\n"
                                          "- Resolução de 2796 x 1290 pixels a 460 ppp\n",

                                    color=ft.colors.GREY,
                                    # size=12
                                )
                            )
                        ),
                    ]
                ),

                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6,
                            height=30,
                            label="Cor",
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text="Titânio"),
                                ft.dropdown.Option(text="Preto"),
                                ft.dropdown.Option(text="Branco"),
                            ]
                        ),

                        ft.Dropdown(
                            col=6,
                            height=30,
                            label="Quantidade",
                            label_style=ft.TextStyle(color=ft.colors.WHITE, size=16),
                            border_color=ft.colors.GREY,
                            border_width=0.5,
                            options=[
                                ft.dropdown.Option(text=f"{num}") for num in range(1, 21)
                            ]
                        )
                    ]
                ),

                ft.Container(expand=True),


                ft.ElevatedButton(
                    width=900,
                    text="Adicionar a lista de desejos",
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.WHITE)
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: ft.colors.WHITE
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.WHITE,
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,

                        }
                    )
                ),

                ft.ElevatedButton(
                    width=900,
                    text="Adicionar ao carrinho",
                    style=ft.ButtonStyle(
                        padding=ft.padding.all(20),
                        side={
                            ft.MaterialState.DEFAULT: ft.BorderSide(width=2, color=ft.colors.AMBER)
                        },
                        bgcolor={
                            ft.MaterialState.HOVERED: ft.colors.AMBER
                        },
                        color={
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                        }
                    )
                )

            ]
        )


    )

    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),

        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                product_images,
                product_details,
            ]
        )
    )

    page.add(layout)



# Verifique se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abra a página da web e execute a função principal nela
    ft.app(target=main)
