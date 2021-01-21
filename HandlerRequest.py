import HandlerGetRequest
import HandlerPostRequest


class HandlerRequest:

    def __init__(self, handlerH, handlerS):
        self.POST = {}
        self.handlerHeaders = handlerH
        self.handlerStatusCode = handlerS

    def parseRequest(self, request):
        request = request.decode()
        request = list(request.split('\n'))
        return request

    def getResponse(self, request, dir):
        request = self.parseRequest(request)

        method, url = self.handlerStatusCode.parseStatusRequest(request)
        status, code = self.handlerStatusCode.generateStatusCodeResponse(method, url, dir)
        content_status = self.handlerStatusCode.generateContentStatus(code)

        handlerGetR = HandlerGetRequest.HandlerGetRequest(self.handlerHeaders, dir)
        handlerPostR = HandlerPostRequest.HandlerPostRequest()

        if content_status == 200:
            if method == 'GET':
                r, body = handlerGetR.getContent(url)
                responseHeaders = self.handlerHeaders.getResponseHeaders()
                self.handlerHeaders.clearResponseHeaders()
                if not body == None:
                    a = (status + '\n\n' + body).encode()
                    print(type(a))
                    return (status + '\n\n' + body).encode()
                elif not (responseHeaders and r) == None:
                    return (status + responseHeaders).encode() + r
            elif method == 'POST':
                data = handlerPostR.getData(request)
                POST = data
                print(POST)
                return (status + '\n' + '<h1>Post request completed successfully!</h1>').encode()

        return (status + '\n' + content_status).encode()
