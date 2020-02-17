import sys
import socket

# Create a TCP/IP socket
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address1 = ('localhost', 31000)
print(f"connecting to {server_address1}")
sock1.connect(server_address1)

try:
    # Send data
    message = 'JARINGAN TEKNIK INFORPEMROGRAMAN MATIKA'
    print(f"sending {message}")
    sock1.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock1.recv(128)
        amount_received += len(data)
        print(f"{data.decode()}")
finally:
    print("closing")
    sock1.close()

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address2 = ('localhost', 31001)
print(f"connecting to {server_address2}")
sock2.connect(server_address2)

try:
    # Send data
    message = 'JARINGAN TEKNIK INFORPEMROGRAMAN MATIKA'
    print(f"sending {message}")
    sock2.sendall(message.encode())

finally:
    print("closing")
    sock2.close()

sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address3 = ('localhost', 31002)
print(f"connecting to {server_address3}")
sock3.connect(server_address3)

try:
    # Send data
    message = 'JARINGAN TEKNIK INFORPEMROGRAMAN MATIKA'
    print(f"sending {message}")
    sock3.sendall(message.encode())

finally:
    print("closing")
    sock3.close()