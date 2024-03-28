# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r Views.py -w

# Defina a função principal que será executada no aplicativo

# Exemplo 3 - Navegação com troca de telas
def main(page: ft.Page):

    # Função para trocar a rota (página) quando a seleção no NavigationDrawer é alterada
    def change_route(e):
        match e.control.selected_index:
            case 0:
                page.go("/")   # Vai para a página inicial
            case 1:
                page.go("/loja")  # Vai para a página da loja
            case 2:
                page.go("/app")  # Vai para a página do aplicativo

    # Função chamada quando a rota (página) é alterada
    def route_change(route):
        # Limpa as visualizações existentes
        page.views.clear()

        # Adiciona uma visualização para a página inicial
        page.views.append(
            ft.View(
                route="/",
                appbar=ft.AppBar(title=ft.Text("Meu APP"), bgcolor=ft.colors.SURFACE_VARIANT),
                controls=[
                    ft.ElevatedButton("Ver loja", on_click=lambda _: page.go("/loja")),  # Botão para ir para a loja
                ],
                scroll=ft.ScrollMode.AUTO,
                auto_scroll=False,
                bgcolor=ft.colors.BLACK,
                drawer=ft.NavigationDrawer(  # NavigationDrawer na lateral da página
                    controls=[
                        ft.NavigationDrawerDestination(  # Destinos do NavigationDrawer
                            label="Home",
                            icon=ft.icons.HOME,
                        ),
                        ft.NavigationDrawerDestination(
                            icon_content=ft.Icon(ft.icons.STORE),
                            label="Loja",
                        ),
                        ft.NavigationDrawerDestination(
                            icon_content=ft.Icon(ft.icons.PHONE_ANDROID),
                            label="App",
                        ),
                    ],
                    on_change=change_route,  # Função chamada quando a seleção é alterada
                ),
                end_drawer=ft.NavigationDrawer(  # NavigationDrawer no final da página
                    controls=[
                        ft.NavigationDrawerDestination(label="Configurações"),
                        ft.NavigationDrawerDestination(label="Dados da conta"),
                        ft.NavigationDrawerDestination(label="Sair"),
                    ]
                ),
                floating_action_button=ft.FloatingActionButton(ft.icons.ADD),  # Botão de ação flutuante
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                vertical_alignment=ft.MainAxisAlignment.START,
                padding=ft.padding.all(100)  # Preenchimento da visualização
            )
        )

        # Adiciona visualizações para outras rotas (páginas)
        if page.route == "/":
            pass
        elif page.route == "/loja":
            page.views.append(
                ft.View(
                    route="/loja",
                    appbar=ft.AppBar(title=ft.Text("Loja"), bgcolor=ft.colors.SURFACE_VARIANT),
                    controls=[
                        ft.ElevatedButton("Ir para página inicial", on_click=lambda _: page.go("/")),  # Botão para ir para a página inicial
                        ft.ElevatedButton("Ir para App", on_click=lambda _: page.go("/app")),  # Botão para ir para a página do aplicativo
                    ],
                    fullscreen_dialog=False
                )
            )
        elif page.route == "/app":
            page.views.append(
                ft.View(
                    route="/app",
                    appbar=ft.AppBar(title=ft.Text("App"), bgcolor=ft.colors.SURFACE_VARIANT),
                    controls=[
                        ft.ElevatedButton("Ir para página inicial", on_click=lambda _: page.go("/")),  # Botão para ir para a página inicial
                    ],
                )
            )
        else:
            # Página não encontrada
            page.views.append(
                ft.View(
                    route="/404",
                    appbar=ft.AppBar(title=ft.Text("404"), bgcolor=ft.colors.SURFACE_VARIANT),
                    controls=[
                        ft.Text(value="Essa página não existe"),
                    ],
                )
            )

        # Atualiza a página
        page.update()

    # Função chamada quando uma visualização é removida da pilha
    def view_pop(view):
        page.views.pop()  # Remove a visualização
        top_view = page.views[-1]  # Obtém a visualização no topo da pilha
        page.go(top_view.route)  # Navega para a rota (página) da visualização no topo

    # Define as funções de rota e de remoção de visualização
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Navega para a rota (página) atual
    page.go(page.route)

# Verifique se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abra a página da web e execute a função principal nela
    ft.app(target=main)
