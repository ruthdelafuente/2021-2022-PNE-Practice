def seq_ping():
    print("OK")


def valid_filename():
    exit = False
    while not exit:
        filename = input("Enter filename: ")
        try:
            f = open(filename, "r")
            exit = True
            return filename
        except FileNotFoundError:
            print("The file does not exist")

def seq_read_fasta(filename):
    seq = open(filename, "r").read()
    seq = seq[seq.find("\n"):].replace("\n", "")
    return seq
