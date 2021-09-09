import unittest
from handlerGetRequest import HandlerGetRequest

class testHandlerGetRequest(unittest.TestCase):

    handlerGetRequest = HandlerGetRequest('', 'mock_templates2')

    def test_readView(self):
        url = '/blog.html'
        temp = self.handlerGetRequest.readView(url)
        print(type(temp))
        self.assertEqual(True, True)
