from Seq1 import Seq
str_list = ["ACCTGC", "Hello? Am I a valid sequence?"]
sequence_list = []

#print(Seq.valid_sequence()) --> not going to work

#print(Seq.valid_sequence2((s)))
for e in str_list:
    if Seq.valid_sequence2(e):
        sequence_list.append(Seq(e))
    else:
        sequence_list.append(Seq("ERROR"))

for i in range(0, len(sequence_list)):
    print("Sequence", str(i) + ":", sequence_list[i])