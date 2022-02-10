import Seq0

FOLDER = "../Session-04/"
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
lenght_list = Seq0.list_lenghts(list_genes, FOLDER)

print("-----| Exercise 3 |------")
zipped_list = list(zip(list_genes, lenght_list))
for e in zipped_list:
    print("Gene", e[0], "---> Length:", e[1])

