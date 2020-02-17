import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)

file_name = input("Masukkan nama file yang ingin di kirim: ")

try:
    # Send data
    sock.send(file_name.encode())

    print(file_name)
    temp = open(file_name, "rb")
    file = temp.read()
    print('Sending data to Server')
    sock.send(file)
finally:
    print("closing")
    sock.close()