import numpy as np
from matplotlib import pyplot as plt, animation
from matplotlib.animation import PillowWriter
import evolve


def gameoflife(k):
    initialMatrix = np.zeros(shape=(20, 20), dtype=bool)
    initialMatrix[8, 9] = True
    initialMatrix[9, 10] = True
    initialMatrix[10, 8] = True
    initialMatrix[10, 9] = True
    initialMatrix[10, 10] = True
    fig, ax = plt.subplots()
    im = ax.imshow(initialMatrix, cmap='viridis')

    def update(num):
        nonlocal initialMatrix
        newMatrix = evolve.evolve(initialMatrix.copy())
        im.set_data(newMatrix)
        initialMatrix = newMatrix
        return im,

    ani = animation.FuncAnimation(fig, update, frames=range(k), interval=100, blit=True)
    writer = PillowWriter(fps=10)
    ani.save('game_of_life.gif', writer=writer)
    plt.close()

    for i in range(k):
        if i % 10 == 0:
            plt.imshow(initialMatrix.astype(int), cmap="binary", interpolation="nearest",
                       extent=[0, initialMatrix.shape[1], 0, initialMatrix.shape[0]])
            plt.show()
        initialMatrix = evolve.evolve(initialMatrix.copy())

    # Save the final plot as 'game_of_life.png' after k iterations
    plt.imshow(initialMatrix.astype(int), cmap="binary", interpolation="nearest",
                   extent=[0, initialMatrix.shape[1], 0, initialMatrix.shape[0]])
    plt.savefig('game_of_life.png')

gameoflife(100)
