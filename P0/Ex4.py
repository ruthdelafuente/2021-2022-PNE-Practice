import Seq0

FOLDER = "../Session-04/"
bases_list = ["A", "C", "T", "G"]
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
seq_list = Seq0.get_seq_list(FOLDER, list_genes)
i = 0
while i < len(seq_list):
    for g in list_genes:
        print("Gene", g + ":")
        for e in bases_list:
            print(e + ":", seq_list[i].count(e))
        i += 1



