import numpy as np
import random

class TSPSolver:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix

    def calculate_distance(self, route):
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.distance_matrix[route[i], route[i+1]]
        total_distance += self.distance_matrix[route[-1], route[0]]  # Distance from last city back to starting city
        return total_distance

    def generate_initial_route(self):
        return random.sample(range(len(self.distance_matrix)), len(self.distance_matrix))

    def explore_neighboring_solution(self, route):
        i, j = random.sample(range(len(route)), 2)
        new_route = route.copy()
        new_route[i], new_route[j] = new_route[j], new_route[i]
        return new_route

    def hill_climbing(self):
        current_route = self.generate_initial_route()
        current_distance = self.calculate_distance(current_route)

        while True:
            new_route = self.explore_neighboring_solution(current_route)
            new_distance = self.calculate_distance(new_route)

            if new_distance < current_distance:
                current_route = new_route
                current_distance = new_distance
            else:
                break

        return current_route, current_distance
