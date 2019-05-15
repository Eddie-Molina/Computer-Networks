"""
	Eddie Molina
	1001088363
	Project 1
"""
#import socket module
from socket import *
from _thread import *
import threading
import http.server
from socketserver import ThreadingMixIn

def threaded(connectionSocket):
	try:
		message = connectionSocket.recv(1024)
		if message:
			filename = message.split()[1] # extract filename "project1.html"
			f = open(filename[1:])
			outPutData = f.read() 
			#Send one HTTP header line into socket
			connectionSocket.send( bytes("\r\nHTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n", "UTF-8") )
			print("\n"+outPutData)
			print("\nClient IP Address: \t" + connectionSocket.getsockname()[0])
			print("Host Name: \t\t" + serverName)
			print("Server Port Number: \t" + str(serverPort))
			print("Peer Name: \t\t" + str(addr[0]) + str(addr[1]))
			print("Socket Family: \t\t" + str(connectionSocket.family))
			print("Type: \t\t\t" + str(connectionSocket.type))
			print("Protocol: \t\t" + str(connectionSocket.proto)+"\n")

			#Send the content of the requested file to the client
			for i in range(0, len(outPutData)):
				connectionSocket.send(bytes(outPutData[i], "UTF-8"))
			connectionSocket.close()

	except IOError:
		#Send response message for file not found
		connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n", "UTF-8"))
		connectionSocket.send(bytes("<html><head></head><body><h1><center>404 Not Found</center></h1></body></html>\r\n", "UTF-8"))
		#Close client socket
		connectionSocket.close()

serverName = "localhost"	
serverPort = 8833
#Prepare a server socket	
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
	print ("Ready to serve...")
	(connectionSocket, addr) = serverSocket.accept() # Establish the connection
	start_new_thread(threaded, (connectionSocket,))  # Function for threaded server
serverSocket.close()

