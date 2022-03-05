from Client0 import Client
from Seq1 import Seq
import termcolor

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8081
c = Client(IP, PORT)

FOLDER = "../Session-04/"
list_genes = ["U5", "ADA", "FRAT1"]

for e in list_genes:
    s = Seq()
    s.read_fasta(FOLDER, e)
    msg = str(s)
    response = c.talk(msg)
    print("To server: ", end="")
    termcolor.cprint(f"Sending {e} Gene to the server...", 'blue')
    print("From server: ", end="")
    termcolor.cprint(response, 'green')
    print("To server: ", end="")
    termcolor.cprint(s, 'blue')
    print("From server: ", end="")
    termcolor.cprint(response, 'green')
    print()
