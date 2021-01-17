import os

statusCode = str
headers = {}


def parseHeader(request):
    request = request.decode()
    request = list(request.split('\n'))
    global statusCode
    statusCode = str(request[0])
    request.pop(0)

    for i in request:
        if i == '\r' or '':
            break

        i = i.replace('\r', '')
        i = i.split(':', maxsplit=1)

        headers[i[0]] = i[1]


def getItemRequestHeader(key):
    return key + ':' + headers.get(key)


def getAllRequestHearder():
    return headers.items()


def parseStatusRequest():
    parsed = statusCode.split(' ')
    method = parsed[0]
    url = parsed[1]
    return (method, url)


def generateStatusCodeResponse(method, url, dir):
    if not method == 'GET' and not method == 'POST':
        return ('HTTP/1.1 405 Method not allowed\n', 405)

    # os.path.exists - возвращает True, если path указывает на существующий путь или дескриптор открытого файла
    # os.path.isfile - является ли путь файлом

    if os.path.exists(dir + url) == False or os.path.isfile(dir + url) == False:
        return ('HTTP/1.1 404 Not found\n', 404)

    return ('HTTP/1.1 200 OK\n', 200)

