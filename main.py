import socket
import config
import handlerRequest

IP_ADDRESS = config.get_ipAdress()
PORT = config.get_port()


def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #параметры
    server.bind((IP_ADDRESS, PORT))
    server.listen()

    while True:
        client_socket, addr = server.accept()
        request = client_socket.recv(2048)

        response = handlerRequest.getResponse(request)

        client_socket.sendall(response)
        client_socket.close()

if __name__ == '__main__':
    run()