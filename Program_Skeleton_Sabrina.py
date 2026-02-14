from socket import *
import sys 

def quitFTP(clientSocket):
    command = "QUIT\r\n"
    data = sendCommand(clientSocket, command)
    print(data)
    return data

def sendCommand(socket, command):
    dataOut = command.encode("utf-8")
    # Complete
    return data

def receiveData(clientSocket):
    dataIn = clientSocket.recv(1024)
    data = dataIn.decode("utf-8")
    return data


def modePASV(clientSocket):
    command = "PASV" + "\r\n"
    # Complete
    status = 0
    if data.startswith(""):
        status = 227
        # Complete
        dataSocket.connect((ip, port))
        
    return status, dataSocket

def changeDirectory(clientSocket, remote_dir):
    command = f"CWD {remote_dir}\r\n"
    data = sendCommand(clientSocket, command)
    print(data)
    return data

def putFile(clientSocket, local_file):
    # Enter passive mode
    pasvStatus, dataSocket = modePASV(clientSocket)
    
    if pasvStatus == 227:
        # Send STOR command
        command = f"STOR {local_file}\r\n"
        response = sendCommand(clientSocket, command)
        print(response)
        
        if response.startswith("150"):
            try:
                with open(local_file, 'rb') as f:
                    file_data = f.read()
                    dataSocket.sendall(file_data)
                dataSocket.close()
                
                final_response = clientSocket.recv(1024).decode("utf-8")
                print(final_response)
                
                if final_response.startswith("226"):
                    print(f"File '{local_file}' uploaded successfully")
                    
            except FileNotFoundError:
                print(f"Error: Local file '{local_file}' not found")
                dataSocket.close()
        else:
            dataSocket.close()
    else:
        print("Failed to enter passive mode")

def deleteFile(clientSocket, remote_file):
    command = f"DELE {remote_file}\r\n"
    data = sendCommand(clientSocket, command)
    print(data)
    return data
    
    
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
    
    print("Disconnecting...")
    

    clientSocket.close()
    dataSocket.close()
    
    sys.exit()#Terminate the program after sending the corresponding data

main()
