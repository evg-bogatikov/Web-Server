import unittest
from main.webServer.HandlerGetRequest import HandlerGetRequest
from main.webServer.HandlerHeaders import HandlerHeaders


class testHandlerGetRequest(unittest.TestCase):

    handlerGetRequest = HandlerGetRequest(HandlerHeaders(), 'mock_templates2')

    def testGetContentHtmlFile(self):
        urn = '/test1/index.html'

        with open('../resources/mock_templates2' + urn) as template:
            mockContent = template.read()

        content = self.handlerGetRequest.getContent(urn)

        self.assertEqual(mockContent, content)

    def testGetContentPngFile(self):
        urn = '/test1/op.png'

        file = open('../resources/mock_templates2' + urn, 'rb')
        mockContent = file.read()
        file.close()

        content = self.handlerGetRequest.getContent(urn)

        self.assertEqual(mockContent, content)

    def testGetContentGifFile(self):
        urn = '/test1/op.png'

        file = open('../resources/mock_templates2' + urn, 'rb')
        mockContent = file.read()
        file.close()

        content = self.handlerGetRequest.getContent(urn)

        self.assertEqual(mockContent, content)

    def testGetContentJpgFile(self):
        urn = '/squirrel.jpg'

        file = open('../resources/mock_templates2' + urn, 'rb')
        mockContent = file.read()
        file.close()

        content = self.handlerGetRequest.getContent(urn)

        self.assertEqual(mockContent, content)

    def testGetContentErrorUrn(self):
        urn = '/test/safwafwa'
        self.assertRaises(Exception, self.handlerGetRequest.getContent, urn)


    def testGetContentEmptyUrn(self):
        urn = ''

        self.assertRaises(Exception, self.handlerGetRequest.getContent, urn)

