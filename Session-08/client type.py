import socket

PORT = 8080
IP = "192.168.124.179"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.send(str.encode("HELLO FROM THE CLIENT!!!"))
s.close()