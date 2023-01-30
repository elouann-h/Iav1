from objects import SequenceTable as SeqTable


class Sequence:
    def __init__(self, expression, name="u", unknown="n", first_term=1, first_rank=0):
        self.expression = expression.replace(" ", "")
        self.name = name
        self.unknown = unknown
        self.first_term = first_term
        self.first_rank = first_rank
        self.table = SeqTable.SequenceTable(self)

    def is_recur(self):
        step = 0
        for i in self.expression.split("=")[1]:
            if step == 0:
                if i == self.name:
                    step = 1
                else:
                    step = 0
            elif step == 1:
                if i == "[":
                    step = 2
                else:
                    step = 0
            elif step == 2:
                if i == self.unknown:
                    step = 3
                else:
                    step = 0
            elif step == 3:
                if i == "]":
                    return True
                step = 0
        return False

    def reduced_expression(self):
        return self.expression.split("=")[1]

    def dissect(self):
        expr = self.reduced_expression()
        symbol, seq_type = "", None
        if not self.is_recur():
            for i in range(len(expr)):
                if expr[i] in ["*"]:
                    symbol, seq_type = expr[i], "arithmetical"
                elif expr[i] in ["^"]:
                    symbol, seq_type = expr[i], "geometrical"
            reason = expr.split(symbol)[1]
            return seq_type, reason, symbol
        else:
            for i in range(len(expr)):
                if expr[i] in ["+", "-"]:
                    symbol, seq_type = expr[i], "arithmetical"
                elif expr[i] in ["*"]:
                    symbol, seq_type = expr[i], "geometrical"
                if seq_type is not None:
                    break
            reason = expr.split(symbol)[1]
            return seq_type, reason, symbol

    def term(self, rank):
        if not self.is_recur():
            return eval(self.reduced_expression().replace('n', str(rank)))
        else:
            if rank < self.first_rank:
                return "Does not exist"
            elif rank == self.first_rank:
                return self.first_term
            else:
                dissected = self.dissect()
                seq_type, reason = dissected[0], dissected[1]
                explicit_form = 0
                if seq_type == "arithmetical":
                    explicit_form = self.first_term + (rank - self.first_rank) * float(reason)
                elif seq_type == "geometrical":
                    explicit_form = self.first_term * float(reason) ** (rank - self.first_rank)
                return explicit_form

    def variation(self):
        dissected = self.dissect()
        seq_type, reason, symbol = dissected[0], dissected[1], dissected[2]
        if seq_type == "arithmetical":
            return eval("{}1".format(symbol))
        elif seq_type == "geometrical":
            if float(reason) >= 1:
                return 1
            elif float(reason) > 0:
                return -1
        return "Does not exist"