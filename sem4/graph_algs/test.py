import numpy as np
from Algs.all_algs import SimAnneal, network_graph

def main():
    adj_mat = np.array([[0,21,0,0,0,0,0,0,13,13,0,0,0,14,15,0,0],
                        [18,0,0,0,0,0,0,0,0,0,60,0,0,0,0,116,79],
                        [0,88,0,0,0,0,0,0,0,0,98,49,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0,0,0,0,0,32,0,0,0,0],
                        [0,0,0,62,0,53,0,0,0,0,0,42,0,0,0,0,0],
                        [0,0,0,0,0,0,11,0,0,0,0,56,0,0,0,0,0],
                        [0,0,0,0,0,13,0,0,0,0,44,0,0,0,0,0,0],
                        [0,0,0,0,0,0,14,0,0,0,0,0,0,0,0,0,0],
                        [19,0,0,0,0,0,0,37,0,24,0,0,0,0,0,0,0],
                        [0,27,0,0,0,0,25,36,0,0,32,0,0,0,0,0,0],
                        [0,0,99,0,156,32,0,0,0,0,0,59,0,0,0,0,0],
                        [0,0,0,68,55,77,0,0,0,0,0,0,0,0,0,0,0],
                        [0,0,87,22,0,0,0,0,0,0,0,0,0,0,0,0,0],
                        [22,0,0,0,0,0,0,0,54,0,0,0,0,0,54,0,0],
                        [40,55,0,0,0,0,0,0,0,0,0,0,0,34,0,33,0],
                        [0,68,0,0,0,0,0,0,0,0,0,0,0,0,44,0,77],
                        [0,0,74,0,0,0,0,0,0,0,0,0,98,0,0,78,0]])
    adj_mat = adj_mat / 100
    adj_mat[adj_mat == 0] = 11

    temp = 30
    gamma = 0.99
    best_tour = None
    best_distance = 1000

    alg = SimAnneal(adj_mat, temp, gamma)
    estimator = network_graph(adj_mat)
    previous_tour = alg.get_init_tour()

    for i in range(100):
        new_tour = alg.change_direction(previous_tour)
        new_tour = alg.alghorithm_step(previous_tour, new_tour)
        current_distance = estimator.get_distance(new_tour)
        if current_distance < best_distance:
            best_distance = current_distance
            best_tour = new_tour
        previous_tour = new_tour
    
    print(best_tour)
    print(best_distance)


if __name__ == "__main__":
    main()