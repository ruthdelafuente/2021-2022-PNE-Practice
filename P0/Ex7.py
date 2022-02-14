from pathlib import Path
import Seq0
filename = "../Session-04/U5.txt"
file_contents = Path(filename).read_text()
seq = file_contents[file_contents.find("\n"):].replace("\n", "")[0:20]
print("-----| Exercise 7 |------\nGene U5:\nFrag:", seq, "\nComp:", Seq0.seq_complement(seq))
