"""
	Eddie Molina
	1001088363
	Project 1
"""
from socket import *
from sys import *
from time import *

start = clock()
serverName = argv[1]		# localhost
serverPort = int(argv[2])	# 8823
filename = argv[3]			# project1.html
clientSocket = socket(AF_INET, SOCK_STREAM) # create socket
clientSocket.connect((serverName, serverPort))  
message = "GET /" + filename
clientSocket.send(bytes(message, "UTF-8"))
while True:		
		data = clientSocket.recv(1024)
		message += data.decode('ascii')	 # ensure all data in file is stored in message variable	
		if not data:  
			stop = clock()
			rtt = (stop - start) * 1000
			rtt = round(rtt,4)
			print(message)
			print("\nRTT:                 " + str(rtt) + "ms")  
			print("Host Name:           " + serverName)
			print("Server Port Number:  " + str(serverPort))
			print("Peer Name:           " + clientSocket.getsockname()[0])
			print("Socket Family:       " + str(clientSocket.family))
			print("Type:                " + str(clientSocket.type))
			print("Protocol             " + str(clientSocket.proto))
			print("Successfully received the file")
			break
print("\nSocket Closed!\n")
clientSocket.close()