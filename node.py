import socket
import sys
import threading
import thread
import time
import datetime
import random
from collections import deque


def server():
	global s_server, server_port, sock, server_ip, num_clients
	s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	server_port = 8000

	try: # setup server socket
		s_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s_server.bind((server_ip, int(server_port)))
	
	# if server setup fail
	except socket.error , msg:
		print '[[ Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1] + ' ]]'
		sys.exit()

	print 'Socket bind complete.'
	s_server.listen(10)
	print 'Socket listening..'

	while 1:
		conn, addr = s_server.accept()
		print 'Connected With '  + addr[0] + ':' + str(addr[1])
		thread.start_new_thread(clientThread, (conn, str(addr[1])))

		#keep track of the number of clients connected to server
		num_clients = num_clients + 1
	conn.close()
	s_server.close()

#Coordinator node
def coordinator():
	while(1):
		userInput = raw_input('>>> ');
		cmd = userInput.split(' ');
		if cmd[0] == "join" and cmd[1] != None:
		elif cmd[0] == "find" and cmd[1] != None and cmd[2] != None:
		elif cmd[0] == "leave" and cmd[1] != None:
		elif cmd[0] == "show" and cmd[1] != None:
		elif cmd[0] == "show" and cmd[1] == "all":
		else:
			print 'invalid Input'

thread.start_new_thread(coordinator,)
server()