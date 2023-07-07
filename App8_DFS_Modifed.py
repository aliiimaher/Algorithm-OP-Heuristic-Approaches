# this is a modified version of DFS 
# but it is not working properly (incomplete)

import random

def euclidean_distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def dfs_randomized(input_file, output_file):
    # Read input from the file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Parse the input
    Tmax, P = map(int, lines[0].split())
    points = []
    for line in lines[1:]:
        x, y, score = map(float, line.split())
        points.append((x, y, score))

    # Initialize variables
    n = len(points)
    visited = [False] * n
    path = [0]  # Starting from the first point (starting point)
    current_time = 0
    current_score = 0
    best_path = None
    best_score = 0

    # Randomized DFS
    def dfs(node):
        nonlocal current_time, current_score, best_path, best_score

        # Update current time and score
        current_time += Tmax
        current_score += points[node][2]
        visited[node] = True

        # Check if the current score is the best so far
        if current_score > best_score:
            best_path = path.copy()
            best_score = current_score

        # Randomly shuffle the unvisited neighbors
        neighbors = [i for i in range(1, n) if not visited[i]]
        random.shuffle(neighbors)

        # Explore the neighbors
        for neighbor in neighbors:
            distance = euclidean_distance(points[node][0], points[node][1], points[neighbor][0], points[neighbor][1])

            # Check if the remaining time is sufficient and the profit is good
            if current_time + distance <= Tmax and points[neighbor][2] / distance > 1.5:
                path.append(neighbor)
                dfs(neighbor)
                path.pop()

        # Undo the changes
        current_time -= Tmax
        current_score -= points[node][2]
        visited[node] = False

    # Start the DFS from the first point (starting point)
    dfs(0)

    # Write the output to the file
    with open(output_file, 'w') as file:
        if best_path is not None:
            file.write(f"Path: {', '.join(map(str, best_path))}\n")
            file.write(f"Total Profit: {best_score}")
        else:
            file.write("No valid path found.")

# Usage example
input_file = 'Dataset/set_64_1_80.txt'
output_file = 'Results/set_64_1_80_App8.txt'
dfs_randomized(input_file, output_file)
