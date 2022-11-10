from socket import *
import pickle
class UDP:
    def __init__ (self):
        self.PAYLOAD_LENGTH = 0
        self.UDP_SYN_FLAG = 0
        self.UDP_ACK_FLAG = 0
        self.UDP_FIN_FLAG = 0
        self.HTTP_GET_REQUEST = 0
        self.HTTP_RESPONSE_STATUS_CODE = 0 
        self.HTTP_CLIENT_VERSION = 0
        self.HTTP_REQUEST_PATH = "" # X length = payload length
        self.HTTP_INCLUDED_OBJECT = 0


serverPort = 18111
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ('The server is ready to receive')
while 1:
    transactionE, clientAddress = serverSocket.recvfrom(2048)
    #modifiedMessage = message.decode().upper()
    #serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    data_variable = pickle.loads(transactionE)
    print(data_variable.UDP_SYN_FLAG)
    '''
    message = input('message: ')
    serverSocket.sendto(message.encode(),clientAddress)
    modifiedMessage, serverAddress = serverSocket.recvfrom(2048)
    print (modifiedMessage.decode())
    '''