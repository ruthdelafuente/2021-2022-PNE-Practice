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

def convert_message(bases_dict, length):
    message = ""
    for k, v in bases_dict.items():
        message += "<p>" + k + ": " + str(v) + " (" + str(round((v/length)*100, 2)) + "%)" + "</p>"
    return message

def change_message():
    return "<br><br><p> ERROR! It looks like you are introducing some data wrong.</p>"


'''def info_operation(arg):
    base_count = count_bases(arg)
    response = "<p> Sequence: " + arg + "</p>"
    response += "<p> Total length: " + str(len(arg)) + "</p>"
    response += convert_message(base_count)
    return response'''