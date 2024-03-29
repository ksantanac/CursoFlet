# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r cofcard.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    # Configurações de alinhamento vertical e horizontal da página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Define a largura mínima da janela
    page.window_min_width = 500

    # Cor de fundo da página
    page.bgcolor = ft.colors.BLACK

    # Contêiner para a imagem do bárbaro
    image = ft.Container(
        expand=2,  # Expande o contêiner verticalmente
        clip_behavior=ft.ClipBehavior.NONE,  # Remove a máscara de recorte para permitir gradientes
        border_radius=ft.border_radius.vertical(top=10),  # Raio da borda superior do contêiner
        gradient=ft.LinearGradient(  # Gradiente de cores para o contêiner
            begin=ft.alignment.bottom_left,
            end=ft.alignment.top_right,
            colors=[ft.colors.BROWN, ft.colors.SURFACE]  # Cores do gradiente
        ),
        content=ft.Image(  # Imagem do bárbaro
            src="https://static.wikia.nocookie.net/clashofclans/images/9/9b/Barbarian-xx.png/revision/latest?cb=20170703143506",  # URL da imagem
            scale=ft.Scale(scale=1.7)  # Escala da imagem
        )
    )

    # Contêiner para as informações do bárbaro
    info = ft.Container(
        expand=2,  # Expande o contêiner verticalmente
        padding=ft.padding.all(30),  # Preenchimento interno do contêiner
        alignment=ft.alignment.center,  # Alinhamento do conteúdo ao centro
        content=ft.Column(  # Coluna para organizar o conteúdo verticalmente
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Alinhamento horizontal ao centro
            controls=[
                ft.Text(value="LEVEL 4", color=ft.colors.ORANGE),  # Texto indicando o nível do bárbaro
                ft.Text(value="Bárbaro", weight=ft.FontWeight.BOLD, size=40, color=ft.colors.BLACK),  # Texto indicando o nome do bárbaro
                ft.Text(  # Descrição do bárbaro
                    value="A aparência do Bárbaro é a de um homem com uma expressão irritada pronto para lutas, cabelos "
                          "loiros cortados de forma curta e um longo bigode amarelo. Ele usa um kilt marrom com um "
                          "cinto de couro e uma fivela em forma de escudo de aço, o que indica que ele pode ser um"
                          " guerreiro escocês.",
                    color=ft.colors.GREY,
                    text_align=ft.TextAlign.CENTER,
                )
            ]

        )
    )

    # Contêiner para as habilidades do bárbaro
    skills = ft.Container(
        expand=1,  # Expande o contêiner horizontalmente
        bgcolor=ft.colors.ORANGE,  # Cor de fundo do contêiner
        padding=ft.padding.symmetric(horizontal=20),  # Preenchimento interno do contêiner
        border_radius=ft.border_radius.vertical(bottom=20),  # Raio da borda inferior do contêiner
        content=ft.Row(  # Linha para organizar o conteúdo horizontalmente
            controls=[
                # Coluna para a primeira habilidade (defesa)
                ft.Column(
                    expand=1,  # Expande a coluna verticalmente
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Alinhamento horizontal ao centro
                    alignment=ft.MainAxisAlignment.CENTER,  # Alinhamento vertical ao centro
                    controls=[
                        ft.Text(  # Valor da primeira habilidade
                            value="20",
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40
                        ),
                        ft.Text(  # Descrição da primeira habilidade
                            value="Defesa",
                            color=ft.colors.WHITE,
                        )
                    ]
                ),

                ft.VerticalDivider(opacity=0.5),  # Divisor vertical com opacidade

                # Coluna para a segunda habilidade (velocidade)
                ft.Column(
                    expand=1,  # Expande a coluna verticalmente
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Alinhamento horizontal ao centro
                    alignment=ft.MainAxisAlignment.CENTER,  # Alinhamento vertical ao centro
                    controls=[
                        ft.Text(  # Valor da segunda habilidade
                            value="16",
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40
                        ),
                        ft.Text(  # Descrição da segunda habilidade
                            value="Velocidade",
                            color=ft.colors.WHITE,
                        )
                    ]
                ),

                ft.VerticalDivider(opacity=0.5),  # Divisor vertical com opacidade

                # Coluna para a terceira habilidade (dano)
                ft.Column(
                    expand=1,  # Expande a coluna verticalmente
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Alinhamento horizontal ao centro
                    alignment=ft.MainAxisAlignment.CENTER,  # Alinhamento vertical ao centro
                    controls=[
                        ft.Text(  # Valor da terceira habilidade
                            value="150",
                            color=ft.colors.WHITE,
                            weight=ft.FontWeight.BOLD,
                            size=40
                        ),
                        ft.Text(  # Descrição da terceira habilidade
                            value="Dano",
                            color=ft.colors.WHITE,
                        )
                    ]
                )
            ]
        )
    )

    # Layout principal que contém os contêineres de imagem, informações e habilidades
    layout = ft.Container(
        height=700,  # Altura do layout
        width=400,  # Largura do layout
        shadow=ft.BoxShadow(blur_radius=100, color=ft.colors.BROWN),  # Sombra do layout
        clip_behavior=ft.ClipBehavior.NONE,  # Remove a máscara de recorte para permitir gradientes
        bgcolor=ft.colors.WHITE,  # Cor de fundo do layout
        border_radius=ft.border_radius.all(20),  # Raio da borda do layout

        content=ft.Column(  # Coluna para organizar os contêineres verticalmente
            spacing=0,  # Espaçamento entre os contêineres
            controls=[
                image,  # Contêiner da imagem do bárbaro
                info,  # Contêiner das informações do bárbaro
                skills,  # Contêiner das habilidades do bárbaro
            ]
        )
    )

    # Adiciona o layout à página
    page.add(layout)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
