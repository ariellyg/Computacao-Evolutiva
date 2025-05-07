import random

def generate_distance_matrix(n, max_distance=20):
    matrix = [[0 if i == j else random.randint(1, max_distance) for j in range(n)] for i in range(n)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def cheapest_insertion(distance_matrix):
    n = len(distance_matrix)
    unvisited = set(range(n))

    # Escolhe duas cidades iniciais aleatoriamente
    start = random.choice(list(unvisited))
    unvisited.remove(start)

    second_city = random.choice(list(unvisited))
    unvisited.remove(second_city)

    tour = [start, second_city, start]

    print(f"Start: {start}, Second city: {second_city}")
    print(f"Initial tour: {tour}\n")

    while unvisited:
        best_increase = float('inf')
        best_city = None
        best_position = None

        for city in unvisited:
            for i in range(len(tour) - 1):
                a = tour[i]
                b = tour[i + 1]
                increase = distance_matrix[a][city] + distance_matrix[city][b] - distance_matrix[a][b]
                if increase < best_increase:
                    best_increase = increase
                    best_city = city
                    best_position = i + 1

        tour.insert(best_position, best_city)
        unvisited.remove(best_city)

    total_distance = sum(
        distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)
    )

    print(f"Final tour: {tour}")
    print(f"Total distance: {total_distance}")

    return tour, total_distance

num_cities = int(input("Quantas cidades? "))
distance_matrix = generate_distance_matrix(num_cities)

print("\nMatriz de distâncias:")
print_matrix(distance_matrix)
print()

cheapest_insertion(distance_matrix)