import handlerHeader

def getContent(url, DIR):
    formatUrl = url.split('.')
    if formatUrl[formatUrl.__len__() - 1] == 'jpg' or formatUrl[formatUrl.__len__() - 1] == 'png' or formatUrl[
        formatUrl.__len__() - 1] == 'gif':
        r = pictureResponse(url, DIR)
        body = None

        # print(r)
        return r, None
    else:
        body = readView(url, DIR)
        # print(body)
        return None, body


def pictureResponse(url, DIR):
    # rb - Opens a file for reading only in binary format.
    f = open(DIR + url, 'rb')
    r = f.read()
    #additional_header = 'Content-Length: ' + r.__sizeof__().__str__() + '\nContent-Type: image/gif\n\n'
    handlerHeader.addResponseHeaders('Content-Length', r.__sizeof__().__str__())
    handlerHeader.addResponseHeaders('Content-Type', 'image/gif')
    handlerHeader.getResponseHeaders()
    f.close()
    return r


def readView(url, DIR):
    with open(DIR + url) as template:
        return template.read()
