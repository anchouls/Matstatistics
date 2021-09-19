import numpy as np
from numpy.random import default_rng
import matplotlib.pyplot as plt
import math

n = 1000
s = 1000
a = 1
rng = default_rng()


def uniform(k):
    X = rng.uniform(0, a, n)
    m_k = np.sum(np.power(X, k)) / n
    return ((k + 1) * m_k) ** (1 / k)


def exp(k):
    X = rng.exponential(a, n)
    m_k = np.sum(np.power(X, k)) / n
    return (m_k / math.factorial(k)) ** (1 / k)


def fun(f, name):
    K = []
    SKO = []
    for k in range(1, 50):
        sko = 0
        for i in range(s):
            sko += (f(k) - a) ** 2
        sko /= s
        K.append(k)
        SKO.append(sko)

    plt.plot(K, SKO, label=name)
    plt.xlabel('k')
    plt.ylabel('СКО')
    plt.legend()
    plt.show()


fun(uniform, "Uniform")
fun(exp, "Exponential")
