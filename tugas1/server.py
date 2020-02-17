import sys
import socket
# Create a TCP/IP socket
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address1 = ('localhost', 31000)
print(f"starting up on {server_address1}")
sock1.bind(server_address1)

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address2 = ('localhost', 31001)
print(f"starting up on {server_address2}")
sock2.bind(server_address2)

sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address3 = ('localhost', 31002)
print(f"starting up on {server_address3}")
sock3.bind(server_address3)
# Listen for incoming connections
sock1.listen(5)

while True:
    # Wait for a connection
    print("waiting for a connection")
    connection1, client_address1 = sock1.accept()
    print(f"connection from {client_address1}")
    # Receive the data in small chunks and retransmit it
    while True:
        data1 = connection1.recv(128)
        print(f"received {data1.decode()}")
        if data1:
            print("sending back data")
            connection1.sendall(data1)
        else:
            #print >>sys.stderr, 'no more data from', client_address
            #print(f"no more data from {client_address}")
           break
    # Clean up the connection
    connection1.close()
    break
sock1.close()

# sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address2 = ('localhost', 31001)
# print(f"starting up on {server_address2}")
# sock2.bind(server_address2)
sock2.listen(5)

while True:
    # Wait for a connection
    print("waiting for a connection")
    connection2, client_address2 = sock2.accept()
    print(f"connection from {client_address2}")
    # Receive the data in small chunks and retransmit it
    while True:
        data2 = connection2.recv(128)
        print(f"received {data2.decode()}")
        if data2:
            print("sending back data")
            connection2.sendall(data2)
        else:
            #print >>sys.stderr, 'no more data from', client_address
            #print(f"no more data from {client_address}")
           break
    # Clean up the connection
    connection2.close()
    break
sock2.close()

# sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address3 = ('localhost', 31001)
# print(f"starting up on {server_address3}")
# sock3.bind(server_address3)
sock3.listen(5)

while True:
    # Wait for a connection
    print("waiting for a connection")
    connection3, client_address3 = sock3.accept()
    print(f"connection from {client_address3}")
    # Receive the data in small chunks and retransmit it
    while True:
        data3 = connection3.recv(128)
        print(f"received {data3.decode()}")
        if data3:
            print("sending back data")
            connection3.sendall(data3)
        else:
            #print >>sys.stderr, 'no more data from', client_address
            #print(f"no more data from {client_address}")
           break
    # Clean up the connection
    connection3.close()
    break
sock3.close()