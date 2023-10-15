import numpy as np
import math


def pagerank(A):
    M = A / A.sum(axis=0, keepdims=1)
    r = np.array([1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
    diff = math.inf
    alpha = 0.85
    s = np.array([1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
    while diff > math.exp(-6):
        r = alpha * (M * r) + (1 - alpha) * s
        print(r)
        for i in range(len(r)-1):
            diff = max(abs(r[i + 1] - r[i]))
        print(diff)
    print(np.linalg.eig(M))


B = np.array(
    [
        [0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0],
    ]
)
pagerank(B)
