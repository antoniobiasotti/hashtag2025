# Flet

# Importar
import flet as ft

# Criar um função main para rodar o app
def main(pagina):
# titulo
    titulo = ft.Text("Hashzap")

    #criar o popup
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    caixa_nome = ft.TextField()
    botao_popup = ft.ElevatedButton("Entrar no Chat")

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    # botao inicial
    def abrir_popup(evento):
        print("Clicou no botão")

    botao = ft.ElevatedButton("Iniciar Chat")

    #colocar os elementos na pagina
    pagina.add(titulo)
    pagina.add(botao)

# Executar a main
ft.app(main, view =ft.WEB_BROWSER)