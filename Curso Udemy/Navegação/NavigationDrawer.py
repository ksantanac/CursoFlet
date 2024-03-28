# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r NavigationDrawer.py

# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    # Crie um NavigationDrawer com diferentes destinos e configurações
    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=12),  # Espaçamento entre os itens do NavigationDrawer
            # Destino do NavigationDrawer com ícone e rótulo
            ft.NavigationDrawerDestination(
                label="Item 1",
                icon = ft.icons.DOOR_BACK_DOOR_OUTLINED,  # Ícone não selecionado
                selected_icon_content=ft.Icon(ft.icons.DOOR_BACK_DOOR),  # Ícone selecionado
            ),

            # Destino do NavigationDrawer com rótulo e conteúdo personalizado (botão)
            ft.NavigationDrawerDestination(
                label="Item 2",
                icon_content=ft.FilledButton(text="Botão")  # Botão como conteúdo
            ),

            # Destino do NavigationDrawer com ícone, rótulo e ícone selecionado
            ft.NavigationDrawerDestination(
                label="Item 3",
                icon=ft.icons.PHONE_OUTLINED,  # Ícone não selecionado
                selected_icon=ft.icons.PHONE  # Ícone selecionado
            ),
        ],
        bgcolor= ft.colors.GREY_900,  # Cor de fundo do NavigationDrawer
        indicator_color= ft.colors.DEEP_ORANGE,  # Cor do indicador de seleção
        indicator_shape= ft.RoundedRectangleBorder(radius=10),  # Forma do indicador de seleção
        selected_index=0,  # Índice do destino inicial selecionado
        tile_padding=ft.padding.all(20),  # Preenchimento dos itens do NavigationDrawer

        # Função de retorno de chamada chamada quando houver alteração na seleção
        on_change= lambda  e: print(e.control.selected_index)
    )

    # Defina uma função para mostrar o NavigationDrawer quando o botão é clicado
    def show_drawer(e):
        page.drawer.open = True
        page.drawer.update()

    # Crie um botão de ícone para abrir o NavigationDrawer
    btn = ft.IconButton(icon= ft.icons.MENU, on_click= show_drawer)
    page.add(btn)  # Adicione o botão à página


# Verifique se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abra a página da web e execute a função principal nela
    ft.app(target=main)
