# Importe a biblioteca flet com o alias ft
import flet as ft

# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    # Crie uma barra de navegação com diferentes destinos
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            # Destino inicial com ícone de casa e rótulo "Início"
            ft.NavigationDestination(
                icon=ft.icons.HOME,
                label="Início"
            ),

            # Destino com ícone de bate-papo e rótulo "Chat"
            ft.NavigationDestination(icon=ft.icons.CHAT, label="Chat"),

            # Destino com ícone de configurações e rótulo "Configurações"
            # Ícone diferente quando selecionado
            ft.NavigationDestination(
                icon=ft.icons.SETTINGS,
                selected_icon=ft.icons.SETTINGS_CELL_OUTLINED,
                label="Configurações"
            ),

            # Destino personalizado com ícones e tooltip
            ft.NavigationDestination(
                icon_content=ft.Container(bgcolor="red", height=20, width=20),
                selected_icon_content=ft.Container(bgcolor="green", width=20, height=20),
                label="Teste",
                tooltip="Selecione aqui"
            )
        ],
        selected_index=0,  # Índice do destino inicial selecionado
        indicator_color=ft.colors.GREY,  # Cor do indicador
        indicator_shape= ft.RoundedRectangleBorder(radius=5),  # Forma do indicador

        # Função de retorno de chamada chamada quando houver alteração na seleção
        on_change= lambda e: print(e.control.selected_index)
    )

    # Atualize a página
    page.update()

# Verifique se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abra a página da web e execute a função principal nela
    ft.app(target=main)
