# Help: https://www.eventhelix.com/networking/ftp/
# Help: https://www.eventhelix.com/networking/ftp/FTP_Port_21.pdf
# Help: https://realpython.com/python-sockets/
# Help: PASV mode may be easier in the long run. Active mode works
# Reading: https://unix.stackexchange.com/questions/93566/ls-command-in-ftp-not-working
# Reading: https://stackoverflow.com/questions/14498331/what-should-be-the-ftp-response-to-pasv-command

# import socket module
from socket import *
import sys  # In order to terminate the program




# Richard Done
def quitFTP(clientSocket):
    # Send QUIT command to server
    command = "QUIT\r\n"
    dataOut = command.encode("utf-8")
    clientSocket.sendall(dataOut)

    # Receive server response (should start with 221)
    dataIn = clientSocket.recv(1024)
    data = dataIn.decode("utf-8")

    print(data)

    # Close the control connection
    clientSocket.close()




def sendCommand(socket, command):
    dataOut = command.encode("utf-8")
    # Complete
    return data

def receiveData(clientSocket):
    dataIn = clientSocket.recv(1024)
    data = dataIn.decode("utf-8")
    return data


#Done Richard

# If you use passive mode you may want to use this method but you have to complete it
# You will not be penalized if you don't
def modePASV(clientSocket):
    command = "PASV\r\n"

    # Send PASV on control connection
    clientSocket.sendall(command.encode("utf-8"))

    # Read reply (should start with 227)
    data = receiveData(clientSocket)
    print(data)  # optional debug

    status = 0
    dataSocket = None

    if data.startswith("227"):
        status = 227

        # Extract numbers inside parentheses: (h1,h2,h3,h4,p1,p2)
        start = data.find("(")
        end = data.find(")", start + 1)
        if start == -1 or end == -1:
            return 0, None

        parts = data[start + 1:end].split(",")
        if len(parts) != 6:
            return 0, None

        h1, h2, h3, h4, p1, p2 = parts
        ip = f"{h1}.{h2}.{h3}.{h4}"
        port = int(p1) * 256 + int(p2)

        dataSocket = socket(AF_INET, SOCK_STREAM)
        dataSocket.connect((ip, port))

    return status, dataSocket




def main():
    # COMPLETE
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    clientSocket = socket(AF_INET, SOCK_STREAM)  # TCP socket

    # COMPLETE
    HOST =  # COMPLETE

    # COMPLETE

    dataIn = receiveData(clientSocket)
    print(dataIn)



# Done Richard
    status = 0
    if dataIn.startswith("220"):
        status = 220
        print("Sending username")
        # COMPLETE Richard Done
        command = "USER " + username + "\r\n"
        clientSocket.sendall(command.encode("utf-8"))
        dataIn = receiveData(clientSocket)
        print(dataIn)

    print("Sending password")
    if dataIn.startswith("331"):
        status = 331
        # COMPLETE
        command = "PASS " + password + "\r\n"
        clientSocket.sendall(command.encode("utf-8"))
        dataIn = receiveData(clientSocket)
        print(dataIn)

    if dataIn.startswith("230"):
        status = 230

    if status == 230:
        # It is your choice whether to use ACTIVE or PASV mode. In any event:
        # COMPLETE
        pasvStatus, dataSocket = modePASV(clientSocket)

        if pasvStatus == 227:
            # COMPLETE
            print("PASV mode enabled successfully.")
            print("Disconnecting...")

            # Close the DATA connection first
            if dataSocket is not None:
                dataSocket.close()

            # Properly close the CONTROL connection using QUIT
            quitFTP(clientSocket)

            sys.exit()  # Terminate the program
        else:
            print("Failed to enter PASV mode.")




main()
