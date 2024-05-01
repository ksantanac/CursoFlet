import flet as ft  # Importa a biblioteca flet com o alias ft
import os  # Importa o módulo os para interagir com o sistema operacional
from flet.security import encrypt, decrypt  # Importa as funções de criptografia do módulo de segurança do Flet


# flet run Criptografia.py -w -p 5353

# Definição da função principal que será executada no aplicativo
def main(page: ft.Page):
    # Chave secreta para criptografia
    secret_key = "dfsakohfaohok34h32h4"

    # Texto a ser criptografado
    texto = "Dado que não deve ser exposto"

    # Criptografa o texto usando a chave secreta
    text_cript = encrypt(texto, secret_key)

    # Adiciona o texto criptografado à página
    page.add(ft.Text(value=text_cript))

    # Descriptografa o texto criptografado usando a mesma chave
    text_descript = decrypt(text_cript, secret_key)

    # Adiciona o texto descriptografado à página
    page.add(ft.Text(value=text_descript))

    # Armazena a senha no armazenamento do cliente
    page.client_storage.set("senha", texto)

    # Armazena a senha criptografada no armazenamento do cliente
    page.client_storage.set("senha", text_cript)

    # Gera uma chave aleatória usando o módulo secrets
    import secrets
    chave = secrets.token_hex(30)

    # Adiciona a chave à página
    page.add(ft.Text(value=chave, size=20))


# Verifica se este script está sendo executado diretamente
if __name__ == '__main__':
    # Abre a página da web e executa a função principal nela
    ft.app(target=main)
