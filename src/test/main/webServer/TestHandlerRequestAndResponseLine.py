import unittest
from main.webServer.HandlerRequestAndResponseLine import HandlerRequestAndResponseLine


class testHandlerRequestAndResponseLine(unittest.TestCase):
    handlerRequestAndResponseLine = HandlerRequestAndResponseLine()

    def testParseStatusRequestNotEmptyRequest(self):
        request = ['GET /test1/index.html HTTP/1.1']

        result = self.handlerRequestAndResponseLine.parseStatusRequest(request)

        self.assertEqual(('GET', '/test1/index.html'), result)

    def testParseStatusRequestEmptyRequest(self):
        request = ['']

        self.assertRaises(Exception, self.handlerRequestAndResponseLine.parseStatusRequest, request)

    def testGenerateContentStatusCode200(self):
        code = 200

        result = self.handlerRequestAndResponseLine.generateContentStatus(code)

        self.assertEqual(200, result)

    def testGenerateContentStatusCode404(self):
        code = 404

        result = self.handlerRequestAndResponseLine.generateContentStatus(code)

        self.assertEqual('<h1>404</h1><p>Not found</p>', result)

    def testGenerateContentStatusCode405(self):
        code = 405

        result = self.handlerRequestAndResponseLine.generateContentStatus(code)

        self.assertEqual('<h1>405</h1><p>Method not allowed</p>', result)

    def testGenerateResponseLineCorrectMethodAndUrnAndDir(self):
        method = "GET"
        urn = '/test1/index.html'
        dir = 'mock_templates2'

        result = self.handlerRequestAndResponseLine.generateResponseLine(method, urn, dir)

        self.assertEqual(('HTTP/1.1 200 OK\n', 200), result)

    def testGenerateResponseLineIncorrectUrn(self):
        method = "GET"
        urn = '/test/index.html'
        dir = 'mock_templates2'

        result = self.handlerRequestAndResponseLine.generateResponseLine(method, urn, dir)

        self.assertEqual(('HTTP/1.1 404 Not found\n', 404), result)

    def testGenerateResponseLineIncorrectMethodHead(self):
        method = "HEAD"
        urn = '/test/index.html'
        dir = 'mock_templates2'

        result = self.handlerRequestAndResponseLine.generateResponseLine(method, urn, dir)

        self.assertEqual(('HTTP/1.1 405 Method not allowed\n', 405), result)
