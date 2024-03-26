# Importa a biblioteca 'flet' e a renomeia como 'ft' para facilitar o uso
import flet as ft

# Define a função principal 'main' que recebe um objeto 'page' do tipo 'ft.Page'
def main(page: ft.Page):
    # Define o título da página
    page.title = "Responsive Row"

    # Cria uma linha responsiva com duas colunas, cada uma ocupando 6 unidades de largura em dispositivos pequenos (celulares e tablets)
    res = ft.ResponsiveRow(
        ft.Column(col={"sm":6}, controls=[ft.Text("Coluna 1")]),
        ft.Column(col={"sm": 6}, controls=[ft.Text("Coluna 2")]),
    )

    # Cria um texto de sobreposição com posicionamento personalizado
    pw = ft.Text(bottom=50, right=50, style='displaysmall')
    # Adiciona o texto de sobreposição à página
    page.overlay.append(pw)

    # Adiciona uma nova linha responsiva à página, contendo quatro contêineres (colunas)
    page.add(
        ft.ResponsiveRow(
            [
                # Primeiro contêiner (coluna) com texto e estilo de fundo amarelo
                ft.Container(
                    ft.Text("Coluna 1"),
                    padding=5,
                    bgcolor=ft.colors.YELLOW,
                    col={'sm':6, 'md':4, 'xl': 2},
                ),

                # Segundo contêiner (coluna) com texto e estilo de fundo cinza azulado
                ft.Container(
                    ft.Text("Coluna 2"),
                    padding=5,
                    bgcolor=ft.colors.BLUE_GREY,
                    col={'sm': 6, 'md': 4, 'xl': 2},
                ),

                # Terceiro contêiner (coluna) com texto branco e fundo preto
                ft.Container(
                    ft.Text("Coluna 3", color='white'),
                    padding=5,
                    bgcolor=ft.colors.BLACK,
                    col={'sm': 6, 'md': 4, 'xl': 2},
                ),

                # Quarto contêiner (coluna) com texto branco e fundo verde
                ft.Container(
                    ft.Text("Coluna 4", color='white'),
                    padding=5,
                    bgcolor=ft.colors.GREEN,
                    col={'sm': 6, 'md': 4, 'xl': 2},
                ),
            ]
        )
    )

# Inicia a aplicação com a função principal 'main' como alvo
ft.app(target=main)
