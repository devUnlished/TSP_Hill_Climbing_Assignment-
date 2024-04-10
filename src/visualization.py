import matplotlib.pyplot as plt

class Visualization:
    def __init__(self, places, distance_matrix):
        self.places = places
        self.distance_matrix = distance_matrix

    def plot_route(self, route):
        plt.figure(figsize=(8, 6))
        plt.scatter(self.distance_matrix[:, 0], self.distance_matrix[:, 1], color='blue', label='Cities', s=200)
        plt.plot(self.distance_matrix[route, 0], self.distance_matrix[route, 1], color='red', linestyle='-', marker='o', markersize=8, label='Route')
        for i, place in enumerate(self.places):
            plt.text(self.distance_matrix[i, 0], self.distance_matrix[i, 1], place, fontsize=12, ha='right')
        plt.xlabel('X coordinate (Kilometers)')
        plt.ylabel('Y coordinate (Kilometers)')
        plt.title('Travelling Salesman Problem - Hill Climbing Solution')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
