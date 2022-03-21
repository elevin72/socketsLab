from socket import socket, AF_INET, SOCK_STREAM


def main():
    serverName = 'localhost'
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedMessage = clientSocket.recv(1024)
    print(f"From server: `{modifiedMessage.decode()}`")
    clientSocket.close()


if __name__ == "__main__":
    main()



