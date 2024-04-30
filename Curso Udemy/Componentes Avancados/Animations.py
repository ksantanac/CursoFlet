import itertools  # Importa a biblioteca itertools para criar iteradores

import flet as ft  # Importa a biblioteca flet com o alias ft


# flet -r Animations.py

# Definição da classe AnimatedContainer que herda de ft.UserControl
class AnimatedContainer(ft.UserControl):
    # Iterador circular de cores para animação
    cores = itertools.cycle(["AMBER", "PINK", "CYAN", ])

    # Método construtor da classe
    def __init__(self, **kwargs):
        super().__init__()  # Chama o método construtor da classe pai
        self.kwargs = kwargs  # Argumentos adicionais para o contêiner

    # Método para construir o contêiner animado
    def build(self):
        # Retorna um contêiner com animações aplicadas
        return ft.Container(
            width=200,
            height=200,
            bgcolor=next(AnimatedContainer.cores),  # Cor do contêiner
            opacity=1,  # Opacidade inicial
            offset=ft.transform.Offset(x=0, y=0),  # Deslocamento inicial
            rotate=ft.transform.Rotate(angle=0, alignment=ft.alignment.center),  # Rotação inicial
            scale=ft.transform.Scale(scale=1),  # Escala inicial
            animate=ft.animation.Animation(duration=1000, curve=ft.AnimationCurve.EASE_IN_OUT),  # Animação padrão
            animate_opacity=True,  # Animar opacidade
            animate_scale=True,  # Animar escala
            animate_offset=True,  # Animar deslocamento
            animate_rotation=True,  # Animar rotação
            **self.kwargs  # Argumentos adicionais do contêiner
        )


# Função principal que será executada no aplicativo
def main(page: ft.Page):
    # Função para animar a opacidade do contêiner ao passar o mouse sobre ele
    def animate_opacity(e):
        e.control.opacity = 0.1 if e.control.opacity == 1 else 1  # Alterna entre opacidade 0.1 e 1
        e.control.update()  # Atualiza o contêiner

    # Função para animar o deslocamento do contêiner ao passar o mouse sobre ele
    def animate_offset(e):
        # Alterna entre deslocamento horizontal 0 e 0.5
        e.control.offset = ft.transform.Offset(x=0.5, y=0) if e.control.offset.x == 0 else ft.transform.Offset(x=0, y=0)
        e.control.update()  # Atualiza o contêiner

    # Função para animar a rotação do contêiner ao passar o mouse sobre ele
    def animate_rotation(e):
        import math  # Importa o módulo math para cálculos matemáticos

        # Alterna entre rotação 0 e 45 graus (em radianos)
        e.control.rotate.angle = math.radians(45) if e.control.rotate.angle == 0 else 0
        e.control.update()  # Atualiza o contêiner

    # Função para animar a escala do contêiner ao passar o mouse sobre ele
    def animate_scale(e):
        e.control.scale.scale = 0.5 if e.control.scale.scale == 1 else 1  # Alterna entre escala 0.5 e 1
        e.control.update()  # Atualiza o contêiner

    # Função para animar a posição do contêiner ao clicar sobre ele
    def animate_position(e):
        # Alterna entre posição superior (20, 0) e posição original (0, 400)
        e.control.top = 20 if e.control.top == 0 else 0
        e.control.left = 0 if e.control.left == 400 else 400
        e.control.update()  # Atualiza o contêiner

    # Adiciona contêineres animados à página
    page.add(
        ft.Column(
            controls=[
                AnimatedContainer(on_hover=animate_opacity),  # Contêiner com animação de opacidade
                AnimatedContainer(on_hover=animate_offset),  # Contêiner com animação de deslocamento
                AnimatedContainer(on_hover=animate_rotation),  # Contêiner com animação de rotação
                AnimatedContainer(on_hover=animate_scale),  # Contêiner com animação de escala
                AnimatedContainer(  # Contêiner com animação de posição ao clicar
                    top=0,
                    left=0,
                    animate_position=True,
                    on_click=animate_position
                ),
            ]
        )
    )


# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
