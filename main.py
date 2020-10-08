import socket
import os
import config
from views import *


IP_ADDRESS = config.get_ipAdress()
PORT = config.get_port()
DIR = config.get_dir()

def readView(url):
    with open(DIR + url) as template:
       return template.read()

def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method, url)

def generate_headers(method, url):
    if not method == 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)

    if  os.path.exists(DIR + url) == False:
        return ('HTTP/1.1 404 Not found\n\n', 404)

    return ('HTTP/1.1 200 OK\n\n', 200)

def generate_content(code, url):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return readView(url)

def generate_response(request, method, url):
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    return (headers + body).encode()

def postRequest( request):
    method, url = parse_request(request)
    print(method, url)
    #body = URLS['/handlerPostRequest'](request)
    #return ('<h1>405</h1><p>Method not allowed</p>', body)

def getOrPost(request):
    method, url = parse_request(request.decode())
    if method == 'POST':
        postResponse = postRequest(request.decode())
        return postResponse
    else:
        response = generate_response(request.decode('utf-8'), method, url)
        return response

def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #параметры
    server.bind((IP_ADDRESS, PORT))
    server.listen()

    while True:
        client_socket, addr = server.accept()
        request = client_socket.recv(2048)

        response = getOrPost(request)

        client_socket.sendall(response)
        client_socket.close()

if __name__ == '__main__':
    run()