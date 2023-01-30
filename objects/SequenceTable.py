class SequenceTable:
    def __init__(self, sequence):
        self.sequence = sequence
        self.mini = 0
        self.maxi = 10
        self.step = 1
        self.table = list()

    def set(self, mini, maxi, step):
        self.mini = mini
        self.maxi = maxi
        self.step = step

    def calc(self):
        self.table = [
            ["{}".format(self.sequence.unknown), "{}({})".format(self.sequence.name, self.sequence.unknown)]
        ]
        for i in range(self.mini, self.maxi + 1, self.step):
            self.table.append([i, self.sequence.term(i)])
        return self.table

    def draw(self):
        self.calc()
        max_len = len(str(sorted(self.table, key=lambda x: len(str(x[0])), reverse=True)[0][0]))

        for i in range(len(self.table)):
            print(self.table[i][0], " " * (max_len - len(str(self.table[i][0]))), " | ", self.table[i][1],
                  end="\n")
