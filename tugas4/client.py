import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    if(sys.argv[1] == "upload"):
        namaFile = sys.argv[2]
        tmp = open(namaFile, "rb")
        isiFile = tmp.read(4096)
        isiFile = isiFile.decode()
        tmp.close()

        # print('Sending data to Server')
        tmp = "upload " + namaFile + " " + isiFile
        tmp = tmp.encode()
        sock.send(tmp)

    elif(sys.argv[1] == "list"):
        sock.send(sys.argv[1].encode())
        listFile = sock.recv(4096)
        print(listFile.decode())

    elif(sys.argv[1] == "download"):
        namaFile = sys.argv[2]
        tmp = "download " + namaFile
        tmp = tmp.encode()
        sock.send(tmp)

        isiFile = sock.recv(4096)
        tmp = open(namaFile, 'wb')
        tmp.write(isiFile)
        tmp.close()


finally:
    print("closing")
    sock.close()