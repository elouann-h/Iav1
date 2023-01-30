class SequenceComparator:
    def __init__(self, *sequences):
        self.sequences = dict()

        for seq in sequences:
            self.sequences[seq.name] = seq

    def compare(self, name1, name2, mini=0, maxi=10, step=1):
        seq1 = self.sequences[name1]
        seq2 = self.sequences[name2]
        seq1.table.set(mini, maxi, step)
        seq2.table.set(mini, maxi, step)
        seq1.table.draw()
        print("------------")
        seq2.table.draw()
        print("------------")
        remarkable_n = 0
        compare = "<="
        pass_to = ">"
        change = False
        for i in range(1, len(seq1.table.table)):
            if i == 1:
                if seq1.table.table[i][1] > seq2.table.table[i][1]:
                    compare = ">"
                else:
                    compare = "<="
            else:
                if seq1.table.table[i][1] > seq2.table.table[i][1] and compare == ">":
                    if not change:
                        remarkable_n = i + 1
                        change = True
                        continue
                elif seq1.table.table[i][1] < seq2.table.table[i][1] and compare == "<=":
                    if not change:
                        remarkable_n = i + 1
                        change = True
                        continue
            if change:
                if seq1.table.table[remarkable_n + 1][1] > seq2.table.table[remarkable_n + 1][1]:
                    pass_to = ">"
                else:
                    pass_to = "<="
                break
        result = "When n ∈ [{} ; {}] {}({}) {} {}({})".format(
            mini, remarkable_n - 1, seq1.name, seq1.unknown, compare, seq2.name, seq1.unknown)
        result += "\nWhen n ∈ [{} ; +∞[ {}({}) {} {}({})".format(
            remarkable_n, seq1.name, seq1.unknown, pass_to, seq2.name, seq1.unknown)
        return result

