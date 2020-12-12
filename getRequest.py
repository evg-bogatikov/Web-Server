def getContent(url, DIR):
    formatUrl = url.split('.')
    if formatUrl[formatUrl.__len__() - 1] == 'jpg' or formatUrl[formatUrl.__len__() - 1] == 'png' or formatUrl[
        formatUrl.__len__() - 1] == 'gif':
        additional_header, r = pictureResponse(url, DIR)
        body = None
        return additional_header, r, None
    else:
        body = readView(url, DIR)
        return None, None, body


def pictureResponse(url, DIR):
    #rb - Opens a file for reading only in binary format.
    f = open(DIR + url, 'rb')
    r = f.read()
    additional_header = 'Content-Length: ' + r.__sizeof__().__str__() + '\nContent-Type: image/gif\n\n'
    f.close()
    return additional_header, r

def readView(url, DIR):
    with open(DIR + url) as template:
       return template.read()