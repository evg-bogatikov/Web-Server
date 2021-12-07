import HandlerGetRequest
import HandlerPostRequest


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

        handlerGetR = HandlerGetRequest.HandlerGetRequest(self.handlerHeaders, dir)
        handlerPostR = HandlerPostRequest.HandlerPostRequest()

        if content_status == 200:
            if method == 'GET':
                body = handlerGetR.getContent(url)
                responseHeaders = self.handlerHeaders.getResponseHeaders()
                self.handlerHeaders.clearResponseHeaders()
                if not responseHeaders == '\n' and not body == None:
                    return (status + responseHeaders).encode() + body
                elif not body == None:
                    return (status + '\n\n' + body).encode()
            elif method == 'POST':
                data = handlerPostR.getData(request)
                return (status + '\n' + '<h1>Post request completed successfully! Your data: <br/>'+ data.__str__() +'</h1>').encode()

        return (status + '\n' + content_status).encode()
