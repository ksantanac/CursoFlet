# Importa o módulo 'flet' com o alias 'ft'
import flet as ft

# Define a função principal 'main' que recebe um objeto 'page' do tipo 'ft.Page'
def main(page: ft.Page):

    # Adiciona um DataTable à página
    page.add(
        ft.DataTable(
            # Define as colunas do DataTable
            columns=[
                ft.DataColumn(ft.Text("Primeira nome")),  # Coluna para o primeiro nome
                ft.DataColumn(ft.Text("Ultima nome")),    # Coluna para o último nome
                ft.DataColumn(ft.Text("Idade Coluna")),   # Coluna para a idade
            ],

            # Define as linhas do DataTable
            rows=[
                # Primeira linha com dados
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Kaue")),     # Célula com o primeiro nome "Kaue"
                        ft.DataCell(ft.Text("Santana")),  # Célula com o último nome "Santana"
                        ft.DataCell(ft.Text("15")),       # Célula com a idade "15"
                    ],
                ),

                # Segunda linha com dados
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text("Karina")),   # Célula com o primeiro nome "Karina"
                        ft.DataCell(ft.Text("Anjos")),    # Célula com o último nome "Anjos"
                        ft.DataCell(ft.Text("18")),       # Célula com a idade "18"
                    ],
                ),
            ]
        )
    )

# Inicializa a aplicação fornecendo a função 'main' como alvo
ft.app(target=main)
