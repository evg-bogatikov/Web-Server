import socket
from config import Config
from handlerHeaders import HandlerHeaders
from controlRequest import ControlRequest
from handlerRequestAndResponseLine import HandlerRequestAndResponseLine
from threading import Thread

class Main(object):

    def __init__(self, handlerR, config):
        self.handlerR = handlerR
        self.HOST = config.getHost()
        self.DIR = config.getDir()
        self.PORT = config.getPort()
        self.BUFSIZE = config.getBufSize()

    def listener(self, host, i, dir):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #параметры
        server.bind((host, self.PORT))
        server.listen()

        while True:
            client_socket, addr = server.accept()
            try:
                request = client_socket.recv(self.BUFSIZE)
                # print(''.join([chr(x) for x in request]))
                response = self.handlerR.getResponse(request, dir)
                print(f"Thread: {str(i)}  Host: {host} her directory: {dir}")
                client_socket.sendall(response)
            except socket.error as e:
                print(e)

            client_socket.close()




    def createServer(self):
        hostLength = len(self.HOST)

        for i in range(hostLength):
            newTh = Thread(target=self.listener, args=(self.HOST[i], i, self.DIR[i],))
            newTh.start()


if __name__ == '__main__':
    handlerH = HandlerHeaders()
    handlerS = HandlerRequestAndResponseLine()
    handlerR = ControlRequest(handlerH, handlerS)
    config = Config()
    main = Main(handlerR, config)
    main.createServer()
