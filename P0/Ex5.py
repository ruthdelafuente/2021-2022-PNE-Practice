import Seq0

FOLDER = "../Session-04/"
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
seq_list = Seq0.get_seq(FOLDER, list_genes)
list_dict = Seq0.seq_count(seq_list)
i = 0
while i < len(list_dict):
    for g in list_genes:
        print("Gene", g + ":", list_dict[i])
        i += 1

