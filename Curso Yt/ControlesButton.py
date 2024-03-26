# Importa o módulo 'flet' com o alias 'ft'
import flet as ft

# Define a função principal 'main' que recebe um objeto 'page' do tipo 'ft.Page'
def main(page: ft.Page):

    def botao_clicado(e):
        page.add(ft.Text("Clicado"))

    botao = ft.ElevatedButton(text="Clique aqui", on_click=botao_clicado)

    page.add(botao)

# Inicializa a aplicação fornecendo a função 'main' como alvo
ft.app(target=main)
