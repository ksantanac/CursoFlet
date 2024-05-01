import flet as ft  # Importa a biblioteca flet com o alias ft
from flet.auth.providers import GitHubOAuthProvider  # Importa o provedor de autenticação do GitHub
from flet.security import encrypt, decrypt  # Importa as funções de criptografia e descriptografia
import os  # Importa o módulo os para lidar com variáveis de ambiente
import requests  # Importa a biblioteca requests para fazer requisições HTTP

# Define as variáveis de ambiente para o Client ID e Client Secret do GitHub
GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
SECRET = os.getenv("SECRET")

# Atribui valores fixos para o Client ID, Client Secret e a chave secreta caso as variáveis de ambiente não estejam definidas
GITHUB_CLIENT_ID = "c118d5c61e2433833bfe"
GITHUB_CLIENT_SECRET = "b67bb2b8eebeeb58840820a5ef9ba8242b02e1ef"
SECRET = "FDSAJHGFIUSDHGFUHSDFJKLHSDUKFHSOIUHFOUISDGHFIUSDHGFIU"

# Definição da função principal que será executada no aplicativo
def main(page: ft.Page):

    # Configuração do provedor de autenticação do GitHub
    provider = GitHubOAuthProvider(
        client_id=GITHUB_CLIENT_ID,
        client_secret=GITHUB_CLIENT_SECRET,
        redirect_url="http://127.0.0.1:5354/api/oauth/redirect"
    )

    # Recupera o token criptografado armazenado localmente, se existir
    encrypted_token = page.client_storage.get("token_github")

    # Se um token criptografado for encontrado, tenta fazer login com ele
    if encrypted_token:
        saved_token = decrypt(encrypted_token, SECRET)
        page.login(provider=provider, saved_token=saved_token)

    # Função chamada quando ocorre um evento de login
    def on_login(e: ft.LoginEvent):
        if not e.error:  # Se não houver erros no login
            token = page.auth.token.to_json()  # Obtém o token de autenticação e converte para JSON
            encrypted_token = encrypt(token, SECRET)  # Criptografa o token
            page.client_storage.set("github_token", encrypted_token)  # Armazena o token criptografado localmente
        else:
            print("Erro: ", e.error)  # Exibe o erro de login
            print("Erro: ", e.error_description)  # Exibe a descrição do erro de login

    # Atribui a função on_login ao evento de login da página
    page.on_login = on_login

    # Se o usuário estiver autenticado, exibe as informações do usuário e seus repositórios
    if page.auth:
        page.add(
            ft.CircleAvatar(
                foreground_image_url=page.auth.user.get("avatar_url")  # Exibe o avatar do usuário
            ),
            ft.Text(
                value=page.auth.user.get("login"),  # Exibe o nome de usuário
                size=30
            )
        )

        # Obtém os repositórios do usuário autenticado
        headers = {"Authorization": f"{page.auth.token.token_type} {page.auth.token.access_token}"}
        repos_resp = requests.get("https://api.github.com/user/repos", headers=headers)
        user_repos = repos_resp.json()

        # Exibe o nome completo de cada repositório do usuário
        for repo in user_repos:
            page.add(ft.Text(value=repo["full_name"]))

    else:  # Se o usuário não estiver autenticado, exibe o botão de login com GitHub
        page.add(
            ft.ElevatedButton(
                text="Login com Github",
                on_click=lambda _: page.login(provider=provider)
            )
        )

# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
