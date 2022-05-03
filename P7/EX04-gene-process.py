# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import json
from Seq1 import Seq

def convert_message(bases_dict, s):
    message = ""
    for k, v in bases_dict.items():
        pcg = round((float(v)/(len(s))) * 100, 2)
        message += k + ": " + str(v) + " (" + str(pcg) + "%" + ")" "\n"
    return message

genes_dict = {"SRCAP": "ENSG00000080603", "FRAT1": "ENSG00000165879", "ADA":"ENSG00000196839", "FXN":"ENSG00000165060","RNU6_269P":"ENSG00000212379", "MIR633":"ENSG00000207552", "TTTY4C":"ENSG00000228296", "RBMY2YP":"ENSG00000227633", "FGFR3":"ENSG00000068078", "KDR":"ENSG00000068078", "ANK2":"ENSG00000145362"}

gene_name = input("Write the gene name: ")

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/' + genes_dict[gene_name]
PARAMS = '?content-type=application/json'

print(f"\nConnecting to server: {SERVER}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS) #we dont need the server
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")
data1 = json.loads(data1)


# -- Print the received data
print(f"CONTENT: {data1}")
print("Gene:", gene_name)
print("Description:", data1['desc'])
print(data1['seq'])
s = Seq(data1['seq'])
print("Total length:", s.len())
print(convert_message(s.count(), str(s)))
print("Most frequent Base:", s.freq_base(s.count()))
