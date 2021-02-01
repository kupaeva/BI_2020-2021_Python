import matplotlib.pyplot as plt

#example of data: scaffolds.faa

path = input('Input path to file in format fasta')

len_list = []
len_ = 0
with open(path) as f:
    for line in f:
        if '>' in line:
            if len_ != 0:
                len_list.append(len_)
                len_ = 0
        elif '>' not in line:
            len_ += len(line.rstrip())
len_list.append(len_)

num_bins = max(len_list)
n, bins, patches = plt.hist(len_list, num_bins, facecolor='green', alpha=0.5)
plt.xlabel('Length')
plt.ylabel('Count')
plt.title('Distribution of sequences length')

plt.show()
