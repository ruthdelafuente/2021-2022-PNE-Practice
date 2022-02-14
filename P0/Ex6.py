from pathlib import Path
import Seq0
filename = "../Session-04/U5.txt"
file_contents = Path(filename).read_text()
seq = file_contents[file_contents.find("\n"):].replace("\n", "")[0:20]
print("------| Exercise 6 |------")
print("""Gene U5:
Frag:""", seq, "\nRev:", Seq0.seq_reverse(seq))
