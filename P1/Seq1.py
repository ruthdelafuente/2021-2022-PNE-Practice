class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        if strbases == "NULL":
            print("NULL Seq Created")

        elif not self.valid_sequence():
            self.strbases = "Error"
            print("INVALID Seq")
        else:
            print("New sequence created!")

    @staticmethod
    def valid_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases):
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid


    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence --> if we don't have this we are going to
        # print the memory location and type of object
        return self.strbases

    def len(self):
        if self.strbases == "NULL" or self.strbases == "Error":
            return 0
        else:
            return len(self.strbases)

    def count_base(self):
        bases = ["A", "C", "G", "T"]
        count_list = [0, 0, 0, 0]
        if self.strbases == "NULL" or self.strbases == "Error":
            zipped_list = list(zip(bases, count_list))
            return zipped_list
        else:
            count_list = []
            for e in bases:
                count = (self.strbases.count(e))
                count_list.append(count)
            zipped_list = list(zip(bases, count_list))
            return zipped_list

    def count(self):
        d = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        if self.strbases == "NULL" or self.strbases == "Error":
            return d
        else:
            for key in d.keys():
                d[key] = (self.strbases.count(key))
            return d

    def reverse(self):
        if self.strbases == "NULL":
            return "NUll"
        elif self.strbases == "Error":
            return "ERROR"
        else:
            new_seq = ""
            for e in self.strbases:
                new_seq = e + new_seq
            return new_seq
    def complement(self):
        if self.strbases == "NULL":
            return "NUll"
        elif self.strbases == "Error":
            return "ERROR"
        else:
            d = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
            comp = ""
            i = 0
            while i < len(self.strbases):
                for key, value in d.items():
                    if self.strbases[i] == key:
                        comp += self.strbases[i].replace(key, value)
                i += 1
            return comp

    def read_fasta(self):
        pass
