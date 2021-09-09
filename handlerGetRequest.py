class HandlerGetRequest:

    def __init__(self, handlerHeaders, DIR):
        self.DIR = DIR
        self.handlerHeaders = handlerHeaders


    def getContent(self, url):
        formatUrl = url.split('.')
        if formatUrl[formatUrl.__len__() - 1] == 'jpg' or formatUrl[formatUrl.__len__() - 1] == 'png' or formatUrl[
            formatUrl.__len__() - 1] == 'gif':
            r = self.pictureResponse(url)
            body = None

            print(type(r))
            return r, None
        else:
            body = self.readView(url)
            # print(body)

            return None, body


    def pictureResponse(self, url):
        # rb - Opens a file for reading only in binary format.
        f = open(self.DIR + url, 'rb')
        r = f.read()
        #additional_header = 'Content-Length: ' + r.__sizeof__().__str__() + '\nContent-Type: image/gif\n\n'
        self.handlerHeaders.addResponseHeaders('Content-Length', r.__sizeof__().__str__())
        self.handlerHeaders.addResponseHeaders('Content-Type', 'image/gif')
        self.handlerHeaders.getResponseHeaders()
        f.close()
        return r


    def readView(self, url):
        with open(self.DIR + url) as template:
            return template.read()
