import flet as ft  # Importa a biblioteca flet com o alias ft


# flet run DadosCliente.py -w -p 5353

# Definição da função principal que será executada no aplicativo
def main(page: ft.Page):
    # Função para listar as tarefas armazenadas localmente
    def list_tasks():
        # Obtém as tarefas armazenadas localmente
        items = page.client_storage.get("tasks")

        # Se não houver tarefas armazenadas, inicializa a lista vazia
        if not items:
            items = []

        # Função para atualizar o estado da tarefa quando o checkbox é alterado
        def change_state(e):
            item = {"label": e.control.label, "selected": e.control.value}
            items[e.control.data] = item
            page.client_storage.set("tasks", items)

        # Cria os controles de checkbox para cada tarefa e atribui a função de alteração de estado
        lv.controls = [
            ft.Checkbox(
                value=item.get("selected"),
                label=item.get("label"),
                adaptive=True,
                data=index,
                on_change=change_state
            ) for index, item in enumerate(items)
        ]
        lv.update()

    # Função para salvar uma nova tarefa localmente
    def save_locally(e):
        item = {"label": e.control.value, "selected": False}
        items = page.client_storage.get("tasks")

        # Se não houver tarefas armazenadas, inicializa a lista vazia
        if not items:
            items = []

        # Adiciona a nova tarefa à lista de tarefas
        items.append(item)

        # Atualiza as tarefas armazenadas localmente
        page.client_storage.set("tasks", items)

        # Limpa o campo de entrada após a adição da nova tarefa
        e.control.value = ""
        e.control.update()

    # Cria um campo de texto para adicionar novas tarefas
    tf = ft.TextField(on_submit=save_locally)

    # Cria uma lista para exibir as tarefas armazenadas
    lv = ft.ListView()

    # Adiciona o campo de texto e a lista à página
    page.add(tf, lv)

    # Chama a função para listar as tarefas armazenadas localmente
    list_tasks()

    # Verifica se a sessão contém uma chave específica
    page.session.contains_key()


# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
