import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# example of data: scaffolds.faa

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
sns.histplot(len_list)
plt.xlabel('Length')
plt.ylabel('Count')
plt.title('Distribution of sequences length')

plt.show()
