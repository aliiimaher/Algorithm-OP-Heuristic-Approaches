# this is DP approach

import math


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def orienteering_problem(input_file, output_file):
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

    # Dynamic programming
    dp = [[0] * (Tmax + 1) for _ in range(n)]
    prev = [[None] * (Tmax + 1) for _ in range(n)]
    for t in range(1, Tmax + 1):
        for j in range(1, n):
            dp[j][t] = float('-inf')
            for i in range(j):  # Utilize symmetry of the distance matrix
                if t >= distance_matrix[i][j]:
                    profit = points[j][2] if t >= distance_matrix[i][j] else 0
                    if dp[i][t - int(distance_matrix[i][j])] + profit > dp[j][t]:
                        dp[j][t] = dp[i][t -
                                         int(distance_matrix[i][j])] + profit
                        prev[j][t] = i

    # Backtracking to construct the optimal path
    path = []  # Starting from the ending point
    j = n - 1  # Ending point
    t = Tmax
    while j is not None:
        path.append(j + 1)
        i = prev[j][t]
        if i is not None:  # Handle the case when i is None
            t -= int(distance_matrix[i][j])
        j = i

    path.reverse()  # Reverse the path to start from the starting point

    # Write the output to the file
    with open(output_file, 'w') as file:
        file.write(f"Path: {', '.join(map(str, path))}\n")
        file.write(f"Total Profit: {dp[n-1][Tmax]}")


    print(path, dp[n-1][Tmax])


# Usage example
input_file = 'Dataset/set_66_1_050.txt'
output_file = 'Results/set_66_1_050_App5.txt'
orienteering_problem(input_file, output_file)
