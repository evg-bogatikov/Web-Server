import socket
import os
import config
import zlib

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
        return ('HTTP/1.1 405 Method not allowed\n', 405)

    #os.path.exists - возвращает True, если path указывает на существующий путь или дескриптор открытого файла
    #os.path.isfile - является ли путь файлом
    if  os.path.exists(DIR + url) == False or os.path.isfile(DIR + url) == False:
        return ('HTTP/1.1 404 Not found\n', 404)

    return ('HTTP/1.1 200 OK\n', 200)#перенос

def generate_content_status(code):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return 200

def getResponse(request, method, url):
    headers, code = generate_headers(method, url)

    content_status = generate_content_status(code)
    if content_status == 200:
        formatUrl = url.split('.')
        if formatUrl[formatUrl.__len__() - 1] == 'jpg' or formatUrl[formatUrl.__len__() - 1] == 'png' or formatUrl[formatUrl.__len__() - 1] == 'gif':
            additional_header, r = pictureResponse(url)
            return (headers + additional_header).encode() + r
        else:
            body = readView(url)
            return (headers + '\n' + body).encode()

    return (headers + '\n' + content_status).encode()

def pictureResponse(url):
    #rb - Opens a file for reading only in binary format.
    f = open(DIR + url, 'rb')
    r = f.read()
    additional_header = 'Content-Length: ' + r.__sizeof__().__str__() + '\nContent-Type: image/gif\n\n'
    f.close()
    return additional_header, r

def postRequest(request):

    return "<h1>1343</h1>".encode()
    #body = URLS['/handlerPostRequest'](request)
    #return ('<h1>405</h1><p>Method not allowed</p>', body)

def getOrPost(request):
    method, url = parse_request(request.decode())
    if method == 'POST':

        postResponse = postRequest(request)
        return postResponse
    else:
        response = getResponse(request.decode('utf-8'), method, url)
        return response

def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   # server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #параметры
    server.bind((IP_ADDRESS, PORT))
    server.listen()

    while True:
        client_socket, addr = server.accept()
        request = client_socket.recv(2048)
        print(request)
        response = getOrPost(request)

        client_socket.sendall(response)
        client_socket.close()

if __name__ == '__main__':
    run()