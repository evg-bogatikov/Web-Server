import handlerGetRequest
import handlerPostRequest


class ControlRequest:

    def __init__(self, handlerH, handlerS):
        self.POST = {}
        self.handlerHeaders = handlerH
        self.handlerRequestLine = handlerS

    def decodeRequest(self, request):
        request = request.decode()
        request = list(request.split('\n'))
        return request

    def getResponse(self, request, dir):
        request = self.decodeRequest(request)

        method, url = self.handlerRequestLine.parseStatusRequest(request)
        status, code = self.handlerRequestLine.generateResponseLine(method, url, dir)
        content_status = self.handlerRequestLine.generateContentStatus(code)

        handlerGetR = handlerGetRequest.HandlerGetRequest(self.handlerHeaders, dir)
        handlerPostR = handlerPostRequest.HandlerPostRequest()

        if content_status == 200:
            if method == 'GET':
                r, body = handlerGetR.getContent(url)
                responseHeaders = self.handlerHeaders.getResponseHeaders()
                self.handlerHeaders.clearResponseHeaders()
                if not body == None:
                    a = (status + '\n\n' + body).encode()
                    return (status + '\n\n' + body).encode()
                elif not (responseHeaders and r) == None:
                    return (status + responseHeaders).encode() + r
            elif method == 'POST':
                data = handlerPostR.getData(request)
                POST = data
                return (status + '\n' + '<h1>Post request completed successfully!</h1>').encode()

        return (status + '\n' + content_status).encode()
