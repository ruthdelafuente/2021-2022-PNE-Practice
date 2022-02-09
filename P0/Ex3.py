import Seq0

FOLDER = "../Session-04/"

list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
lenght_list = []

print("-----| Exercise 3 |------")
for l in list_genes:
    lenght = len(Seq0.seq_read_fasta(FOLDER + l + ".txt"))
    lenght_list.append(lenght)

zipped_list = list(zip(list_genes, lenght_list))
for e in zipped_list:
    print("Gene", e[0], "---> Length:", e[1])

