# Importa a biblioteca 'flet' e a renomeia como 'ft' para facilitar o uso
import flet as ft

# Define a função principal 'main' que recebe um objeto 'page' do tipo 'ft.Page'
def main(page: ft.Page):

    # Define o título da página
    page.title = "Cartao"

    # Adiciona um cartão à página com conteúdo interno
    page.add(
        ft.Card(
            # Conteúdo interno do cartão, um contêiner com uma coluna de elementos
            content = ft.Container(
                # Conteúdo da coluna
                content= ft.Column(
                    [
                        # Elemento ListTile contendo um ícone, um título e um subtítulo
                        ft.ListTile(
                            leading=ft.Icon(ft.icons.ALBUM),  # Ícone à esquerda do ListTile
                            title= ft.Text("Como posso não seguir"),  # Título do ListTile
                            subtitle= ft.Text("Musica de alguém")  # Subtítulo do ListTile
                        ),

                        # Linha com dois botões de texto
                        ft.Row(
                            [
                                ft.TextButton("Comprar bilhetes"),  # Botão de texto "Comprar bilhetes"
                                ft.TextButton("Ouvir")  # Botão de texto "Ouvir"
                            ],
                            alignment= ft.MainAxisAlignment.CENTER,  # Alinhamento dos botões no centro da linha
                        )

                    ]
                ),
                width=400,  # Largura do contêiner
                padding=10,  # Preenchimento interno do contêiner

            )
        )
    )

# Inicia a aplicação com a função principal 'main' como alvo
ft.app(target=main)
