from Seq1 import Seq

print("-----| Practice 1, Exercise 9 |------")
s = Seq()
FILENAME = "../Session-04/U5.txt"
s.read_fasta(FILENAME)
print(s)
print("Sequence :", "(Len:", str(s.len()) + ")", s, "\n"" Bases:", s.count(), "\n"" Rev:", s.reverse(),"\n"" Comp:", s.complement())
