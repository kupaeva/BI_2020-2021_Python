import itertools
from Bio import SeqIO
from Bio.Seq import Seq

generate = ()

def generate(n):
    elements = 'ATGC'
    for len in range(1, n+1):
        for i in itertools.combinations_with_replacement(elements, len):
            yield(''.join(i))

def translator(path):
    file = SeqIO.parse(path, "fasta")
    for seq_record in file:
        yield(seq_record.seq.translate())


length = int(input('Input maximal length of sequense'))
a = generate(length)

for i in a:
    print(i)

b = translator('D:/YandexDisk/хакатон/fishes/Danio.fasta')
for i in b:
    print(i)

