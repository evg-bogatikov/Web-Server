class HandlerHeaders:
    def __init__(self):
        self.requestHeaders = {}
        self.responseHeaders = {}

    def parseHeader(self, request):
        # request = request.decode()
        # request = list(request.split('\n'))

        request.pop(0)

        for i in request:
            if i == '\r' or '':
                break

            i = i.replace('\r', '')
            i = i.split(':', maxsplit=1)

            self.requestHeaders[i[0]] = i[1]

    def getItemRequestHeader(self, key):
        return key + ':' + self.requestHeaders.get(key)

    def getAllRequestHearder(self):
        return self.requestHeaders.items()

    def addResponseHeaders(self, nameHeader, dataHeader):
        self.responseHeaders[nameHeader] = dataHeader

    def clearResponseHeaders(self):
        self.responseHeaders.clear()

    def getResponseHeaders(self):
        result = ''
        for i in self.responseHeaders:
            result += i + ': ' + self.responseHeaders[i] + '\n'

        result += '\n'
        return result
