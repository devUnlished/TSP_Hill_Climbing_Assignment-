TSP Hill Climbing Assignment

Problem Representation:

- Designe a data structure to represent the places and distances between them.
- Implemente a function to calculate the total distance of a given route (visiting order) for all the places.

Hill Climbing Algorithm:
- Implemente the hill climbing algorithm for the TSP.
- Define a function that generates a random initial route visiting all places.
- Define a function to explore neighboring solutions (swap two places in the route).
- Implemente the core logic of hill climbing: evaluate neighboring routes, move to a better route if found, and repeat until reaching a local optimum.



Visualization:
- Develope a visualization tool to display a sample city set and the routes generated by your hill climbing algorithm (initial, intermediate, and final).

Project Implementation:
 tsp_solver.py:
- Implemented the hill climbing algorithm and functions for generating initial routes, exploring neighbors, and calculating total distances.

 visualization.py:
- Developed a visualization tool to display routes using matplotlib or other suitable libraries.

main.py:
- Main script to run the TSP solver and visualization.
- Load the distance matrix and call the hill climbing algorithm.
- Display the results using the visualization tool.

data/distance_matrix.npy:

- Store the example distance matrix as a numpy array for easy loading.


Discussion:
- Analyze the effectiveness of the hill climbing algorithm for solving the TSP.
- Consider real-world limitations and potential improvements for solving the TSP.

