import http.client
import json

SERVER = "127.0.0.1"
PORT = 8080
ENDPOINT = '/listspecies'
PARAMS = '?limit=10'

print(f"\nConnecting to server: {SERVER}\n")
conn = http.client.HTTPConnection(SERVER, PORT)
try:
    conn.request("GET", "/listSpecies?limit=10") #we dont need the server
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
r1 = conn.getresponse()
print(f"Response received!: {r1.status} {r1.reason}\n")
data1 = r1.read().decode("utf-8")
print(f"CONTENT: {data1}")


