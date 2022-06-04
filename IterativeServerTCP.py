import socket
import NumIntPar

class ServerProtocol:

    def processRequest(self, inputSteps):

        print("Recieved message from client: " + inputSteps)

        inputSteps=int(inputSteps)

        # sum = 0                       #pi computation (sequential)
        # step = 1.0 / inputSteps
        #
        # for i in range(inputSteps):
        #       x = (i + 0.5) * step
        #       sum += 4.0 / (1.0 + x**2)
        #
        # pi = sum * step
        #
        # return pi

        numThreads=4               #number of threads

        object=NumIntPar.calcPiInThreads()        #create an instance of the class calcPiInThreads
        pi=object.calcPi(inputSteps,numThreads)   #invoke method for parallel calculation

        return pi


class ServerTCP:
    #Server address
    PORT=1234
    serverAdd=("localhost",PORT)

    @staticmethod
    def main():

        connectionSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connectionSocket.bind(ServerTCP.serverAdd)
        connectionSocket.listen(10)

        while True:

            print("Server is listening to port: " + str(ServerTCP.PORT))

            conn, add = connectionSocket.accept()
            print("Received request from " + str(add))

            inmsg = conn.recv(1024)

            app = ServerProtocol()
            outmsg = app.processRequest(inmsg.decode())
            conn.sendall(str(outmsg).encode())

        conn.close()
        print("Data socket closed")

if __name__ == '__main__':
    ServerTCP.main()
