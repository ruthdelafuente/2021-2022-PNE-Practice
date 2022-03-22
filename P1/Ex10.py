from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")
FOLDER = "../Session-04/"
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

i = 0
while i < len(list_genes):
    s = Seq()
    s.read_fasta(FOLDER, list_genes[i])
    d = s.count()
    print("Gene", list_genes[i] + ":", "Most frequent Base:", s.freq_base(d))
    i += 1