import socket

host = socket.gethostname()
port = 2929

# AF_INET = IPv4
# SOCK_STREAM = TCP Connecion
sock_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_.bind((host,port))

# incoming conncetion
sock_.listen(1)

print("\nServer started...\n")

# accept connection from client
conn,addr = sock_.accept()

print("Connection established with: ", str(addr))

message = "\nThank you for connecting" + str(addr)
conn.send(message.encode("ascii"))
conn.close()
