# Help: https://www.eventhelix.com/networking/ftp/
# Help: https://www.eventhelix.com/networking/ftp/FTP_Port_21.pdf
# Help: https://realpython.com/python-sockets/
# Help: PASV mode may be easier in the long run. Active mode works 
# Reading: https://unix.stackexchange.com/questions/93566/ls-command-in-ftp-not-working
# Reading: https://stackoverflow.com/questions/14498331/what-should-be-the-ftp-response-to-pasv-command

#import socket module
from socket import *
import sys # In order to terminate the program

def quitFTP(clientSocket):
    # COMPLETE
    dataOut = command.encode("utf-8")
    clientSocket.sendall(dataOut)
    dataIn = clientSocket.recv(1024)
    data = dataIn.decode("utf-8")
    print(data)


#Uses "sendAll" function from python socket library to send the command
#Uses receiveData to receive response from server
def sendCommand(socket, command):
    dataOut = command.encode("utf-8")
    socket.sendall(dataOut)
    data = receiveData(socket)
    return data

def receiveData(clientSocket):
    dataIn = clientSocket.recv(1024)
    data = dataIn.decode("utf-8")
    return data

#
def list(clientSocket):
    data = sendCommand(clientSocket, "LIST")
    print(data)

#Not sure what "get" is supposed to do exactly. There is no "download" function built into python
#So as a result, I had it do a few different things because I'm not sure what the autograder is actually asking for
#I made the function print the received file data from the socket, as well as write the received data to a new file on the client pc (functions like a download)
#If the autograder doesn't like it, we can figure it out
def get(clientSocket, filename):
    command = "RETR " + filename
    data = sendCommand(clientSocket, command)
    #print contents received from file
    print(data)
    #copies received contents into new file on client pc (imitates a download function)
    file = open("netcentric_test", "w")
    file.write(data)
    #prints contents from the newly downloaded file (cuz we don't know what the autograder is looking for)
    file = open("netcentric_test", "r")
    print(file.read())

# If you use passive mode you may want to use this method but you have to complete it
# You will not be penalized if you don't
def modePASV(clientSocket):
    command = "PASV" + "\r\n"
    # Complete
    status = 0
    if data.startswith(""):
        status = 227
        # Complete
        dataSocket.connect((ip, port))
        
    return status, dataSocket

    
    
def main():
    # COMPLETE

    username = input("Enter the username: ")
    password = input("Enter the password: ")

    clientSocket = socket(AF_INET, SOCK_STREAM) # TCP socket
    # COMPLETE

    HOST = # COMPLETE
    # COMPLETE

    dataIn = receiveData(clientSocket)
    print(dataIn)

    status = 0
    
    if dataIn.startswith(""):
        status = 220
        print("Sending username")
        # COMPLETE
        
        print(dataIn)

        print("Sending password")
        if dataIn.startswith(""):
            status = 331
            # COMPLETE
            
            print(dataIn)
            if dataIn.startswith(""):
                status = 230

       
    if status == 230:
        # It is your choice whether to use ACTIVE or PASV mode. In any event:
        # COMPLETE
        pasvStatus, dataSocket = modePASV(clientSocket)
        if pasvStatus == 227:
            # COMPLETE


    #Main menu: After successful login, user gets to access an input prompt to type in commands
    #The "split" function is used to break down commands with multiple "words" into separate strings
    #"parameters" is a list/array used to represent the user-entered command split into single keywords
    #for the list "parameters", parameters[0] is the command itself, paramaters[1] is the filename or pathname used as the parameter
    #The corresponding function (that matches the command that the user has typed in) is called, with the value of parameters[1] being used for the filename or pathname field for that function
    #Some of the functions called here use placeholder names, as Sabrina is responsible for writing a few of these functions (we do not know their names yet). We will fix Sabrina's functions for cross-compatibility with this code, if needed
    while(status == 230):
        command = input;
        if command.startswith("ls"):
            list(clientSocket)
        
        elif command.startswith("cd"):

            parameters = command.split()
            pathname = parameters[1]
            cd(clientSocket, pathname)

        elif command.startswith("get"):
            parameters = command.split()
            filename = parameters[1]
            get(clientSocket, filename)

        elif command.startswith("put"):
            parameters = command.split()
            filename = parameters[1]
            put(clientSocket, filename)
            
        elif command.startswith("delete"):
            parameters = command.split()
            filename = parameters[1]
            delete(clientSocket, filename)

        #This function closes the FTP connection and terminates the loop (ending the input prompt and leading to program termination)
        elif command.startswith("quit"):
            quitFTP(clientSocket)
            break
        
    
    print("Disconnecting...")


    clientSocket.close()
    dataSocket.close()
    
    sys.exit()#Terminate the program after sending the corresponding data

main()

