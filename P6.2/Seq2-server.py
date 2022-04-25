import http.server
import socketserver
import termcolor
from pathlib import Path
import jinja2 as j
from urllib.parse import parse_qs, urlparse
from Seq1 import Seq

HTML_FOLDER = "./html/"
LIST_SEQUENCES = ['ATCGTAGCTAGCATGCATGC', 'TTTGCGATGCACAGTCA', 'GACGTAGCTAGCTACTG', 'CTGAGCAGTTGCATGTGCTAAA', 'ACATGCTAGCTATCGAT']
LIST_GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
def read_html_file(filename):
    contents = Path(HTML_FOLDER + filename).read_text()
    contents = j.Template(contents)
    return contents

def count_bases(seq):
    d = {"A": 0, "C": 0, "G": 0, "T": 0}
    for b in seq:
        d[b] += 1

    total = sum(d.values())
    for k,v in d.items():
        d[k] = [v, (v * 100) / total]
    return d

def convert_message(base_count):
    message = ""
    for k,v in base_count.items():
        message += k + ": " + str(v[0]) + " (" + str(v[1]) + "%)" +"\n"
    return message
# Define the Server's port
def info_operation(arg):
    base_count = count_bases(arg)
    response = "<p> Sequence: " + arg + "</p>"
    response += "<p> Total length: " + str(len(arg)) + "</p>"
    response += convert_message(base_count)
    return response
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

'''def read_template_html(filename):
    template = Template(Path(filename).read_text())
    return template'''
# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print("The new path is:", url_path.path)
        if self.path == "/":
            contents = read_html_file('index.html').render(context={"n_sequences": len(LIST_SEQUENCES), "genes": LIST_GENES})
        elif path == "/ping":
            contents = read_html_file(path[1:] + ".html").render()
        elif path == "/get":
            n_sequence = int(arguments["n_sequence"][0])
            sequence = LIST_SEQUENCES[n_sequence]
            contents = read_html_file(path[1:] + ".html").render(context={"n_sequence": n_sequence, "sequence": sequence})
        elif path == "/gene":
            gene_name = arguments["gene_name"][0]
            sequence = Path("./sequences/" + gene_name + ".txt").read_text()
            contents = read_html_file(path[1:] + ".html").render(context={"gene_name": gene_name, "sequence": sequence})
        elif path == "/operation":
            sequence = arguments["sequence"][0]
            operation = arguments["operation"][0]
            if operation == "rev":
                contents = read_html_file(path[1:] + ".html").render(context={"operation": operation, "result": sequence[::-1]})
            #elif operation == "info":
                #contents = read_html_file(path[1:] + ".html").render(context={"operation": operation, "result": info_operation(sequence)})

        else:
            contents = "I am the happy server :)"
            # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return

    # ------------------------
    # - Server MAIN program
    # ------------------------
    # -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()