import Seq0
FOLDER = "../Session-04/"
list_genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
seq_list = Seq0.get_seq(FOLDER, list_genes)
list_dict = Seq0.seq_count(seq_list)
freq_list = Seq0.freq_base(list_dict)
print("-----| Exercise 8 |------")
i = 0
while i < len(freq_list):
    for d in list_dict:
        for k, v in d.items():
            if d[k] == freq_list[i]:
                print("Gene", list_genes[i], "Most frequent Base:", k)
        i += 1


