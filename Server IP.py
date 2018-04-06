import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s,"\n")
history=[]
c=""
e=True

while (e==True):
	c=input("\nCOMMAND>>>")
	if(c=="server ip"):
		print("\n")
		server=input("Server : ")
		server_ip=socket.gethostbyname(server)
		history.append(server)
		print(server_ip)
	elif(c=="history"):
		print("\n")
		print(history)
	elif(c=="exit"):
		e=False
	elif(c=="help"):
		print("<<server ip>>\n<<history>>\n<<exit>>\n<<help>>")
