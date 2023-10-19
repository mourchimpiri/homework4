import numpy as np
import count_neighbors


def evolve(A):
    rows, cols = A.shape
    evolved_A = np.copy(A)
    for i in range(rows):
        for j in range(cols):
            if not A[i, j]:
                if count_neighbors.countneighbors(A, i, j) == 3:
                    evolved_A[i, j] = True
            else:
                if count_neighbors.countneighbors(A, i, j) > 3 or count_neighbors.countneighbors(A, i, j) < 2:
                    evolved_A[i, j] = False

    A = evolved_A
    return A
