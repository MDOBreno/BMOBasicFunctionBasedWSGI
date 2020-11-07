
from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

#Remoção de Warnings do console
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def web_app(environment, response):
    #Criação de cabeçalho da resposta informando que houve um recebimento OK
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    response(status, headers)

    # A variável de environment(ambiente) CONTENT_LENGTH pode estar vazia(se for GET) ou não(se for POST)
    try:
        request_body_size = int(environment.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    # Quando o método for POST a variável será enviada
    # no corpo da solicitação HTTP que é passado pelo servidor WSGI
    # no próprio arquivo como sendo a variável de ambiente wsgi.input
    if request_body_size > 0:       #Se for POST:
        d = parse_qs(environment['wsgi.input'].read(request_body_size))
        usuario = (d.get(b'usuario', [''])[0]).decode('utf-8')
        enderecoDeEmail = (d.get(b'enderecoDeEmail', [''])[0]).decode('utf-8')
    else:                           #Se for GET:
        d = parse_qs(environment['QUERY_STRING'])
        usuario = d.get('usuario', [''])[0]
        enderecoDeEmail = d.get('enderecoDeEmail', [''])[0]

    # Sempre escape(livre-se) de novas entradas/digitações do usuário para evitar injeção de script
    usuario = escape(usuario)
    enderecoDeEmail = escape(enderecoDeEmail)

    # Cria o corpo da resposta HTTP para ser exibida no navegador do usuario
    resposta = ("<strong>Seu usuário é: " + usuario + "</strong>"
                "<br />"
                "<strong>Seu e-mail é: " + enderecoDeEmail + "</strong>")

    return [resposta.encode()]



with make_server('', 8000, web_app) as server:
    print("Servindo na porta 8000...\nVisite http://127.0.0.1:8000\nPara finalizar o servidor insira 'Control + C' ")
    # Deixa o servidor ligado para sempre ou até que seu administrador encerre sua execução
    server.serve_forever()


