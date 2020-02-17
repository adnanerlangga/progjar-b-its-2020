import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 31000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it

    while True:
        data = connection.recv(32)
        if data:
            file_name = data.decode('utf-8')
            str1 = "new"
            str2 = file_name
            file_name = "_".join((str1, str2))
        data2 = connection.recv(1024)
        temp = open(file_name, "a+b")
        if not data2:
            temp.close()
            break
        temp.write(data2)

# Clean up the connection
connection.close()

