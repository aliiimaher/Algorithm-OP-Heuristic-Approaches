# this greedy approach

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

    # Calculate the "score - cost" value for each node
    score_cost_values = [points[i][2] - distance_matrix[0][i] for i in range(n)]

    # Greedy approach
    visited = [False] * n
    visited[0] = True
    path = [0]  # Start with the first point
    current_time = 0

    while current_time < Tmax:
        max_value = float('-inf')
        max_index = -1

        for i in range(1, n):
            if not visited[i] and score_cost_values[i] > max_value:
                max_value = score_cost_values[i]
                max_index = i

        if max_index == -1:
            break

        time_to_next_node = distance_matrix[path[-1]][max_index]
        if current_time + time_to_next_node > Tmax:
            break

        path.append(max_index)
        visited[max_index] = True
        current_time += time_to_next_node

        for i in range(1, n):
            if not visited[i]:
                score_cost_values[i] -= distance_matrix[max_index][i]

    # Calculate the total profit and total cost
    total_profit = sum(points[i][2] for i in path)
    total_cost = sum(distance_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))

    # Write the output to the file
    with open(output_file, 'w') as file:
        file.write("Path: ")
        file.write(", ".join(str(node+1) for node in path))
        file.write("\n")
        file.write(f"Total Profit: {total_profit}\n")
        file.write(f"Total Cost: {total_cost}")

    print("Path:", ", ".join(str(node+1) for node in path))
    print(f"Total Profit: {total_profit}")
    print(f"Total Cost: {total_cost}")

# Usage example
input_file = 'Dataset/set_66_1_050.txt'
output_file = 'Results/set_66_1_050_App3.txt'
orienteering_problem_greedy(input_file, output_file)
