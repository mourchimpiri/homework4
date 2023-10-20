import numpy as np
import count_neighbors


def evolve(A):  # Details the rules for Conway's Game of Life
    evolve.__doc__ = ("Details how the matrix evolves in Conway's Game of Life \n"
                      "Input- A: MxN boolean matrix \n"
                      "Output- A: MxN updated matrix")
    rows, cols = A.shape
    evolved_A = np.copy(A)  # Creates a copy of A to edit
    for i in range(rows):
        for j in range(cols):
            if not A[i, j]:
                if count_neighbors.countneighbors(A, i, j) == 3:  # If a false element has 3 True neighbors,
                    # it becomes True
                    evolved_A[i, j] = True
            else:
                if count_neighbors.countneighbors(A, i, j) > 3 or count_neighbors.countneighbors(A, i, j) < 2:  # If a
                    # true element has either more than 3 True neighbors or less than 2 True neighbors, it becomes false
                    evolved_A[i, j] = False

    A = evolved_A
    return A
