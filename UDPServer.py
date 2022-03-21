from socket import socket, AF_INET, SOCK_DGRAM

def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print(" The server is ready to recieve")

    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print(f"Server recieved `{message.decode()}`")
        modifiedMessage = message.decode().upper()
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)


if __name__ == "__main__":
    main()


