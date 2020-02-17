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

    data = connection.recv(1024)
    if data:
        file_name = data.decode('utf-8')
    # print(file_name)

    temp = open(file_name, "rb")
    file = temp.read()
    print('Sending file to Client')
    connection.sendall(file)

    # Clean up the connection
    connection.close()

