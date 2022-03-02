from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "10.3.63.105"
PORT = 8080
c = Client(IP, PORT)
s = Seq()
FILENAME = "../Session-04/U5.txt"
s.read_fasta(FILENAME)
c.talk(s)
