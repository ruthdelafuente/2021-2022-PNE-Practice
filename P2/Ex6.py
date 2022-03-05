from Client0 import Client
from Seq1 import Seq
import termcolor

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8081
c = Client(IP, PORT)

FOLDER = "../Session-04/"
FILENAME = "FRAT1"

s = Seq()
s.read_fasta(FOLDER, FILENAME)
s = str(s)
msg = f"Gene FRAT1: {s}"
c.talk(msg)
i = 0
count = 1
while i < len(str(s)) and count < 6:
    seq = s[i:i+10]
    msg = f"Fragment {count}: {seq}"
    c.talk(msg)
    i += 10
    count += 1

i = 0
count = 1
while i < len(str(s)) and count < 6:
    seq = s[i:i+10]
    print(f"Fragment {count}: {seq}")
    i += 10
    count += 1
