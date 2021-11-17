import unittest
from main.webServer.handlerRequestAndResponseLine import  HandlerRequestAndResponseLine

class TestHandlerRequestLine(unittest.TestCase):

    handlerRequestLine = HandlerRequestAndResponseLine()

    def test_parseStatusRequest(self):
        request = ["GET /blog.html HTTP/1.1\r", "Content-Type: text/xml"]


        result = ("GET", "/blog.html")

        self.assertEqual(self.handlerRequestLine.parseStatusRequest(request), result)

    def test_generateResponseLine(self):
        method = 'GET'
        urn = '/blog.html'
        dir = '../resources/mock_templates2'

        result = ('HTTP/1.1 200 OK\n', 200)

        self.assertEqual(self.handlerRequestLine.generateResponseLine(method, urn, dir), result)

    def test_generateContentStatus(self):
        code = 404
        result = '<h1>404</h1><p>Not found</p>'
        self.assertEqual(self.handlerRequestLine.generateContentStatus(code), result)