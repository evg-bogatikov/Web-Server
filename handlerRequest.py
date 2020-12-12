import os
import config
import getRequest
import postRequest

DIR = config.get_dir()
POST = {}
def generateContentStatus(code):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return 200

def parseRequest(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method, url)

def generateHeaders(method, url):
    if not method == 'GET' and not method == 'POST':
        return ('HTTP/1.1 405 Method not allowed\n', 405)

    #os.path.exists - возвращает True, если path указывает на существующий путь или дескриптор открытого файла
    #os.path.isfile - является ли путь файлом
    if os.path.exists(config.get_dir() + url) == False or os.path.isfile(config.get_dir() + url) == False:
        return ('HTTP/1.1 404 Not found\n', 404)

    return ('HTTP/1.1 200 OK\n', 200)

def getResponse(request):
    method, url = parseRequest(request.decode())
    headers, code = generateHeaders(method, url)
    content_status = generateContentStatus(code)

    if content_status == 200:
        if method == 'GET':
             additional_header, r, body = getRequest.getContent(url, DIR)
             if not body == None:
                 return (headers + '\n' + body).encode()
             elif not (additional_header and r) == None:
                 return (headers + additional_header).encode() + r
        elif method == 'POST':
            data = postRequest.getData(request)
            POST = data
            print(POST)
            return (headers + '\n' + '<h1>Post request completed successfully!</h1>').encode()
    

    return (headers + '\n' + content_status).encode()