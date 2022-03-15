from Client0 import Client

PRACTICE = 3
EXERCISE = 7

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)

print(" * Testing PING...")
msg = c.talk("PING")
print(msg)

print(" * Testing GET...")
msg = c.talk("GET 0")
print(" GET 0:", msg)
msg = c.talk("GET 1")
print(" GET 1:", msg)
msg = c.talk("GET 2")
print(" GET 2:", msg)
msg = c.talk("GET 0")
print(" GET 3:", msg)
msg = c.talk("GET 4")
print(" GET 4:", msg)

print(" * Testing INFO...")
print("Sequense: AAATCGATGCTAGCTAGC")
msg = c.talk("INFO AAATCGATGCTAGCTAGC")
print(msg)

print(" * Testing COMP...")
print("COMP GGCTAGCGATCAGTGTCAGCTA")
msg = c.talk("COMP GGCTAGCGATCAGTGTCAGCTA")
print(msg)

print(" * Testing REV...")
print("REV ATCATGCGTTGGCACGT")
msg = c.talk("REV ATCATGCGTTGGCACGT")
print(msg)

print(" * Testing GENE...")
print("GENE U5")
msg = c.talk("GENE U5")
print(msg)
print("GENE ADA")
msg = c.talk("GENE ADA")
print(msg)
print("GENE FRAT1")
msg = c.talk("GENE FRAT1")
print(msg)
print("GENE FXN")
msg = c.talk("GENE FXN")
print(msg)
print("GENE RNU6_269P")
msg = c.talk("GENE RNU6_269P")
print(msg)