import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print(f"connecting to {server_address}")
sock.connect(server_address)

file_name = input("Masukkan nama file yang ingin di request: ")

try:
    # Send data
    sock.sendall(file_name.encode())
    print('Sending data to Server')
    str1 = "req"
    str2 = file_name
    file_name = "_".join((str1, str2))

    while True:
        data = sock.recv(1024)
        temp = open(file_name, "a+b")
        if not data:
            temp.close()
            break
        temp.write(data)

finally:
    print("closing")
    sock.close()