
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape


import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def web_app(environment, response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    response(status, headers)

    #form = cgi.FieldStorage()
    # the environment variable CONTENT_LENGTH may be empty(if its GET) or not(if its POST)
    try:
        request_body_size = int(environment.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    if request_body_size > 0:       #Se for POST:
        d = parse_qs(environment['wsgi.input'].read(request_body_size))
        usuario = (d.get(b'usuario', [''])[0]).decode('utf-8')  # Returns the first usuario value.
        enderecoDeEmail = (d.get(b'enderecoDeEmail', [''])[0]).decode('utf-8')  # Returns the first enderecoDeEmail value.
    else:                           #Se for GET:
        d = parse_qs(environment['QUERY_STRING'])
        usuario = d.get('usuario', [''])[0]  # Returns the first usuario value.
        enderecoDeEmail = d.get('enderecoDeEmail', [''])[0]  # Returns the first enderecoDeEmail value.

    # Always escape user input to avoid script injection
    usuario = escape(usuario)
    enderecoDeEmail = escape(enderecoDeEmail)

    resposta = ("<strong>Seu usuário é: " + usuario + "</strong>"
                "<br />"
                "<strong>Seu e-mail é: " + enderecoDeEmail + "</strong>")

    return [resposta.encode()]



with make_server('', 8000, web_app) as server:
    print("Servindo na porta 8000...\nVisite http://127.0.0.1:8000\nPara finalizar o servidor insira 'Control + C' ")
    server.serve_forever()


