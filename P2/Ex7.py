from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP1 = "127.0.0.1"
PORT1 = 8080 #server1
c1 = Client(IP1, PORT1)

IP2 = "127.0.0.1"
PORT2 = 8081 #server2
c2 = Client(IP2, PORT2)


FOLDER = "../Session-04/"
FILENAME = "FRAT1"

s = Seq()
s.read_fasta(FOLDER, FILENAME)
s = str(s)
msg = (f"Gene FRAT1: {s}")
c2.talk(msg)
c1.talk(msg)

i = 0
count = 1
while i < len(str(s)) and count < 11:
    seq = s[i:i+10]
    msg = f"Fragment {count}: {seq}"
    if count % 2 == 0:
        c2.talk(str(msg))
    else:
        c1.talk(str(msg))
    i += 10
    count += 1

