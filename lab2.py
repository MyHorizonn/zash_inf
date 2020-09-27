import matplotlib.pyplot as plt
import math
import numpy as np
from random import randint, seed


def main():
    print("A")
    a = float(input())
    print("B")
    b = float(input())
    print("C")
    c = float(input())
    print("alpha")
    alpha = float(input())
    print("beta")
    beta = float(input())
    print("gamma")
    gamma = float(input())
    print("signal")
    kek = input()
    signal_x = [i for i in kek]
    print(signal_x)
    x = list()
    temp = 0.8
    for i in range(len(signal_x)):
        temp += 0.2
        x.append(temp)
    print(x)
    y = list()
    for i in range(len(x)):
        y.append(a * math.sin(alpha * x[i]) + b * math.cos(beta * x[i]) + x[i] * c * math.cos(math.cos(gamma * x[i])))
    print(y)
    print("key")
    key = int(input())
    y1 = list()
    seed(key)
    for i in range(len(x)):
        y1.append(randint(0, len(x)))
    print(y1)
    print(signal_x)
    plt.subplot(2, 2, 1)
    plt.plot(x, y, 'o-g', fillstyle='none', ls='-', lw=2.5)
    plt.grid(True)
    for i in range(len(y)):
        temp = y[i]
        y[i] = y[y1[i]]
        y[y1[i]] = temp
        print(i, y1[i])
    plt.subplot(2, 2, 2)
    plt.plot(x, y, 'o-g', fillstyle='none', ls='-', lw=2.5)
    plt.grid(True)
    for i in reversed(range(len(y))):
        temp = y[i]
        y[i] = y[y1[i]]
        y[y1[i]] = temp
        print(i, y1[i])
    plt.subplot(2, 2, 3)
    plt.plot(x, y, 'o-g', fillstyle='none', ls='-', lw=2.5)
    plt.grid(True)
    plt.show()


main()
