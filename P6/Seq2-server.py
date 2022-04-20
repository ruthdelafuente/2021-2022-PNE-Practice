import http.server
import socketserver
import termcolor
import pathlib
from Seq1 import Seq

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
list_seq = ['ATCGTAGCTAGCATGCATGC', 'TTTGCGATGCACAGTCA', 'GACGTAGCTAGCTACTG', 'CTGAGCAGTTGCATGTGCTAAA', 'ACATGCTAGCTATCGAT']
FOLDER = "../Session-04/"

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # We just print a message
        print("GET received! Request line:")

        # Print the request line
        termcolor.cprint("  " + self.requestline, 'green')

        # Print the command received (should be GET)
        print("  Command: " + self.command)

        # Print the resource requested (the path)
        print("  Path: " + self.path)

        # IN this simple server version:
        # We are NOT processing the client's request
        # We are NOT generating any response message

        # Message to send back to the clinet
        #contents = "I am the happy server! :-)"

        lines = self.requestline.split('\n')
        req_line = lines[0]
        route = req_line.split(" ")[1]
        print("ROUTE", route)
        try:
            if route == "/":
                contents = pathlib.Path("html/form-3.html").read_text()
            elif route == "/ping?":
                contents = pathlib.Path("html/ping.html").read_text()
            elif route.startswith("/get?"):
                num = route.split("=")[1]
                contents = pathlib.Path("html/get.html").read_text().format(number=num, seq=list_seq[int(num)])
            elif route.startswith("/gene?"):
                FILENAME = route.split("=")[1].replace("+", "")
                s = Seq()
                s.read_fasta(FOLDER, str(FILENAME))
                contents = pathlib.Path("html/gene.html").read_text().format(name=FILENAME, sequence=s)
            elif route == "/favicon.ico":
                contents = pathlib.Path("html/form-1.html").read_text()
            else:
                filename = route[1:]
                contents = pathlib.Path("html/" + filename + ".html").read_text()
        except FileNotFoundError:
            contents = pathlib.Path("html/error.html").read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())
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