from objects import Sequence as Seq, SequenceComparator as SeqComp


def main():
    # Je définis deux suites géométriques avec une formule de récurrence
    # u(n+1) = u(n) * 0.5          u(0) = 8
    # v(n+1) = v(n) * 0.6          v(0) = 5
    sequence1 = Seq.Sequence("u[n+1] = u[n] * 0.5", first_rank=0, first_term=8)
    sequence2 = Seq.Sequence("v[n+1] = v[n] * 0.6", first_rank=0, first_term=5, name="v")

    # Je définis un comparateur de suites (classe)
    comparator = SeqComp.SequenceComparator(sequence1, sequence2)

    # Je compare les deux suites
    print(comparator.compare("u", "v", maxi=6))


if __name__ == '__main__':
    main()
