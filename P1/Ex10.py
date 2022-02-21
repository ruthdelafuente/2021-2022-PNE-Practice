from Seq1 import Seq

print("-----| Practice 1, Exercise 10 |------")
FOLDER = "../Session-04/"
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

s0 = Seq()
s0.get_seq(FOLDER, list_genes[0])
d = s0.count()
print("Gene", list_genes[0] + ":", "Most frequent Base:", s0.freq_base(d))

s1 = Seq()
s1.get_seq(FOLDER, list_genes[1])
d = s1.count()
print("Gene", list_genes[1] + ":", "Most frequent Base:", s1.freq_base(d))

s2 = Seq()
s2.get_seq(FOLDER, list_genes[2])
d = s2.count()
print("Gene", list_genes[2] + ":", "Most frequent Base:", s2.freq_base(d))

s3 = Seq()
s3.get_seq(FOLDER, list_genes[3])
d = s3.count()
print("Gene", list_genes[3] + ":", "Most frequent Base:", s3.freq_base(d))

s4 = Seq()
s4.get_seq(FOLDER, list_genes[4])
d = s4.count()
print("Gene", list_genes[4] + ":", "Most frequent Base:", s4.freq_base(d))
