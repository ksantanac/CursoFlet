import flet as ft  # Importa a biblioteca flet com o alias ft
import time  # Importa o módulo time para lidar com pausas no código

# flet -r UserControler.py

# Definição da classe Product que herda de ft.UserControl
class Product(ft.UserControl):

    # Método construtor da classe Product
    def __init__(self, image: str, title: str):
        super().__init__()  # Chama o método construtor da classe pai
        self.image = image  # Define a imagem do produto
        self.title = title  # Define o título do produto

    # Método para construir a representação visual do produto
    def build(self):
        # Retorna um contêiner com a imagem e o título do produto
        return ft.Container(
            image_src=self.image,
            image_fit=ft.ImageFit.COVER,
            height=500,
            aspect_ratio=1.0,
            alignment=ft.alignment.bottom_center,
            padding=ft.padding.all(20),
            content=ft.Text(
                value=self.title,
                size=30,
                color=ft.colors.BLACK,
                weight=ft.FontWeight.BOLD
            )
        )

    # Método chamado após a inserção do produto na página
    def did_mount(self):
        print(f"O produto {self.title} foi inserido na página")

    # Método chamado antes da remoção do produto da página
    def will_unmount(self):
        print(f"Removendo o produto {self.title}")

    # Método para destruir o controle do produto
    def destroy(self):
        self.will_unmount()  # Chama o método will_unmount
        self.clean()  # Limpa o controle

# Função principal que será executada no aplicativo
def main(page: ft.Page):
    # Cria instâncias de Product com diferentes imagens e títulos
    prod1 = Product(
            image="https://alonsofotografia.com.br/wp-content/uploads/2019/02/fotos-de-cadeiras-para-e-commerce.jpg",
            title="Cadeiras bege"
        )

    prod2 = Product(
        image="https://images.tcdn.com.br/img/img_prod/1101616/conjunto_de_jantar_mesa_industrial_pes_em_metal_4_cadeiras_2781_1_e3dd58642a684da7f14a105db597a381.jpg",
        title="Mesa"
    )

    # Adiciona o primeiro produto à página
    page.add(prod1)

    time.sleep(3)  # Pausa de 3 segundos

    # Adiciona o segundo produto à página após 3 segundos
    page.add(prod2)

    time.sleep(2)  # Pausa de 2 segundos

    prod1.destroy()  # Destroi o primeiro produto após 2 segundos


# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
