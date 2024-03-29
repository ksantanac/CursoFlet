# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r Carousel.py
# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    # Configurações de alinhamento vertical e horizontal da página
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Cor de fundo da página
    page.bgcolor = ft.colors.BLACK

    # Função para expandir a imagem quando clicada
    def expand_img(e):
        # Percorre todos os controles do carrossel
        for c in carousel.controls:
            c.col = 1  # Redefine a coluna de cada controle para 1

        # Define a coluna do controle clicado
        e.control.col = 12 - len(carousel.controls) + 1

        # Atualiza o carrossel após as alterações
        carousel.update()

    # Cria um carrossel responsivo de imagens
    carousel = ft.ResponsiveRow(
        columns=12,  # Número de colunas do layout responsivo
        spacing=5,  # Espaçamento entre os controles
        controls=[
            ft.Container(  # Contêiner para cada imagem no carrossel
                col=1,  # Coluna inicial do contêiner
                image_src=f"https://picsum.photos/250/300?{num}",  # URL da imagem gerada aleatoriamente
                image_fit=ft.ImageFit.COVER,  # Ajuste da imagem dentro do contêiner
                border_radius= ft.border_radius.all(5),  # Raio da borda do contêiner
                on_click=expand_img  # Função chamada quando a imagem é clicada
            )
            for num in range(10, 18)  # Gera números de 10 a 17 para criar as imagens
        ]
    )

    # Define a coluna do primeiro controle para ocupar o restante das colunas disponíveis
    carousel.controls[0].col = 12 - len(carousel.controls) + 1

    # Layout principal que contém o carrossel
    layout = ft.Container(
        width=700,  # Largura do contêiner
        height=300,  # Altura do contêiner
        shadow= ft.BoxShadow(blur_radius=500, color=ft.colors.AMBER),  # Sombra do contêiner
        border_radius= ft.border_radius.all(10),  # Raio da borda do contêiner
        bgcolor=ft.colors.GREY_200,  # Cor de fundo do contêiner

        padding= ft.padding.all(5),  # Preenchimento interno do contêiner
        content=carousel  # Conteúdo do contêiner é o carrossel criado

    )

    # Adiciona o layout à página
    page.add(layout)

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
