from Seq1 import Seq

print("-----| Practice 1, Exercise 8 |------")

s0 = Seq()
s1 = Seq("ACTGA")
s2 = Seq("VYVUWV")

print("Sequence 0:", "(Len:", str(s0.len()) + ")", s0, "\n"" Bases:", s0.count(), "\n"" Rev:", s0.reverse(),"\n"" Comp:", s0.complement())
print("Sequence 1:", "(Len:", str(s1.len()) + ")", s1, "\n"" Bases:", s1.count(), "\n"" Rev:", s1.reverse(),"\n"" Comp:", s1.complement())
print("Sequence 2:", "(Len:", str(s2.len()) + ")", s2, "\n"" Bases:", s2.count(), "\n"" Rev:", s2.reverse(),"\n"" Comp:", s2.complement())