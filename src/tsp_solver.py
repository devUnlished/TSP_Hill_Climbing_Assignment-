import numpy as np
import random

# Function to calculate total distance of a route
def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    num_places = len(route)
    for i in range(num_places - 1):
        current_place = route[i]
        next_place = route[i + 1]
        total_distance += distance_matrix[current_place][next_place]
    # Add distance back to starting point
    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance

# Function to generate a random initial route
def generate_initial_route(num_places):
    return random.sample(range(num_places), num_places)

# Function to explore neighboring solutions (swap two places)
def explore_neighbours(route):
    new_route = route.copy()
    idx1, idx2 = random.sample(range(len(route)), 2)
    new_route[idx1], new_route[idx2] = new_route[idx2], new_route[idx1]
    return new_route

# Function to implement hill climbing algorithm
def hill_climbing(distance_matrix, max_iterations):
    num_places = len(distance_matrix)
    current_route = generate_initial_route(num_places)
    current_distance = calculate_total_distance(current_route, distance_matrix)
    
    for _ in range(max_iterations):
        new_route = explore_neighbours(current_route)
        new_distance = calculate_total_distance(new_route, distance_matrix)
        
        if new_distance < current_distance:
            current_route = new_route
            current_distance = new_distance
    
    return current_route, current_distance

# Create the example distance matrix
distance_matrix = np.array([[0, 7, 20, 15, 12],
                            [10, 0, 6, 14, 18],
                            [20, 6, 0, 15, 30],
                            [15, 14, 25, 0, 2],
                            [12, 18, 30, 2, 0]])

# Save the distance matrix as a numpy array
np.save('data/distance_matrix.npy', distance_matrix)

# Load the distance matrix
distance_matrix = np.load('data/distance_matrix.npy')

# Run the hill climbing algorithm
max_iterations = 1000
best_route, best_distance = hill_climbing(distance_matrix, max_iterations)

print("Best route found:", best_route)
print("Total distance of the best route:", best_distance)
