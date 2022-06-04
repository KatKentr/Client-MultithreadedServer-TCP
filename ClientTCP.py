import socket
from utils import processInput

class ClientProtocol:

    def prepareRequest(self):

        steps=processInput()
        return str(steps)

    def processReply(self,theInput):

        try:
            theInput=float(theInput)
            print("Pi recieved from server: "+ str(theInput))
        except:
            print(theInput)


class ClientTCP:

    HOST="localhost"
    PORT=1234
    serverAdd=(HOST,PORT)
    EXIT="CLOSE"        #maybe not needed? we will see

    @staticmethod
    def main():

        dataSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        dataSocket.connect(ClientTCP.serverAdd)
        print("Connection to "+ ClientTCP.HOST+" established")

        app=ClientProtocol()
        outmsg=app.prepareRequest()
        dataSocket.sendall(outmsg.encode())   # send number of steps to server
        inmsg=dataSocket.recv(1024)            #recieve calculated Pi
        app.processReply(inmsg.decode())       #print result
        dataSocket.close()
        print("Data socket closed")

if __name__ == '__main__':
    ClientTCP.main()






