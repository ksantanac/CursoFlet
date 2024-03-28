# Importe a biblioteca flet com o alias ft
import flet as ft

# flet -r Views.py -w

# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    page.add(ft.Text("Página Inical", size=40))

    def route_change(e: ft.RouteChangeEvent):
        page.add(ft.Text(f"Acessando: {e.route}", size=40))


    page.on_route_change = route_change

    page.add(
        ft.ElevatedButton(
        text="Ir para a loja",

        # Acessa rota especififca
        on_click= lambda _: page.go("/loja")
        ),

        ft.ElevatedButton(
            text="Home",

            # Acessa rota especififca
            on_click=lambda _: page.go("/")
        ),

        ft.ElevatedButton(
            text="Ir para compras",

            # Acessa rota especififca
            on_click=lambda _: page.go("/minhas-compras")
        )
    )



# Verifique se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abra a página da web e execute a função principal nela
    ft.app(target=main)
