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

def send_ack(address):
    serverDatagram = UDP()
    serverDatagram.UDP_ACK_FLAG = 1
    data_string = pickle.dumps(serverDatagram)
    serverSocket.sendto(data_string,address) # sends udpclient class

if __name__ == '__main__':

    serverPort = 18111
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))

    print ('The server is ready to receive')
    while 1:

        dataGramE, clientAddress = serverSocket.recvfrom(2048)
        dataGram = pickle.loads(dataGramE)
        
        if(dataGram.PAYLOAD_LENGTH and dataGram.UDP_SYN_FLAG == 1):
            print("recieved SYN")
            send_ack(clientAddress)
            print("send ACK")


