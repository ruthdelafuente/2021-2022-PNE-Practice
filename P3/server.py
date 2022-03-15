import socket
import termcolor
from Seq1 import Seq

def convert_message(bases_dict, s):
    message = ""
    for k, v in bases_dict.items():
        pcg = round((float(v)/(len(s))) * 100, 2)
        print(pcg)
        message += k + ": " + str(v) + " (" + str(pcg) + "%" + ")" "\n"

    return message

FOLDER = "../Session-04/"
list_seq = ['ATCGTAGCTAGCATGCATGC', 'TTTGCGATGCACAGTCA', 'GACGTAGCTAGCTACTG', 'CTGAGCAGTTGCATGTGCTAAA', 'ACATGCTAGCTATCGAT']
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
            try:
                response = list_seq[int(arg)]
                print(response)
            except ValueError:
                response = "The argument must be a number between 0 and 4"
            except IndexError:
                response = "The argument must be a number between 0 and 4"
        elif cmd == "INFO":
            s = Seq(arg)
            bases_dict = s.count()
            response = convert_message(bases_dict, str(s))
            response = f"Total lenght: {str(s.len())}\n{response}"
            print(response)
        elif cmd == "COMP":
            s = Seq(arg)
            response = str(s.complement())
            print(response)
        elif cmd == "REV":
            s = Seq(arg)
            response = str(s.reverse())
            print(response)
        elif cmd == "GENE":
            s = Seq()
            s.read_fasta(FOLDER, str(arg))
            response = str(s)
            print(response)

        else:
            response = "This command is not available in the server :-)\n"
        cs.send(response.encode())
        cs.close()