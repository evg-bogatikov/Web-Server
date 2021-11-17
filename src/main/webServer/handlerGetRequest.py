class HandlerGetRequest:

    def __init__(self, handlerHeaders, DIR):
        self.DIR = DIR
        self.handlerHeaders = handlerHeaders


    def getContent(self, urn):
        urnArray = urn.split('.')
        formatFile = urnArray[urnArray.__len__() - 1]
        if formatFile == 'jpg' or formatFile == 'png' or formatFile == 'gif':
            r = self.pictureResponse(urn)
            body = None
            return r, None
        else:
            body = self.readView(urn)
            print("Body" + type(body) + body)
            return None, body


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
