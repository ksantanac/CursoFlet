# Importe a biblioteca flet com o alias ft
import flet as ft

# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    # Crie uma barra de navegação lateral (NavigationRail) com diferentes destinos
    rail = ft.NavigationRail(
        destinations=[
            # Destino com ícone de casa e rótulo "Inicio"
            ft.NavigationRailDestination(
                icon=ft.icons.HOME,
                label="Inicio"
            ),

            # Destino com apenas rótulo "Chat"
            ft.NavigationRailDestination(
                label="Chat"
            ),

            # Destino com ícone de marcador e rótulo "Itens salvos"
            # Ícone diferente quando selecionado
            ft.NavigationRailDestination(
                icon= ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Itens salvos",
            ),

            # Destino personalizado com ícones e rótulo "Configurações"
            # Conteúdo do ícone e ícone selecionado diferentes
            ft.NavigationRailDestination(
                icon_content=ft.Container(bgcolor="red", height=20, width=20),
                selected_icon_content=ft.Container(bgcolor="green", width=20, height=20),
                label="Configurações",
                padding=ft.padding.only(top=50),  # Adiciona padding somente no topo
            )
        ],

        bgcolor=ft.colors.GREY_900,  # Cor de fundo da barra de navegação
        selected_index=0,  # Índice do destino inicial selecionado
        extended=True,  # Define se a barra de navegação é estendida

        # Tamanho mínimo da barra de navegação estendida
        min_extended_width=200,

        # Botão no final da barra de navegação
        trailing=ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Cadastrar novo"),
                ft.PopupMenuItem(text="Enviar mensagem")
            ],
            icon=ft.icons.MORE_HORIZ  # Ícone do botão
        ),

        # Conteúdo no início da barra de navegação
        leading=ft.CircleAvatar(content=ft.Text(value="PA")),

        # Função de retorno de chamada chamada quando houver alteração na seleção
        on_change= lambda e: print(e.control.selected_index)
    )

    # Crie uma linha com a barra de navegação lateral
    row = ft.Row(controls=[rail], expand=True)

    # Adicione a linha à página
    page.add(row)

# Verifique se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abra a página da web e execute a função principal nela
    ft.app(target=main)
