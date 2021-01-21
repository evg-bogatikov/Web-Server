import os


class HandlerStatusCode:

    def parseStatusRequest(self, request):
        statusCode = request[0]
        parsed = statusCode.split(' ')
        method = parsed[0]
        url = parsed[1]
        print(method)
        return (method, url)

    def generateContentStatus(self, code):
        if code == 404:
            return '<h1>404</h1><p>Not found</p>'
        if code == 405:
            return '<h1>405</h1><p>Method not allowed</p>'
        return 200

    def generateStatusCodeResponse(self, method, url, dir):
        if not method == 'GET' and not method == 'POST':
            return ('HTTP/1.1 405 Method not allowed\n', 405)

        # os.path.exists - возвращает True, если path указывает на существующий путь или дескриптор открытого файла
        # os.path.isfile - является ли путь файлом

        if os.path.exists(dir + url) == False or os.path.isfile(dir + url) == False:
            return ('HTTP/1.1 404 Not found\n', 404)

        return ('HTTP/1.1 200 OK\n', 200)
