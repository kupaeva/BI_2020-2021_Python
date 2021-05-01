
class Rna:
    def __init__(self, sequence):
        self.sequence = sequence.upper()

    def gc_content(self):
        g = self.sequence.count('G')
        c = self.sequence.count('C')
        if len(self.sequence) > 0:
            return (g + c) / len(self.sequence)
        else:
            return None

    def reverse_complement(self):
        complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
        return "".join(complement.get(base, base) for base in reversed(self.sequence))

    def __iter__(self):
        return iter(self.sequence)


class Dna(Rna):
    def __init__(self, sequence):
        super().__init__(sequence)

    def reverse_complement(self):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return "".join(complement.get(base, base) for base in reversed(self.sequence))

    def transcribe(self):
        complement = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
        return Rna("".join(complement.get(base, base) for base in self.sequence))

testInstance = Rna('ATGC')
print(testInstance.reverse_complement())
