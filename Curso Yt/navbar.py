# Importa a biblioteca 'flet' e a renomeia como 'ft' para facilitar o uso
import flet as ft

# Define a função principal 'main' que recebe um objeto 'page' do tipo 'ft.Page'
def main(page: ft.Page):

    # Define uma função local 'check_click' para lidar com cliques em itens do menu
    def check_click(e):
        # Altera o estado de seleção do item clicado
        e.control.checked = not e.control.checked
        # Atualiza a página para refletir a mudança
        page.update()


    # Configura a barra de aplicativos (AppBar)
    page.appbar = ft.AppBar(

        # Configura o ícone à esquerda da barra de aplicativos
        leading= ft.Icon(ft.icons.PALETTE),
        # Define a largura do ícone à esquerda
        leading_width=40,
        # Define o título da barra de aplicativos
        title= ft.Text("AppBar Exemplo"),
        # Define se o título deve estar centralizado
        center_title = True,
        # Define a cor de fundo da barra de aplicativos
        bgcolor= ft.colors.SURFACE_VARIANT,
        # Define as ações (ícones de botão) à direita da barra de aplicativos
        actions= [
            # Botão de ícone para alternar entre temas claro e escuro
            ft.IconButton(ft.icons.WB_SUNNY_OUTLINED),
            # Botão de ícone para aplicar filtros
            ft.IconButton(ft.icons.FILTER_3),

            # Botão de menu popup com itens de menu
            ft.PopupMenuButton(
                items=[
                    # Item do menu 1
                    ft.PopupMenuItem(text="Item 1"),
                    # Item do menu 2
                    ft.PopupMenuItem(text="Item 2"),
                    # Item do menu com a capacidade de ser marcado
                    ft.PopupMenuItem(
                        text="Checked item", checked=False, on_click=check_click
                    )
                ]
            )
        ],

    )

    page.add(ft.Text("Body!"))

    # Atualiza a página para aplicar todas as configurações acima
    page.update()

# Inicia a aplicação com a função principal 'main' como alvo
ft.app(target=main)
