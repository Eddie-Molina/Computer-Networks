Eddie Molina



 To check whether the multi-threaded webserver works do the following steps:
	1. open a terminal
	2. change directory (cd) into the directory where the server.py file is
	3. run the server file as python3 server.py
	4. open a web browser (i.e google chrome)
	5. in the web browser type in localhost:8833/project1.html hello world should be displayed
	6. open a new tab and type in localhost:8833/project1.html hello world should be displayed again
	7. in the web browser type in localhost:8833/project this will display an error saying 404 file not found


To test the client do the following steps:
	1. open two terminals
	2. in one terminal change directory into the directory where the server.py file is
	3. run the server file as [ python3 server.py ] without the brackets
	4. in the other terminal change directory to where the client.py file is
	5. run the client file as [ python3 client.py localhost 8833 project1.html ] without the brackets


MacOS was used to compile the python files. The terminal and Google Chrome was used to test the python files.

Resources used in this project was:

Geek for Geeks
https://www.geeksforgeeks.org/socket-programming-multi-threading-python/

Stack Overflow was used for error resolve and debugging.

The textbook for the class, specifically chapter 2.7.2 Socket Programming With TCP was used.

The given skeleton code in python was also used for this project.


