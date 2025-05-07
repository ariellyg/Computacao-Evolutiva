import random

def generate_random_distance_matrix(n, max_distance=20):
    matrix = [[0 if i == j else random.randint(1, max_distance) for j in range(n)] for i in range(n)]
    return matrix

def nearest_neighbor(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    tour = []
    total_distance = 0

    start = random.randint(0, n - 1)
    current_city = start
    visited[current_city] = True
    tour.append(current_city)

    print(f"Start: {start}")
    print(f"Initial tour: {tour}\n")

    while len(tour) < n:
        next_city = None
        min_distance = float('inf')

        for j in range(n):
            if not visited[j] and distance_matrix[current_city][j] < min_distance:
                min_distance = distance_matrix[current_city][j]
                next_city = j

        tour.append(next_city)
        visited[next_city] = True
        total_distance += min_distance
        current_city = next_city

    # Retorna à cidade inicial
    total_distance += distance_matrix[current_city][start]
    tour.append(start)

    print(f"Final tour: {tour}")
    print(f"Total distance: {total_distance}")

    return tour, total_distance

num_cities = 3  # Altere este valor se quiser outro número de cidades
distance_matrix = generate_random_distance_matrix(num_cities)

print("Distance matrix:")
for row in distance_matrix:
    print(row)
print()

nearest_neighbor(distance_matrix)
