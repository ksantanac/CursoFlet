# Importa a biblioteca 'flet' e a renomeia como 'ft' para facilitar o uso
import flet as ft


# Define a função principal 'main' que recebe um objeto 'page' do tipo 'ft.Page'
def main(page: ft.Page):

    page.theme_mode = ft.ThemeMode.LIGHT

    # Define o título da página
    page.title = "Falando sobre conteiner"

    # Define o preenchimento da página como 0 (sem preenchimento)
    page.padding = 0

    # Define a largura e altura da janela da página
    page.window_width = 400
    page.window_height = 450

    # Envia as alterações para a aplicação para atualizar a página
    page.update()

    # Define dois contêineres com botões elevados dentro deles
    c1 = ft.Container(
        content=ft.ElevatedButton("Botão elevado no container 1"),
        bgcolor="#f34563",  # Define a cor de fundo do contêiner
        padding=5  # Define o preenchimento interno do contêiner
    )

    c2 = ft.Container(
        content=ft.ElevatedButton("Botão elevado no container 2"),
        bgcolor="#f34563",  # Define a cor de fundo do contêiner
        padding=5  # Define o preenchimento interno do contêiner
    )

    # Lista de controles que contém os contêineres criados anteriormente
    item = [c1, c2]

    # Cria uma linha horizontal com os controles especificados e espaçamento entre eles
    row = ft.Row(spacing=10, controls=item)

    # Cria uma coluna vertical com os controles especificados e espaçamento entre eles
    coluna = ft.Column(spacing=10, controls=item)

    # Cria um ListView (exibição de lista) com os controles especificados, permitindo expansão, espaçamento e rolagem automática
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)

    # Adiciona um texto "Teste" e a coluna criada anteriormente ao ListView
    lv.controls.append(ft.Text("Teste"))
    lv.controls.append(coluna)

    # Cria um GridView (exibição de grade) com os controles especificados, definindo o número máximo de itens em cada linha e outras configurações
    gv = ft.GridView(expand=1, runs_count=5, max_extent=150, child_aspect_ratio=1.0, spacing=7,
                     run_spacing=5)

    # Adiciona várias imagens com borda arredondada ao GridView, utilizando a API do Picsum para obter imagens de exemplo
    for i in range(0, 30):
        gv.controls.append(
            ft.Image(
                src=f"https://picsum.photos/150/150?{i}",
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10)  # Define o raio do canto para criar bordas arredondadas
            ))

    # Adiciona os ListView e GridView à página
    page.add(lv, gv)


# Inicia a aplicação com a função principal 'main' como alvo
ft.app(target=main)
