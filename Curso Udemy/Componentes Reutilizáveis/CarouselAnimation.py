# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r CarouselAnimation.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    # Configurações de alinhamento vertical e horizontal da página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Cor de fundo da página
    page.bgcolor = ft.colors.WHITE

    # Função para mover o carrossel para trás
    def move_backward(e):
        carousel.scroll_to(delta=-100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carousel.update()

    # Função para mover o carrossel para frente
    def move_forward(e):
        carousel.scroll_to(delta=100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carousel.update()

    # Layout principal da página
    layout = ft.Container(
        shadow=ft.BoxShadow(blur_radius=70),  # Sombra do contêiner
        content=ft.Column(  # Coluna que contém os controles
            controls=[
                # Atribuição de variável com o operador :=
                # Define o carrossel de imagens e o armazena na variável carousel
                carousel := ft.Row(
                    scroll=ft.ScrollMode.HIDDEN,  # Oculta a barra de rolagem do carrossel
                    controls=[  # Controles do carrossel (imagens)
                        ft.Image(  # Imagem do carrossel
                            src=f"https://picsum.photos/250/300?{num}"  # URL da imagem gerada aleatoriamente
                        ) for num in range(10)  # Gera 10 imagens aleatórias para o carrossel
                    ]
                ),
                ft.Row(  # Linha que contém os botões de navegação do carrossel
                    alignment=ft.MainAxisAlignment.END,  # Alinhamento dos botões à direita
                    controls=[
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT, on_click=move_backward),  # Botão para mover o carrossel para trás
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, on_click=move_forward)  # Botão para mover o carrossel para frente
                    ]
                )
            ]
        )
    )

    # Adiciona o layout à página
    page.add(layout)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
