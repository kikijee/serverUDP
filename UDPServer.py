from socket import *
import pickle
import os

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
        self.TEXT = ""
        self.HTTP_INCLUDED_OBJECT = ""

serverPort = 18111
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

def send_syn_ack(address):
    serverDatagram = UDP()
    serverDatagram.UDP_ACK_FLAG = 1
    serverDatagram.UDP_SYN_FLAG = 1
    data_string = pickle.dumps(serverDatagram)
    serverSocket.sendto(data_string,address) # sends udpclient class

def send_html(address, dataObj):
    arr = []
    print(dataObj.HTTP_REQUEST_PATH)
    for root, dirs, files in os.walk(r'\Users\cam00\Desktop\python\serverUDP\attachments'):
        if dataObj.HTTP_REQUEST_PATH in files:
            with open(os.path.join(root,dataObj.HTTP_REQUEST_PATH)) as text:
                arr = text.readlines() 
    serverDatagram = UDP()
    if not arr: serverDatagram.HTTP_RESPONSE_STATUS_CODE = 404
    else:
        serverDatagram.HTTP_RESPONSE_STATUS_CODE = 202
        serverDatagram.TEXT = arr[0]
        if len(arr) == 2: serverDatagram.HTTP_INCLUDED_OBJECT = arr[1]
    data_string = pickle.dumps(serverDatagram)
    serverSocket.sendto(data_string,address) # sends udpclient class

def send_FIN_ACK(address):
    serverDatagram = UDP()
    serverDatagram.UDP_ACK_FLAG = 1
    serverDatagram.UDP_FIN_FLAG = 1
    data_string = pickle.dumps(serverDatagram)
    serverSocket.sendto(data_string,address) # sends udpclient class



if __name__ == '__main__':

    print ('The server is ready to receive')
    while 1:

        dataGramE, clientAddress = serverSocket.recvfrom(2048)
        dataGram = pickle.loads(dataGramE)
        
        if(dataGram.PAYLOAD_LENGTH and dataGram.UDP_SYN_FLAG == 1):
            print("recieved SYN")
            send_syn_ack(clientAddress)
            print("sent SYN & ACK")

        elif(dataGram.UDP_ACK_FLAG == 1):
            print("recieved ACK")

        elif(dataGram.HTTP_GET_REQUEST == 1):
            print("recieved HTTP REQ")
            send_html(clientAddress,dataGram)
            print("sent HTTP RES")

        elif(dataGram.UDP_FIN_FLAG == 1):
            print("recieved FIN")
            send_FIN_ACK(clientAddress)
            print("sent FIN & ACK")
            



