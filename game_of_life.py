import sys

import numpy as np
from matplotlib import pyplot as plt, animation
from matplotlib.animation import PillowWriter
import evolve


def gameoflife(k):  # Runs Conway's game of life with the Glider formation
    gameoflife.__doc__ = ("Run Conway's Game of Life with the Glider formation for k iterations \n"
                          "Input- k: positive integer number of steps \n"
                          "Outputs- game_of_life.gif: GIF of the evolution of the matrix \n"
                          "\t game_of_life.png: PNG file of final matrix after k iterations")

    # Checks if k is a positive integer or stops the program if invalid
    if not isinstance(k, int) or k <= 0:
        print("k must be a positive integer")
        return

    # Creates the Glider formation
    initialMatrix = np.zeros(shape=(20, 20), dtype=bool)
    initialMatrix[8, 9] = True
    initialMatrix[9, 10] = True
    initialMatrix[10, 8] = True
    initialMatrix[10, 9] = True
    initialMatrix[10, 10] = True
    fig, ax = plt.subplots()
    im = ax.imshow(initialMatrix, cmap='viridis')

    # Defines the update function for the animation
    def update():
        nonlocal initialMatrix
        newMatrix = evolve.evolve(initialMatrix.copy())
        im.set_data(newMatrix)
        initialMatrix = newMatrix
        return im,

    # Animates the evolution and saves it as a GIF
    ani = animation.FuncAnimation(fig, update, frames=range(k), interval=100, blit=True)
    writer = PillowWriter(fps=10)
    try:
        ani.save('game_of_life.gif', writer=writer)
        plt.close()
    except Exception as e:
        print("Error in saving the final animation", e)

    # Creates a plot of the matrix every 10 iterations
    for i in range(k):
        if i % 10 == 0:
            plt.imshow(initialMatrix.astype(int), cmap="binary", interpolation="nearest",
                       extent=[0, initialMatrix.shape[1], 0, initialMatrix.shape[0]])
            plt.show()
        initialMatrix = evolve.evolve(initialMatrix.copy())

    # Save the final plot as a PNG after k iterations
    try:
        plt.imshow(initialMatrix.astype(int), cmap="binary", interpolation="nearest",
                   extent=[0, initialMatrix.shape[1], 0, initialMatrix.shape[0]])
        plt.savefig('game_of_life.png')
    except Exception as e:
        print("Error occurred when saving the final plot", e)

    # Checks if the function is called with only one parameter, k
    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python script.py k")
        else:
            try:
                k = int(sys.argv[1])
                gameoflife(k)
            except ValueError:
                print("Error: k must be an integer.")


# Test data
gameoflife(100)
