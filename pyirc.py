from socket import *

def hirc():
	username = input("username: ")
	ip = input("ip: ")
	port = input("port: ")


	s = socket(2, 1)
	try:
		s.bind((str(ip), int(port)))
		s.listen(10)
		print("listening on " + str(ip) + " through port " + str(port))
		c, addr = s.accept()
		print("connected to " + str(addr[0]) + " through port " + str(addr[1]))
		while True:
			message = input(str(username) + " #> ")
			c.sendall(bytes(username + " #> " + message, encoding = 'utf-8'))
			data = c.recv(5120)
			print(data.decode("utf-8"))
	except:
		print("could not connect or recv/send data to " + str(addr[0]) + " through port " + str(addr[1]))

	s.close()

def circ():
	username = input("username: ")
	ip = input("ip: ")
	port = input("port: ")

	s = socket(2, 1)
	try:
		s.connect((str(ip), int(port)))
		print("connected to " + str(ip) + " through port " + str(port))
		while True:
			data = s.recv(5120)
			print(data.decode("utf-8"))
			message = input(str(username) + " #> ")
			s.sendall(bytes(username + " #> " + message, encoding = 'utf-8'))
	except:
		print("could not connect or recv/send data to " + str(ip) + " through port " + str(port))
		
	s.close()

while True:
	choc = str(input("[1] Host\n[2] Connect\n[0] Exit\n"))
	if choc == '1':
		hirc()
	elif choc == '2':
		circ()
	elif choc == '0':
		exit(0)
	else:
		print("wrong input, try again")
