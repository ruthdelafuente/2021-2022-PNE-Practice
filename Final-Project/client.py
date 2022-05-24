import http.client
import json
import termcolor

SERVER = "127.0.0.1"
PORT = 8080
ENDPOINT = '/listspecies'
PARAMS = '?limit=10'

def convert_json(data1):
    for k, v in data1.items():
        print(k + ":" + str(v) + "\n")

print(f"\nConnecting to server: {SERVER}\n")
conn = http.client.HTTPConnection(SERVER, PORT)

termcolor.cprint("--TEST /listSpecies--", 'green')
conn.request("GET", "/listSpecies?limit=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/listSpecies?limit=1", 'blue')
print("* Output: ")
print(data1)

conn.request("GET", "/listSpecies?limit=-1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/listSpecies?limit=-1", 'blue')
print("* Output: ")
print(data1)

conn.request("GET", "/listSpecies?limit=7&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/listSpecies?limit=7&json=1", 'blue')
print("* Output: ")
data1 = json.loads(data1)
convert_json(data1)

termcolor.cprint("--TEST /karyotype--", 'green')
conn.request("GET", "/karyotype?specie=pig")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/karyotype?specie=pig", 'blue')
print("* Output: ")
print(data1)

conn.request("GET", "/karyotype?specie=bicycle")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/karyotype?specie=bicycle", 'blue')
print("* Output: ")
print(data1)

conn.request("GET", "/karyotype?specie=pig&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/karyotype?specie=pig&json=1", 'blue')
print("* Output: ")
data1 = json.loads(data1)
convert_json(data1)

termcolor.cprint("--TEST /chromosomeLength--", 'green')
conn.request("GET", "/chromosomeLength?name=human&number=14")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/chromosomeLength?name=human&number=14", 'blue')
print("* Output: ")
print(data1)

conn.request("GET", "/chromosomeLength?name=human&number=hello")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/chromosomeLength?name=human&number=hello", 'blue')
print("* Output: ")
print(data1)

conn.request("GET", "/chromosomeLength?name=human&number=7&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/chromosomeLength?name=human&number=7&json=1", 'blue')
print("* Output: ")
data1 = json.loads(data1)
convert_json(data1)

termcolor.cprint("--TEST /geneSeq--", 'green')
conn.request("GET", "/geneSeq?gene_name=SRCAP")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/geneSeq?gene_name=SRCAP", 'blue')
print("* Output: ")
print(data1)

conn.request("GET", "/geneSeq?gene_name=SRCAP&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/geneSeq?gene_name=SRCAP&json=1", 'blue')
print("* Output: ")
data1 = json.loads(data1)
convert_json(data1)

termcolor.cprint("--TEST /geneInfo--", 'green')
conn.request("GET", "/geneInfo?gene_name=FGFR3")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/geneInfo?gene_name=FGFR3", 'blue')
print("* Output: ")
print(data1)

conn.request("GET", "/geneInfo?gene_name=FGFR3&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/geneInfo?gene_name=FGFR3&json=1", 'blue')
print("* Output: ")
data1 = json.loads(data1)
convert_json(data1)

termcolor.cprint("--TEST /geneCalc--", 'green')
conn.request("GET", "/geneCalc?g_name=TTTY4C")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/geneCalc?g_name=TTTY4C", 'blue')
print("* Output: ")
print(data1)

conn.request("GET", "/geneCalc?g_name=TTTY4C&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/geneCalc?g_name=TTTY4C&json=1", 'blue')
print("* Output: ")
data1 = json.loads(data1)
convert_json(data1)

termcolor.cprint("--TEST /geneList--", 'green')
conn.request("GET", "/geneList?chromo=9&start=22125500&end=22136000")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/geneList?chromo=9&start=22125500&end=22136000", 'blue')
print("* Output: ")
print(data1)

conn.request("GET", "/geneList?chromo=9&start=22125500&end=22136000&json=1")
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
termcolor.cprint("/geneList?chromo=9&start=22125500&end=22136000&json=1", 'blue')
print("* Output: ")
data1 = json.loads(data1)
convert_json(data1)
