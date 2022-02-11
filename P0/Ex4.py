import Seq0

FOLDER = "../Session-04/"
bases_list = ["A", "C", "T", "G"]
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
seq_list = Seq0.get_seq(FOLDER, list_genes)
count_list = Seq0.seq_count_base(seq_list, bases_list)
i = 0
while i < len(count_list):
    for g in list_genes:
        print("Gene", g + ":")
        for e in bases_list:
            print(e + ":", count_list[i])
            i += 1



