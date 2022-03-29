import socket
import termcolor
import pathlib

IP = "127.0.0.1"
PORT = 8080


def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()
    print("Message FROM CLIENT: ")
    lines = req.split('\n')
    req_line = lines[0]
    print("Request line: ", end="")
    termcolor.cprint(req_line, "green")
    route = req_line.split(" ")[1]
    print("ROUTE", route)
    try:
        filename = route[1:]
        if filename == "info/A":
            body = pathlib.Path("html/info/A" + ".html").read_text()
        elif filename == "info/C":
            body = pathlib.Path("html/info/C" + ".html").read_text()
        elif filename == "info/G":
            body = pathlib.Path("html/info/G" + ".html").read_text()
        elif filename == "info/T":
            body = pathlib.Path("html/info/T" + ".html").read_text()
        else:
            body = pathlib.Path("html/blank" + ".html").read_text()

    except FileNotFoundError:
        body = pathlib.Path("html/error.html").read_text()
    status_line = "HTTP/1.1 200 OK\n"
    header = "Content-Type: text/html\n"
    header += f"Content-Length: {len(body)}\n"
    response_msg = status_line + header + "\n" + body
    cs.send(response_msg.encode())

ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
ls.bind((IP, PORT))
ls.listen()
print("SEQ Server configured!")
while True:
    print("Waiting for clients....")
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print("Server Stopped!")
        ls.close()
        exit()
    else:
        process_client(cs)
        cs.close()