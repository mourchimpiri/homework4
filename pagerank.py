import numpy as np
import math


def pagerank(A):
    M = A / A.sum(axis=0, keepdims=1)
    print(M)
    r = np.array([1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
    diff = math.inf
    alpha = 0.85
    s = np.array([1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
    while diff >= math.exp(-6):
        temp_r = alpha * M @ r + (1 - alpha) * s
        diff = max(abs(temp_r - r))
        r = temp_r
        print(r)
        print(diff)
    M_eig_values, M_eig_vectors = np.linalg.eig(M)
    comp_eig_vector = M_eig_vectors[:, np.argmax(M_eig_values)]
    norm_comp_eig_vector = comp_eig_vector/comp_eig_vector.sum()
    print(norm_comp_eig_vector)

A = np.array(
    [
        [0, 1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0],
    ]
)
pagerank(A)
