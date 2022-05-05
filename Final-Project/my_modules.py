import http.client
import json

SERVER = 'rest.ensembl.org'
def requesting(endpoint, PARAMS): #cambia nombre
    conn = http.client.HTTPConnection(SERVER)
    try:
        conn.request("GET", endpoint + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit() #return NONE y hacer algo con este none en mi server
    r1 = conn.getresponse()
    data1 = r1.read().decode("utf-8")
    return json.loads(data1)
