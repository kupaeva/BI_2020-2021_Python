import time
import numpy as np
import random
import matplotlib.pyplot as plt
import statistics
from random import shuffle


# this function compare speed of generation random values modules numpy and random
def np_random_compare():
    count_list = []
    time_np = []
    time_random = []
    for count in range(1, 100):
        start_time = time.time()
        np.random.uniform(0, 1, size=count)
        finish_time = time.time() - start_time
        time_np.append(finish_time)
        count_list.append(count)

    for i in count_list:
        time_ = 0
        for j in range(1, i + 1):
            start_time = time.time()
            random.uniform(0, 1)
            finish_time = time.time() - start_time
            time_ += finish_time
        time_random.append(time_)

    plt.plot(time_np, color="red")
    plt.plot(time_random, color="blue")
    plt.xlabel('count of random values')
    plt.ylabel('time')
    plt.show()
    print('ok')


# next 3 function provide bogosort. It work really slow with lists longer than 9.
def check_sorted_bogosort(list_):
    return all(list_[i] <= list_[i + 1] for i in range(len(list_) - 1))


def bogosort(list_):
    while not check_sorted_bogosort(list_):
        shuffle(list_)
    return list_


def bogosort_init():
    size_list = np.arange(2, 10)
    time_temp_list = []
    mean_ = np.zeros(8)
    sd_ = np.zeros(8)

    for size in size_list:
        for repeat in range(10):
            data = np.random.randint(1, 100, size=size)
            start_time = time.time()
            bogosort(data)
            time_temp_list.append(time.time() - start_time)
        mean_[size - 2] = statistics.mean(time_temp_list)
        sd_[size - 2] = statistics.stdev(time_temp_list)
        time_temp_list = []

    plt.plot(size_list, mean_, color="red")
    plt.fill_between(size_list, mean_ - sd_, mean_ + sd_)
    plt.xlabel('Size of array')
    plt.ylabel('Time')
    plt.show()
    print('ok')


# random walk: 100 step to any direction. All dots in scatterplot joined by line.
def random_walk():
    x = [0]
    y = [0]
    n = 0
    while n < 100:
        step = np.random.randint(1, 5)
        if step == 1:
            x.append(x[-1] + 1)
            y.append(y[-1])
        elif step == 2:
            y.append(y[-1] + 1)
            x.append(x[-1])
        elif step == 3:
            x.append(x[-1] - 1)
            y.append(y[-1])
        elif step == 4:
            y.append(y[-1] - 1)
            x.append(x[-1])
        n += 1
    plt.scatter(x, y, color="red", s=10)
    plt.scatter(0, 0, color="black", s=20)
    plt.plot(x, y, color="blue")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Random Walk')
    plt.show()


# this function draw Sierpinski triangle
def triangle():
    x = [0, 1, 2, 0]
    y = [0, 1.75, 0, 0]
    n = 0
    x_side = [np.random.uniform(0, 2)]
    y_side = [np.random.uniform(0, 2)]

    while n < 10000:
        direction = np.random.randint(0, 3)
        x_side.append(x_side[-1] - (x_side[-1] - x[direction]) / 2)
        y_side.append(y_side[-1] - (y_side[-1] - y[direction]) / 2)
        n += 1

    plt.scatter(x_side, y_side, color="red", s=1)
    plt.plot(x, y, color="blue")
    plt.title('Sierpinski triangle')
    plt.show()


# this function draw Sierpinski carpet
def carpet():
    x = [0, 0, 1, 1, 0, 0.5, 0.5, 1]
    y = [0, 1, 0, 1, 0.5, 0, 1, 0.5]

    n = 0
    x_side = [np.random.uniform(0, 1)]
    y_side = [np.random.uniform(0, 1)]

    while n < 100000:
        direction = np.random.randint(0, 8)
        x_side.append((x_side[-1] + x[direction]) / 3)
        y_side.append((y_side[-1] + y[direction]) / 3)
        n += 1

    plt.scatter(x_side, y_side, color="red", s=1)
    plt.title('Sierpiński carpet')
    plt.show()


# this function shuffles letters inside a word
def text_spoil():
    text = input().split(' ')
    new_text = []
    for word in text:
        if len(word) > 1:
            word = list(word)
            new_order = word[1: (len(word) - 1)]
            shuffle(new_order)
            new_order.insert(0, word[0])
            new_order.append(word[-1])
            print(new_order)
            new_text.append(''.join(new_order))
        else:
            new_text.append(word)
    print(new_text)


np_random_compare()
bogosort_init()
random_walk()
triangle()
carpet()
text_spoil()
