import socket
import config
import HandlerRequest
import HandlerStatusCode
import HandlerHeaders
from threading import Thread


class Main:

    def __init__(self):
        self.handlerH = HandlerHeaders.HandlerHeaders()
        self.handlerS = HandlerStatusCode.HandlerStatusCode()
        self.handlerR = HandlerRequest.HandlerRequest(self.handlerH, self.handlerS)
        self.HOST = config.getHost()
        self.DIR = config.getDir()
        self.PORT = config.getPort()
        self.BUFSIZE = config.getBufSize()

    def listener(self, host, i, dir):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # параметры
        server.bind((host, self.PORT))
        server.listen()
        while True:
            client_socket, addr = server.accept()
            try:
                request = client_socket.recv(self.BUFSIZE)

                response = self.handlerR.getResponse(request, dir)
                print(f"Thread: {str(i)}  Host: {host} her directory: {dir}")
                client_socket.sendall(response)
            except:
                print('Double request or another unknown error')

            client_socket.close()

    def run(self):
        hostLength = len(self.HOST)

        for i in range(hostLength):
            newTh = Thread(target=self.listener, args=(self.HOST[i], i, self.DIR[i],))
            newTh.start()


if __name__ == '__main__':

    main = Main()
    main.run()
