# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r BottomAppBar.py

# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    # Crie um BottomAppBar com uma barra de aplicativo na parte inferior da página
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=ft.colors.BLUE,  # Cor de fundo da barra inferior
        shape=ft.NotchShape.CIRCULAR,  # Formato da barra inferior (circular neste caso)
        content= ft.Row(  # Conteúdo da barra inferior
            controls=[
                ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),  # Botão do menu
                ft.Container(expand=True),  # Container expansível para ocupar o espaço restante
                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),  # Botão de pesquisa
                ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE)  # Botão de favoritos
            ],
            # alignment=ft.MainAxisAlignment.SPACE_BETWEEN  # Alinhamento do conteúdo (opcional)
        )

    )

    # Adicione um botão de ação flutuante na parte inferior da página
    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD  # Ícone do botão de ação flutuante
    )

    page.update()  # Atualize a página


# Verifique se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abra a página da web e execute a função principal nela
    ft.app(target=main)
