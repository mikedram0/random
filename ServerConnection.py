import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)

while True:
	print('\n')
	server=input("Server : ")
	port =input("Port : ")
	request = "GET / HTTP/1.1\nHost: "+server+"\n\n"
	s.connect((server,int(port)))
	s.send(request.encode())
	result = s.recv(2**16)
	print(result)