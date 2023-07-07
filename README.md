# Algorithm-OP-Heuristic-Approaches
In this project, 8 approaches are presented for solving OP.

Authors: Ali Maher, [Mehdi Mortazavian](@mortazavian)

***

# Orienteering Problem Solver

This repository contains algorithms for solving the Orienteering Problem (OP), an optimization problem that involves finding the shortest route between control points while visiting each point only once and maximizing the total score obtained from these points.

## Introduction

The Orienteering Problem is a well-known problem in the field of operations research with various real-world applications such as logistics, transportation planning, and recreational activities like hiking and orienteering. The goal is to find the most efficient route that visits a set of control points, where each point has a different score associated with it.

## Algorithms

The repository provides several algorithms to solve the Orienteering Problem. Each algorithm is implemented in Python and comes with its own documentation and usage examples. The algorithms available are:

1. Greedy Algorithm A: A greedy algorithm that selects the closest node at each step to minimize the cost of traversing the nodes.
2. Greedy Algorithm B: A greedy algorithm that selects the node with the highest score at each step to maximize the total score.
3. Greedy Algorithm C: A greedy algorithm that selects the node with the highest profit, defined as the difference between the node's score and the cost of visiting the node.
4. Greedy Algorithm D: A modified version of Greedy Algorithm C with an error coefficient to control node selection based on the score-to-distance ratio.
5. Dynamic Programming: A dynamic programming approach that uses a table to calculate the maximum profit at each node and time step, followed by backtracking to extract the optimal path.
6. MST - Kruskal: An approach based on the Kruskal algorithm to find the minimum spanning tree, where the weights of the edges are modified to maximize the profit.
7. MST - Prim: An approach based on the Prim algorithm to find the minimum spanning tree, followed by additional pruning of edges to obtain the maximum path.
8. DFS with Randomized Selection and Bad Nodes Pruning: An algorithm that combines depth-first search with randomized selection of neighbor nodes and pruning of nodes with low scores.

## Usage

To use the algorithms, follow the instructions provided in each algorithm's documentation file. The input format, as well as the expected output, are described in the project documentation.

## Examples

The repository includes example input files and corresponding output files for testing the algorithms. These examples can be used to verify the correctness and efficiency of the algorithms.

## Contribution

Contributions to the repository are welcome. If you have any improvements, bug fixes, or new algorithms to add, feel free to create a pull request.

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

The algorithms in this repository were developed as part of an orienteering problem project. Thanks to the authors and contributors for their valuable work in solving this optimization problem.

## References

1. [Add relevant references here]
2. [Add relevant references here]
3. [Add relevant references here]

