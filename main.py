import numpy as np
from src.tsp_solver import hill_climbing
from src.visualization import plot_route

# Load the example distance matrix
distance_matrix = np.load('data/distance_matrix.npy')

# Run the hill climbing algorithm
max_iterations = 1000
best_route, best_distance = hill_climbing(distance_matrix, max_iterations)

# Plot the best route
plot_route(best_route, distance_matrix)

print("Best route found:", best_route)
print("Total distance of the best route:", best_distance)
