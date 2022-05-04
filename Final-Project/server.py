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
PARAMS = '?content-type=application/json'

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
            list_species = dict_answer["species"]
            list_species = list_species[0: n_species]
            contents = read_html_file("list_of_species.html").render(context={"my_lim": n_species, "species": list_species})

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
        print("Stoped by the user")
        httpd.server_close()