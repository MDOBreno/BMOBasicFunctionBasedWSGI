
from wsgiref.simple_server import make_server
import cgi, cgitb



def web_app(environment, response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    response(status, headers)

    form = cgi.FieldStorage()
    usuario = "Ola" #form["usuario"].value
    enderecoDeEmail = "Mundo" #form["enderecoDeEmail"].value
    resposta = ("<strong>Seu usuario e: " + usuario + "</strong>"
                "<br />"
                "<strong>Seu e-mail e: " + enderecoDeEmail + "</strong>")

    return [resposta.encode()]



with make_server('', 8000, web_app) as server:
    print("Servindo na porta 8000...\nVisite http://127.0.0.1:8000\nPara finalizar o servidor insira 'Control + C' ")
    server.serve_forever()


