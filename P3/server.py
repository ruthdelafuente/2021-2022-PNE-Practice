import socket
import termcolor
from Seq1 import Seq

list_seq = ['ATCGTAGCTAGCATGCATGC', 'TTTGCGATGCACAGTCA', 'GACGTAGCTAGCTACTG', 'CTGAGCAGTTGCATGTGCTAAA', 'ACATGCTAGCTATCGAT']
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

PORT = 8080
IP = "127.0.0.1"

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("The server is configured!")

while True:
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()
    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode().replace("\n", "").strip()
        splitted_command = msg.split(" ")
        cmd = splitted_command[0]
        if cmd != "PING":
            arg = splitted_command[1]

        termcolor.cprint(f"Message received: {msg}", 'green')
        if cmd == "PING":
            response = "OK!\n"
        elif cmd == "GET":
            response = list_seq[int(arg)]
            print(response)
        elif cmd == "INFO":
            s = Seq(arg)
            response = f"Total lenght: {str(s.len())}"
            print(response)

        else:
            response = "This command is not available in the server :-)\n"
        cs.send(response.encode())
        cs.close()