from Client0 import Client

PRACTICE = 2
EXERCISE = 2

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "10.3.63.105"
PORT = 8080

c = Client(IP, PORT)
print(c)