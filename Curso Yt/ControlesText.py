# Importa o módulo 'flet' com o alias 'ft'
import flet as ft

# Define a função principal 'main' que recebe um objeto 'page' do tipo 'ft.Page'
def main(page: ft.Page):
    # Cria três objetos de texto: 'a', 'b' e 'c'
    a = ft.Text("A")  # Objeto de texto com conteúdo "A"
    b = ft.Text("B")  # Objeto de texto com conteúdo "B"
    c = ft.Text("C")  # Objeto de texto com conteúdo "C"

    # Adiciona uma linha à página com os objetos de texto 'a', 'b' e 'c' como controles
    page.add(
        ft.Row(controls=[a, b, c]))  # Uma linha contendo os controles 'a', 'b' e 'c'

# Inicializa a aplicação fornecendo a função 'main' como alvo
ft.app(target=main)
