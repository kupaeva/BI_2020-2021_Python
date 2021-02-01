import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

#example of data: python_scores.tsv

student = []
scores = []
path = input('Input path to file with data in tsv format, which contains 2 columns with data')
path_x = input('Input label for x axis')
path_y = input('Input label for y axis')
path_title = input('Input title for plot')

with open(path) as f:
    for line in f:
        line_ = line.rstrip().split('\t')
        student.append(line_[0])
        scores.append(float(line_[1].replace(',','.')))

a = [scores, student]
sns.lineplot(x = student, y = scores)
plt.xlabel('path_x')
plt.ylabel('path_y')
plt.title('path_title')

plt.show()