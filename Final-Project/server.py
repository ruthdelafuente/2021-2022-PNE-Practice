import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
import http.client
import my_modules
import json
from Seq1 import Seq

HTML_FOLDER = "./html/"
PARAMS = '?content-type=application/json' #if we want to append a parameter -> ej params should be &param1=a -> convert params -> params = "&number=" + str(n_sequence)

def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path #esto quita las interrogaciones
        arguments = parse_qs(url_path.query)
        print("The new path is:", url_path.path)
        print("my arg", arguments)
        if self.path == "/":
            contents = read_html_file('index.html').render()
        elif path == "/listSpecies":
            n_species = int(arguments["limit"][0])
            dict_answer = my_modules.requesting("info/species", PARAMS)
            list_species = []
            total_n_species = []
            for d in dict_answer["species"]:
                total_n_species.append(d["name"])
            if n_species > len(total_n_species) or n_species <= 0:
                contents = read_html_file("list_of_species.html").render(context={"total_number": len(total_n_species), "my_lim": n_species, "species": ["Error. Can´t provide a list with that number"]})
            else:
                for i in range(n_species):
                    list_species.append(dict_answer["species"][i]["name"])
                contents = read_html_file("list_of_species.html").render(context={"total_number": len(total_n_species),"my_lim": n_species, "species": list_species})
        elif path == "/karyotype":
            specie = arguments["select"][0]
            ens_answer = my_modules.requesting("info/assembly/" + specie, PARAMS)
            list_karyotype = []
            list_karyotype.append(ens_answer["karyotype"])
            contents = read_html_file("karyotype.html").render(context={"chromosomes": ens_answer["karyotype"]})
        elif path == "/chromosomeLength":
            pass
        else:
            contents = "I am the happy server :)"
        self.send_response(200)

        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))
        return

Handler = TestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()