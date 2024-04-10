import numpy as np
from tsp_solver import TSPSolver
from visualization import Visualization

# Given distance matrix
distance_matrix = np.array([
    [0, 7, 20, 15, 12],
    [10, 0, 6, 14, 18],
    [20, 6, 0, 15, 30],
    [15, 14, 25, 0, 2],
    [12, 18, 30, 2, 0]
])

# Names of the places
places = ['Dorado Park', 'Khomasdal', 'Katutura', 'Eros', 'Klein Windhoek']

def main():
    tsp_solver = TSPSolver(distance_matrix)
    best_route, best_distance = tsp_solver.hill_climbing()
    print("Best Route:", [places[i] for i in best_route])
    print("Total Distance:", best_distance)

    visualization = Visualization(places, distance_matrix)
    visualization.plot_route(best_route)

if __name__ == "__main__":
    main()
