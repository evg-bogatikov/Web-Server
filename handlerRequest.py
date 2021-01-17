import getRequest
import handlerHeader
import postRequest

POST = {}


def generateContentStatus(code):
    if code == 404:
        return '<h1>404</h1><p>Not found</p>'
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    return 200


def getResponse(request, dir):
    method, url = handlerHeader.parseStatusRequest()
    status, code = handlerHeader.generateStatusCodeResponse(method, url, dir)
    content_status = generateContentStatus(code)
    print(handlerHeader.getItemRequestHeader('Connection'))
    if content_status == 200:
        if method == 'GET':
            additional_header, r, body = getRequest.getContent(url, dir)
            if not body == None:
                return (status + '\n' + body).encode()
            elif not (additional_header and r) == None:
                return (status + additional_header).encode() + r
        elif method == 'POST':
            data = postRequest.getData(request)
            POST = data
            print(POST)
            return (status + '\n' + '<h1>Post request completed successfully!</h1>').encode()

    return (status + '\n' + content_status).encode()
