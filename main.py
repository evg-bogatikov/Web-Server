import socket
import config
import handlerRequest
from threading import Thread

HOST = config.getHost()
DIR = config.getDir()
PORT = config.getPort()
BUFSIZE = config.getBufSize()


def listener(host, i, dir):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #параметры
    server.bind((host, PORT))
    server.listen()
    while True:
        client_socket, addr = server.accept()
        request = client_socket.recv(BUFSIZE)
        response = handlerRequest.getResponse(request, dir)
        print('Thread: '+ str(i))
        client_socket.sendall(response)
        client_socket.close()

def run():

    hostLength = config.getHostLength()
    for i in range(hostLength):
        newTh = Thread(target=listener, args=(HOST[i], i, DIR[i],))
        newTh.start()

if __name__ == '__main__':
    run()