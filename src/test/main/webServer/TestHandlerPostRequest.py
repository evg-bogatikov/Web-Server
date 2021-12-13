import unittest
from main.webServer.HandlerPostRequest import HandlerPostRequest

class MyTestCase(unittest.TestCase):

    handlerPostRequest = HandlerPostRequest()

    def test_getData(self):
        request = ['Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7\r', 'Cookie: PGADMIN_LANGUAGE=ru; PGADMIN_INT_KEY=390b4398-ace6-4244-98b9-9fe30c0d68ba\r', '\r', 'data1=desc1&data2=desc2']

        result = {'data1': 'desc1', 'data2': 'desc2'}

        self.assertEqual(self.handlerPostRequest.getData(request), result)


