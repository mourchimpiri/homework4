import numpy as np
import math


def pagerank(A):  # Implements the PageRank algorithm to a given matrix. Assumes a square NxN matrix is used
    pagerank.__doc__ = ("Implement the PageRank algorithm to a given matrix \n"
                        "Input- A: NxN adjacency matrix of the linked web of pages \n "
                        "Outputs- r: 1x6 updated rank matrix of all webpages \n"
                        " \t diff: Float of the maximum difference between elements in 2 iterations of r \n"
                        " \t Normalized principal eigenvector of normalized matrix M")

    # Normalizes the matrix along the columns
    M = A / A.sum(axis=0, keepdims=1)
    r = np.array([1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
    diff = math.inf
    alpha = 0.85
    s = np.array([1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
    # Continues the loop until r converges
    while diff >= math.exp(-6):
        # Updates the rank according to the dampening factor
        temp_r = alpha * M @ r + (1 - alpha) * s
        diff = max(abs(temp_r - r))
        r = temp_r
        print(r)  # Prints r to check if it converges
        print(diff)  # Prints the difference

    # Finds the principal eigenvector and normalizes the vector to compare to r
    M_eig_values, M_eig_vectors = np.linalg.eig(M)
    comp_eig_vector = M_eig_vectors[:, np.argmax(M_eig_values)]
    norm_comp_eig_vector = comp_eig_vector / comp_eig_vector.sum()
    print(norm_comp_eig_vector)


# Test data
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
B = np.array(
    [
        [0, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0],
    ]
)
pagerank(B)
