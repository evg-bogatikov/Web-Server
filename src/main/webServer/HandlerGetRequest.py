class HandlerGetRequest:

    def __init__(self, handlerHeaders, DIR):
        self.DIR = DIR
        self.handlerHeaders = handlerHeaders

    def getContent(self, urn):
        formatUrl = urn.split('.')
        if formatUrl[formatUrl.__len__() - 1] == 'jpg' or formatUrl[formatUrl.__len__() - 1] == 'png' or formatUrl[
            formatUrl.__len__() - 1] == 'gif':
            body = self.pictureResponse(urn)
        else:
            body = self.readView(urn)
        return body


    def pictureResponse(self, urn):
        #открываем файл для чтения только в бинарном формате - 'rb'
        file = open('../resources/' + self.DIR + urn, 'rb')
        readFile = file.read()
        file.close()

        self.handlerHeaders.addResponseHeaders('Content-Length', readFile.__sizeof__().__str__())
        self.handlerHeaders.addResponseHeaders('Content-Type', 'image/gif')
        return readFile


    def readView(self, urn):
        with open('../resources/' + self.DIR + urn) as template:
            return template.read()
