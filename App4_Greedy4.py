# this greedy approach

# greedy with error coefficient

import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def orienteering_problem_greedy(input_file, output_file):
    # Read input from the file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Parse the input
    Tmax, P = map(int, lines[0].split())
    points = []
    for line in lines[1:]:
        x, y, score = map(float, line.split())
        points.append((x, y, score))

    # Calculate the distance matrix
    n = len(points)
    distance_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):  # Utilize symmetry of the distance matrix
            dist = euclidean_distance(
                points[i][0], points[i][1], points[j][0], points[j][1])
            distance_matrix[i][j] = dist
            distance_matrix[j][i] = dist

    # Compute the score-to-distance ratio for each node
    ratio_values = [points[i][2] / distance_matrix[0][i] for i in range(1, n)]

    # Greedy algorithm
    path = [0]  # Starting from the first point (starting point)
    current_time = 0
    current_score = 0
    visited = [False] * n
    visited[0] = True

    while current_time < Tmax:
        remaining_time = Tmax - current_time
        max_ratio = 0
        max_index = None

        for i in range(1, n):
            if not visited[i] and remaining_time >= distance_matrix[path[-1]][i]:
                if ratio_values[i-1] > 2 and distance_matrix[path[-1]][i] < remaining_time:
                    if ratio_values[i-1] > max_ratio:
                        max_ratio = ratio_values[i-1]
                        max_index = i
        
        if max_index is None:
            break

        path.append(max_index)
        current_time += distance_matrix[path[-2]][max_index]
        current_score += points[max_index][2]
        visited[max_index] = True
    print("gooz: ", remaining_time)

    # Write the output to the file
    with open(output_file, 'w') as file:
        file.write(f"Path: {', '.join(map(str, path))}\n")
        file.write(f"Total Profit: {current_score}")

    print(f"Path: {path}")
    print(f"Total Profit: {current_score}")

# Usage example
input_file = 'Dataset/set_66_1_050.txt'
output_file = 'Results/set_66_1_050_App4.txt'
orienteering_problem_greedy(input_file, output_file)
