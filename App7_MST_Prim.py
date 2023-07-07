# this is MST approach using Prim's algorithm

import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def orienteering_problem_prim(input_file, output_file):
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

    # Create the "score - cost" values list for each node
    node_values = [points[i + 1][2] - distance_matrix[0][i + 1] for i in range(n - 1)]

    # Initialize the parent array for the MST
    parent = [-1] * n

    # Initialize the minimum values array
    min_values = [float('inf')] * n

    # Set the minimum value of the starting node to 0
    min_values[0] = 0

    # Find the minimum value node from the list
    def find_min_value():
        min_value = float('inf')
        min_index = -1
        for i in range(1, n):
            if node_values[i - 1] < min_value:
                min_value = node_values[i - 1]
                min_index = i
        return min_index

    # Perform Prim's algorithm
    mst = []
    total_profit = 0
    total_cost = 0

    for _ in range(n - 1):
        u = find_min_value()
        if u == -1:
            break
        mst.append((parent[u], u))
        total_profit += points[u + 1][2]
        total_cost += distance_matrix[parent[u]][u]
        node_values[u - 1] = float('inf')

        for v in range(1, n):
            if distance_matrix[u][v] <= Tmax and node_values[v - 1] > points[v][2] - distance_matrix[u][v]:
                node_values[v - 1] = points[v][2] - distance_matrix[u][v]
                parent[v] = u

    # Write the output to the file
    with open(output_file, 'w') as file:
        file.write("MST Edges:\n")
        for edge in mst:
            file.write(f"{edge[0]+1} - {edge[1]+1}\n")
        file.write("\n")
        file.write(f"Total Profit: {total_profit}\n")
        file.write(f"Total Cost: {total_cost}")

    print("MST Edges:")
    for edge in mst:
        print(f"{edge[0]+1} - {edge[1]+1}")
    print(f"Total Profit: {total_profit}")
    print(f"Total Cost: {total_cost}")

# Usage example
input_file = 'Dataset/set_64_1_80.txt'
output_file = 'Results/set_64_1_80_App7.txt'
orienteering_problem_prim(input_file, output_file)
