# Python Mini-projects homework4
The pageRank project aims to execute the pageRank algorithm to rank webpages according to their importance

pagerank- this function runs the pageRank algorithm with a given matrix by updating the rank of webpages and compares the final ranking to the principal eigenvector of the normalized initial matrix. The rank stops updating when the difference between elements in consecutive iterations is less than 1e^-6

The gameOfLife project simulates Conway's Game of Life with a Glider formation

countneighbors- this function counts the True neighbors around a specified element. This function includes all 8 surrounding elements and wraps the matrix around the edges to handle edge cases

evolve- this function evolves the matrix according to the rules of Conway's Game of Life

main- this function runs the game for k iterations and saves the final matrix as a PNG and the animation as a GIF. The boolean 20 x 20 matrix uses False = dead and True = alive. The function produces a black-and-white image of the matrix every 10 iterations with False = white and True = black. The file ensures k is a positive integer and handles exceptions with file saving and function calling.