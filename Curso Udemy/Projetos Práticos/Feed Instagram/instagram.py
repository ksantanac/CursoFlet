# Importe a biblioteca flet com um nome mais curto para facilitar a referência
import flet as ft


# Define a função principal 'main', que recebe uma página como parâmetro
def main(page: ft.Page):
    # Define o alinhamento vertical e horizontal do conteúdo da página para o centro
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Define a cor de fundo da página como preto
    page.bgcolor = ft.colors.BLACK

    # Define a função de callback 'clicked' que será chamada quando um elemento for clicado
    def clicked(e):
        # Alterna o estado selecionado do controle
        e.control.selected = not e.control.selected
        # Se o controle estiver selecionado, imprime "Selecionado"
        if e.control.selected:
            print("Selecionado")
        # Atualiza o controle
        e.control.update()

    # Cria um layout de contêiner com algumas configurações de estilo
    layout = ft.Container(
        bgcolor=ft.colors.WHITE,  # Define a cor de fundo do contêiner como branco
        width=500,  # Define a largura do contêiner como 500
        # height=700,  # Define a altura do contêiner como 700
        border_radius=ft.border_radius.all(10),  # Define o raio da borda do contêiner como 10
        shadow=ft.BoxShadow(blur_radius=50, color=ft.colors.TEAL),  # Adiciona uma sombra ao contêiner
        content=ft.Column(  # Cria uma coluna para organizar o conteúdo verticalmente
            spacing=0,
            controls=[  # Lista de controles dentro da coluna
                ft.ListTile(  # Cria um item de lista
                    title=ft.Text(value="NASA", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD, offset=(-0.17, 0)),
                    # Define o título do item de lista
                    subtitle=ft.Text(value="A lua!", color=ft.colors.BLACK, offset=(-0.17, 0)),
                    # Define o subtítulo do item de lista
                    leading=ft.Image(  # Define uma imagem como elemento de liderança do item de lista
                        src="https://upload.wikimedia.org/wikipedia/commons/e/e5/NASA_logo.svg",  # URL da imagem
                        fit=ft.ImageFit.CONTAIN,  # Define o ajuste da imagem dentro do espaço disponível
                        offset=ft.Offset(x=-0.25, y=-0)
                    ),
                    trailing=ft.Icon(name=ft.icons.MORE_HORIZ, color=ft.colors.BLACK),
                    # Define um ícone à direita do item de lista
                ),

                ft.Image(  # Adiciona uma imagem
                    src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Aldrin_Apollo_11_original.jpg/"
                        "1024px-Aldrin_Apollo_11_original.jpg",  # URL da imagem
                    fit=ft.ImageFit.CONTAIN  # Define o ajuste da imagem dentro do espaço disponível
                ),

                ft.Container(  # Cria um contêiner interno
                    padding=ft.padding.all(15),  # Define o preenchimento interno do contêiner
                    content=ft.Column(  # Cria uma coluna dentro do contêiner interno
                        controls=[  # Lista de controles dentro da coluna interna
                            ft.ResponsiveRow(  # Cria uma linha responsiva para organizar o conteúdo horizontalmente
                                columns=12,  # Define o número de colunas na linha
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                # Alinha os elementos verticalmente ao centro
                                controls=[  # Lista de controles dentro da linha responsiva
                                    ft.IconButton(  # Cria um botão de ícone
                                        col=1,  # Define a posição da coluna do botão de ícone
                                        icon=ft.icons.FAVORITE_BORDER,  # Define o ícone do botão
                                        selected_icon=ft.icons.FAVORITE,  # Define o ícone selecionado do botão
                                        selected=False,  # Define o estado inicial do botão como não selecionado
                                        on_click=clicked,  # Define a função de callback para quando o botão for clicado
                                        icon_color=ft.colors.BLACK,  # Define a cor do ícone
                                        selected_icon_color=ft.colors.RED,
                                        # Define a cor do ícone quando selecionado                                        # offset=ft.Offset(x=-0.2, y=-0)
                                    ),

                                    ft.Icon(  # Adiciona um ícone
                                        col=1,  # Define a posição da coluna do ícone
                                        name=ft.icons.CHAT_OUTLINED,  # Define o nome do ícone
                                        color=ft.colors.BLACK,
                                        # Define a cor do ícone                                        # offset=ft.Offset(x=-0.2, y=-0)
                                    ),
                                    ft.Icon(  # Adiciona um ícone
                                        col=1,  # Define a posição da coluna do ícone
                                        name=ft.icons.SEND,  # Define o nome do ícone
                                        color=ft.colors.BLACK,  # Define a cor do ícone
                                    ),

                                    ft.Container(col=8),  # Adiciona um contêiner vazio ocupando 8 colunas

                                    ft.IconButton(  # Cria um botão de ícone
                                        col=1,  # Define a posição da coluna do botão de ícone
                                        icon=ft.icons.BOOKMARK_BORDER,  # Define o ícone do botão
                                        selected_icon=ft.icons.BOOKMARK_ROUNDED,  # Define o ícone selecionado do botão
                                        selected=False,  # Define o estado inicial do botão como não selecionado
                                        on_click=clicked,  # Define a função de callback para quando o botão for clicado
                                        icon_color=ft.colors.BLACK,  # Define a cor do ícone
                                        selected_icon_color=ft.colors.BLACK,  # Define a cor do ícone quando selecionado
                                    ),
                                ],
                                offset=ft.Offset(x=0, y=-0.2)
                            ),
                            ft.Text(
                                # Usado para fazer personalizações diferentes para partes dos texto
                                spans=[
                                    ft.TextSpan(text="Curtido por ",
                                                style=ft.TextStyle(color=ft.colors.BLACK, size=16)),
                                    ft.TextSpan(text="programadorkaue ",
                                                style=ft.TextStyle(color=ft.colors.BLACK, size=16,
                                                                   weight=ft.FontWeight.BOLD)),
                                    ft.TextSpan(text="e ",
                                                style=ft.TextStyle(color=ft.colors.BLACK, size=16)),
                                    ft.TextSpan(text="2300 outros ",
                                                style=ft.TextStyle(color=ft.colors.BLACK, size=16,
                                                                   weight=ft.FontWeight.BOLD)),
                                ],
                                offset=ft.Offset(x=0, y=-0.8)
                            ),
                            # Texto com mesmo estilo
                            ft.Text(
                                #
                                value="Um pequeno passo para mentira da NASA enganar todos!!! 🚀🌑",
                                color=ft.colors.BLACK,
                                size=16,
                                offset=ft.Offset(x=0, y=-0.42)
                            ),

                            ft.Text(
                                value="HÁ 55 ANOS ATRÁS",
                                color=ft.colors.GREY,
                                size=13,
                                offset=ft.Offset(x=0, y=-1)
                            ),

                            ft.Text(
                                spans=[
                                    ft.TextSpan(text="ksantanac_ ",
                                                style=ft.TextStyle(color=ft.colors.BLACK, size=16,
                                                                   weight=ft.FontWeight.BOLD)),
                                    ft.TextSpan(text="Agora vamos acordar! #TONTOS",
                                                style=ft.TextStyle(color=ft.colors.BLACK, size=16)),
                                ],
                                offset=ft.Offset(x=0, y=-0.77)
                            ),

                            ft.Text(
                                value="Ver todos os 2.567 comentários",
                                color=ft.colors.GREY,
                                size=13,
                                offset=ft.Offset(x=0, y=-1.1)
                            ),

                            ft.TextField(
                                hint_text="Adicione um comentário...",
                                hint_style=ft.TextStyle(color=ft.colors.GREY, size=16),
                                border=ft.InputBorder.UNDERLINE,
                                border_color=ft.colors.GREY,
                                border_width=1,
                                color=ft.colors.BLACK,
                            )

                        ]
                    )
                )
            ]
        )
    )

    # Adiciona o layout à página
    page.add(layout)


# Verifica se o script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função 'main' nela
    ft.app(target=main)
