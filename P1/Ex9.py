from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")
s = Seq()
FOLDER = "../Session-04/"
FILENAME = "U5"
s.read_fasta(FOLDER, FILENAME)
print(s)
print("Sequence :", "(Len:", str(s.len()) + ")", s, "\n"" Bases:", s.count(), "\n"" Rev:", s.reverse(),"\n"" Comp:", s.complement())
