from pathlib import Path
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

def list_lenghts(list_genes, FOLDER):
    lenght_list = []
    for l in list_genes:
        lenght = len(seq_read_fasta(FOLDER + l + ".txt"))
        lenght_list.append(lenght)
    return lenght_list

def get_seq(FOLDER, list_genes):
    seq_list = []
    for l in list_genes:
        filename = FOLDER + l + ".txt"
        file_contents = Path(filename).read_text()
        seq = file_contents[file_contents.find("\n"):].replace("\n", "")
        seq_list.append(seq)
    return seq_list


def seq_count_base(seq, base):
    count_list = []
    i = 0
    while i < len(seq):
        for e in base:
            count = (seq[i].count(e))
            count_list.append(count)
        i += 1
    return count_list