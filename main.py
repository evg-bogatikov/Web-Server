import socket
import config
import handlerRequest
from threading import Thread
import handlerHeader

HOST = config.getHost()
DIR = config.getDir()
PORT = config.getPort()
BUFSIZE = config.getBufSize()


def listener(host, i, dir):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # параметры
    server.bind((host, PORT))
    server.listen()
    while True:
        client_socket, addr = server.accept()
        try:
            request = client_socket.recv(BUFSIZE)
            handlerHeader.parseHeader(request)
            response = handlerRequest.getResponse(request, dir)
            print(f"Thread: {str(i)}  Host: {host} her directory: {dir}")
            client_socket.sendall(response)
        except:
            print('Double request or another unknown error')

        client_socket.close()


def run():
    hostLength = len(HOST)

    for i in range(hostLength):
        newTh = Thread(target=listener, args=(HOST[i], i, DIR[i],))
        newTh.start()


if __name__ == '__main__':
    run()
