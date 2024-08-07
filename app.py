import numpy as np
import random
import math

graph = {
    "A": [("B", 1), ("C", 3), ("E", 5)],
    "B": [("C", 4)],
    "C": [("D", 3)],
    "D": [("Z", 2)],
    "E": [("K", 4)],
    "K": [],
    "Z": [],
}

heuristic = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 4, "K": 6, "Z": 0}


def get_neighbors(node):
    return graph[node]


def simulated_annealing(start, goal, initial_temp, alpha, stopping_temp, stopping_iter):
    def probability_acceptance(cost, new_cost, temperature):
        if new_cost < cost:
            return 1
        return math.exp(-(new_cost - cost) / temperature)

    current_node = start
    current_cost = heuristic[current_node]
    temperature = initial_temp
    iter_count = 0

    while temperature > stopping_temp and iter_count < stopping_iter:
        iter_count += 1
        neighbors = get_neighbors(current_node)

        if not neighbors:
            break

        next_node = random.choice(neighbors)[0]
        new_cost = heuristic[next_node]

        if (
            probability_acceptance(current_cost, new_cost, temperature)
            > random.random()
        ):
            current_node = next_node
            current_cost = new_cost

        temperature *= alpha

        print(
            f"Iteration: {iter_count}, Temperature: {temperature}, Current node: {current_node}, Current cost: {current_cost}"
        )

        if current_node == goal:
            print("Goal reached!")
            return current_node

    print("Goal not reached! Traveled to city:", current_node)

    return current_node


initial_temp = 1000
alpha = 0.85
stopping_temp = 0.1
stopping_iter = 1000

simulated_annealing("A", "Z", initial_temp, alpha, stopping_temp, stopping_iter)
