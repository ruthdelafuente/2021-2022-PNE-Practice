from Seq1 import Seq

print("-----| Practice 1, Exercise 5 |------")
seq1 = Seq()
seq2 = Seq("ACTGA")
seq3 = Seq("AXRAYW")

print("Sequence 1:", "(len:", str(seq1.len()) +")", seq1)
for e1, e2 in seq1.count_base():
    print(e1 + ":", str(e2) + ",", end=" ")
print("\n")

print("Sequence 2:", "(len:", str(seq2.len()) +")", seq2)
for e1, e2 in seq2.count_base():
    print(e1 + ":", str(e2) + ",", end=" ")
print("\n")

print("Sequence 3:", "(len:", str(seq3.len()) +")", seq3)
for e1, e2 in seq3.count_base():
    print(e1 + ":", str(e2) + ",", end=" ")
