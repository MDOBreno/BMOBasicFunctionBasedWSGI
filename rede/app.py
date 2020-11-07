from wsgiref.simple_server import make_server

def web_app(environment, response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    response(status, headers)

    return [b'<strong>Ola Mundo Eu acabei de criar meu primeiro WSGI</strong>']


with make_server('', 8000, web_app) as server:
    print("Servindo na porta 8000...\nVisite http://127.0.0.1:8000\nPara finalizar o servidor insira 'Control + C' ")

    server.serve_forever()