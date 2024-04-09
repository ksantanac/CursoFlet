import flet as ft  # Importa a biblioteca flet com o alias ft
import sqlite3  # Importa o módulo sqlite3 para interagir com o banco de dados SQLite


# flet -r todo.py

# Definição da classe Todo
class Todo:
    # Método construtor da classe
    def __init__(self, page: ft.Page):
        # Inicialização de variáveis e configuração da página
        self.page = page
        self.page.bgcolor = ft.colors.BLACK
        self.page.window_width = 350
        self.page.window_height = 400
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = "ToDo App"
        self.task = ''
        self.view = "all"

        # Criação da tabela 'tasks' se não existir no banco de dados
        self.db_execute("CREATE TABLE IF NOT EXISTS tasks(name, status)")
        # Consulta inicial para obter todas as tarefas
        self.results = self.db_execute("SELECT * FROM tasks")

        # Chamada para criar a página principal
        self.main_page()

    # Método para executar consultas no banco de dados
    def db_execute(self, query, params=[]):
        with sqlite3.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(query, params)
            con.commit()
            return cur.fetchall()

    # Método chamado quando a checkbox de uma tarefa é marcada ou desmarcada
    def checked(self, e):
        is_checked = e.control.value
        label = e.control.label

        # Atualiza o status da tarefa no banco de dados com base na marcação da checkbox
        if is_checked:
            self.db_execute('UPDATE tasks SET status = "complete" WHERE name = ?', params=[label])
        else:
            self.db_execute('UPDATE tasks SET status = "incomplete" WHERE name = ?', params=[label])

        # Atualiza a lista de tarefas com base na visualização selecionada
        if self.view == "all":
            self.results = self.db_execute("SELECT * FROM tasks")
        else:
            self.results = self.db_execute("SELECT * FROM tasks WHERE status =?", params=[self.view])

        # Atualiza a lista de tarefas na página
        self.update_task_list()

    # Método para criar o contêiner das tarefas
    def tasks_container(self):
        return ft.Container(
            height=self.page.height * 0.8,
            content=ft.Column(
                controls=[
                    ft.Checkbox(
                        on_change=self.checked,
                        label=res[0],
                        value=True if res[1] == "complete" else False,
                    )
                    for res in self.results if res
                ]
            )
        )

    # Método chamado quando o valor do campo de entrada é alterado
    def set_value(self, e):
        self.task = e.control.value

    # Método chamado para adicionar uma nova tarefa
    def add(self, e, input_task):
        name = self.task
        status = "incomplete"

        # Insere a nova tarefa no banco de dados e limpa o campo de entrada
        if name:
            self.db_execute(query="INSERT INTO tasks VALUES(?, ?)", params=[name, status])
            input_task.value = ""
            self.results = self.db_execute("SELECT * FROM tasks")
            self.update_task_list()

    # Método chamado quando o usuário muda de guia (todos, em andamento, finalizados)
    def tabs_changed(self, e):
        if e.control.selected_index == 0:
            self.results = self.db_execute("SELECT * FROM tasks")
            self.view = "all"
        elif e.control.selected_index == 1:
            self.results = self.db_execute('SELECT * FROM tasks WHERE status = "incomplete" ')
            self.view = "incomplete"
        elif e.control.selected_index == 2:
            self.results = self.db_execute('SELECT * FROM tasks WHERE status = "complete" ')
            self.view = "complete"

        self.update_task_list()

    # Método para atualizar a lista de tarefas na página
    def update_task_list(self):
        tasks = self.tasks_container()
        self.page.controls.pop()  # Remove a lista de tarefas antiga
        self.page.add(tasks)  # Adiciona a lista de tarefas atualizada
        self.page.update()

    # Método para criar a página principal
    def main_page(self):
        # Campo de entrada para adicionar novas tarefas
        input_task = ft.TextField(
            hint_text="Digite uma tarefa",
            expand=True,
            border_color=ft.colors.WHITE,
            on_change=self.set_value,
        )

        # Barra de entrada com o campo de texto e o botão de adicionar tarefa
        input_bar = ft.Row(
            controls=[
                input_task,
                ft.FloatingActionButton(
                    icon=ft.icons.ADD,
                    on_click=lambda e: self.add(e, input_task)
                )
            ]
        )

        # Guias para selecionar a visualização das tarefas
        tabs = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="Todos"),
                ft.Tab(text="Em andamento"),
                ft.Tab(text="Finalizados"),
            ]
        )

        # Contêiner para exibir as tarefas
        tasks = self.tasks_container()

        # Adiciona os controles à página
        self.page.add(input_bar, tabs, tasks)


# Executa o aplicativo com a classe Todo como alvo
ft.app(target=Todo)
