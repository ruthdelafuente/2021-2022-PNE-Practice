from Seq1 import Seq

print("-----| Practice 1, Exercise 6 |------")
seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("AXRAYW")

print("Sequence 1:", "(len:", str(seq1.len()) +")", seq1, "\n", "Bases:", seq1.count())
print("Sequence 2:", "(len:", str(seq2.len()) +")", seq2, "\n", "Bases:", seq2.count())
print("Sequence 3:", "(len:", str(seq3.len()) +")", seq3, "\n", "Bases:", seq3.count())