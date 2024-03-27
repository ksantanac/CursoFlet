# Importa a biblioteca flet com um alias 'ft'
import flet as ft

# Define a função principal 'main' que recebe um objeto 'page' do tipo ft.Page
def main(page: ft.Page):
    # Define o alinhamento vertical e horizontal do conteúdo da página para o centro
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK  # Define a cor de fundo da página como preto

    # Cria um avatar de círculo com uma imagem de perfil e um ícone de bate-papo dentro dele
    avatar = ft.CircleAvatar(
        col=2,
        foreground_image_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRW4QHBQ1-BIWQT5YaT5fILo9_PVy-TJICgaA&usqp=CAU",
        height=60,
        width=60,
        content=ft.Column(
            controls=[
                ft.Icon(name=ft.icons.CHAT, col=1, color=ft.colors.BLACK),
            ]
        )
    )

    # Define um texto representando o nome de usuário e o identificador
    user = ft.Text(
        spans=[
            ft.TextSpan(text="Valorant ", style=ft.TextStyle(color=ft.colors.BLACK, weight=ft.FontWeight.BOLD)),
            ft.TextSpan(text="@valorant_br", style=ft.TextStyle(color=ft.colors.GREY))
        ],
        size=16,
    )

    # Cria um contêiner de mídia com uma imagem e uma descrição relacionada
    media = ft.Container(
        border_radius=ft.border_radius.all(20),
        border=ft.border.all(width=1, color=ft.colors.GREY_300),
        width=440,
        margin=ft.margin.symmetric(vertical=10),
        content=ft.Column(
            spacing=1,
            controls=[
                ft.Image(
                    src="https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt252b944251ebec12/65fb58c6a93acb3e14313a78/E8A2_Clove_Throwing_Orb_16x9.jpg",
                    fit=ft.ImageFit.COVER,
                    aspect_ratio=1.78,  # 16:9
                ),
                ft.Container(
                    padding=ft.padding.all(20),
                    content=ft.Column(
                        spacing=1,
                        controls=[
                            user,
                            ft.Text(
                                value="Com Clove, é possível desafiar a fronteira final: a morte.",
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS,
                                color=ft.colors.BLACK
                            )
                        ]
                    )
                )
            ]
        )
    )

    # Define uma descrição do personagem
    description = ft.Text(
        value="As habilidades de Clove giram em torno do conceito de uma bela morte: morrer em qualquer rodada pode ser apenas o começo."
              "\n\nAinda que elu seja Controladore, nem pense em ficar de bobeira na retaguarda com Clove. "
              "Para habilitar o kit delu, você terá que correr riscos calculados e mergulhar na batalha. Há uma linha "
              "tênue entre jogar com cautela e arriscar tudo, e Clove precisa equilibrar-se nela.",
        color=ft.colors.BLACK
    )

    # Cria uma linha de ações com ícones
    actions = ft.ResponsiveRow(
        controls=[
            ft.Icon(name=ft.icons.CHAT, col=1, color=ft.colors.BLACK),
            ft.Icon(name=ft.icons.SHARE, col=1, color=ft.colors.BLACK),
            ft.Icon(name=ft.icons.FAVORITE_BORDER, col=1, color=ft.colors.BLACK),
            ft.Icon(name=ft.icons.ANALYTICS, col=1, color=ft.colors.BLACK)
        ],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
    )

    # Define um layout principal da página com todos os elementos anteriores organizados
    layout = ft.Container(
        bgcolor=ft.colors.WHITE,  # Define a cor de fundo do contêiner como branco
        width=600,  # Define a largura do contêiner como 600
        padding=ft.padding.all(20),
        border_radius=ft.border_radius.all(10),  # Define o raio da borda do contêiner como 10
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.LIGHT_BLUE_ACCENT),  # Adiciona uma sombra ao contêiner
        content=ft.ResponsiveRow(
            columns=12,
            controls=[
                avatar,
                ft.Column(
                    col=10,
                    controls=[
                        user,
                        description,
                        media,
                        actions
                    ]
                )
            ]
        )
    )

    # Adiciona o layout à página
    page.add(layout)

# Verifica se este arquivo está sendo executado como um script principal
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
