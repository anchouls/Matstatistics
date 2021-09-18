import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import math


def uniform():
    K = []
    SKO = []

    for k in np.arange(0.1, 20, 0.1):
        n = 5000
        s = 1000
        a = 1
        rng = default_rng()
        sko = 0
        for i in range(s):
            X = rng.uniform(0, a, n)
            m_k = np.sum(np.power(X, k)) / n
            ai = ((k + 1) * m_k) ** (1 / k)
            sko += (ai - a) ** 2
        sko /= s
        K.append(k)
        SKO.append(sko)

    plt.plot(K, SKO)
    plt.xlabel('k')
    plt.ylabel('СКО')
    plt.show()


def exp():
    K = []
    SKO = []

    for k in np.arange(1, 50):
        n = 5000
        s = 1000
        a = 1
        rng = default_rng()
        sko = 0
        for i in range(s):
            X = rng.exponential(a, n)
            m_k = np.sum(np.power(X, k)) / n
            ai = (m_k/math.factorial(k)) ** (1 / k)
            sko += (ai - a) ** 2
        sko /= s
        K.append(k)
        SKO.append(sko)

    plt.plot(K, SKO)
    plt.xlabel('k')
    plt.ylabel('СКО')
    plt.show()


uniform()
exp()
