# Importe a biblioteca flet com o alias ft
import flet as ft

#flet -r TemplateRoute.py -w

# Defina a função principal que será executada no aplicativo
def main(page: ft.Page):

    def route_change(route):
        troute = ft.TemplateRoute(page.route)

        if troute.match("/loja/:produto"):
            page.add(
                ft.Text(
                    value=f"Acessando página do produto: {troute.produto}"
                )
            )

            # Pegando da API
            # produto = request.get("minhaapi.com.br/produtos/{troute.id}")



        elif troute.match("/loja/:produto/pedido/:id"):
            page.add(
                ft.Text(value=f"Acessando página de compra do produto: {troute.produto}, com ID: {troute.id}, {troute.id.isnumeric()}")
            )

            # troute.id.isnumeric()
        else:
            page.add(ft.Text(value="Página não encontrada"))

    page.on_route_change = route_change
    page.update()


# Verifique se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abra a página da web e execute a função principal nela
    ft.app(target=main)
