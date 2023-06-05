import numpy as np
from scipy.spatial import distance
import random

class network_graph:
    def __init__(self, adj_mat):
        self.adj_mat = adj_mat

    def get_distance(self, current_tour):
        distance = 0
        for direction in current_tour:
            distance += self.adj_mat[direction[0], direction[1]]
        return distance

    
class NVM(network_graph):
    def __init__(self, adj_mat):
        super().__init__(adj_mat)

    def gamilton_tour_with_nvm(self, first_node = None, first_dir = None):

        visited = []
        gamilton_tour = []
        node = first_node or 0
        while node not in visited:
            current_row = self.adj_mat[node]
            
            if first_dir == None:
                min_ind = np.argmin(current_row)
            else:
                min_ind = first_dir

            if min_ind in visited:
                current_row[min_ind] = 100
            else:
                visited.append(node)
                found_edge = [node, min_ind]
                gamilton_tour.append(found_edge)
                node = min_ind
                first_dir = None
        
        n_nodes = len(self.adj_mat[0])
        if len(visited) == n_nodes:
            gamilton_tour[-1][1] = gamilton_tour[0][0]
            return gamilton_tour
        else:
            return 'Гамильтонов цикл отсутствует'


class SimAnneal(network_graph):

    initial_phase = True

    def __init__(self, adj_mat, temp, gamma):
        super().__init__(adj_mat)
        self.temp = temp
        self.gamma = gamma

    def get_init_tour(self):
        if self.initial_phase:
            nvm = NVM(self.adj_mat.copy())
            init_tour = nvm.gamilton_tour_with_nvm()
            self.initial_phase = False
            return init_tour
        else:
            return None

    def change_direction(self, current_tour):
        in_process = True
        while in_process:
            node = random.randint(0, np.shape(self.adj_mat)[0]- 1)
            current_row = self.adj_mat[node]
            existing_directions = [[node, i] for i, dir in enumerate(current_row) if dir < 11]
            if len(existing_directions) > 1:
                checked_ind = random.randint(0, len(existing_directions) - 1)
                checked = existing_directions[checked_ind]
                while checked in current_tour:
                    checked_ind = random.randint(0, len(existing_directions) - 1)
                    checked = existing_directions[checked_ind]
                nvm = NVM(self.adj_mat.copy())
                new_tour = nvm.gamilton_tour_with_nvm(checked[0], checked[1])
                in_process = False
        
        return new_tour

    def check_accept(self, current_solution, new_solution):
        prob = min(1, np.exp(-(new_solution - current_solution) / self.temp))
        if prob > random.uniform(0, 1):
            return True
        else:
            return False
        
    def alghorithm_step(self, old_tour, new_tour):
        old_dist = self.get_distance(old_tour)
        new_dist = self.get_distance(new_tour)
        self.temp = self.temp * self.gamma
        decision = self.check_accept(old_dist, new_dist)
        if decision:
            return new_tour
        else:
            return old_tour
        
class ACO_TSP(network_graph):
    def __init__(self, adj_mat, pop_size = 10, alpha = 1, beta = 2, rh = 0.1, com = 1):
        super().__init__(adj_mat)
        self.pop_size = pop_size
        self.alpha = alpha
        self.beta = beta
        self.rh = rh
        self.com = com

        self.pher_matrix = np.random.rand(np.shape(self.adj_mat)[0], np.shape(self.adj_mat)[1])

    def get_probability(self):
        prob_matrix = self.adj_mat.copy()
        for i, row in enumerate(prob_matrix):
            for j, element in enumerate(row):
                if row[j] == 11:
                    row[j] = 0    
                else:
                    denominator = 0
                    for m, dist in enumerate(row):
                        if dist != 11 and dist != 0:
                            denominator += self.pher_matrix[i, m]**self.alpha * self.adj_mat[i, m]**self.beta 
                    row[j] = self.pher_matrix[i, j]**self.alpha * element**self.beta / denominator

        for i in range(np.shape(prob_matrix)[0]):
            sum = 0
            for j in range(np.shape(prob_matrix)[1]):
                if prob_matrix[i, j] != 0:
                    prob_matrix[i, j] = sum + prob_matrix[i, j]
                    sum = prob_matrix[i, j]

        return prob_matrix
    
    def update_pher(self, delta_pher):
        self.pher_matrix = self.pher_matrix * (1 - self.rh) + delta_pher

    def update_swarm(self):
        current_solutions = []
        prob_matrix = self.get_probability()
        for i in range(self.pop_size):
            visited = []
            gamilton_tour = []
            node = 0
            while node not in visited:
                prob = random.uniform(0, 1)
                ind = np.where(prob_matrix[node] >= prob)[0][0]
                if ind not in visited:
                    visited.append(node)
                    found_edge = [node, ind]
                    gamilton_tour.append(found_edge)
                    node = ind
                if len(gamilton_tour) == np.shape(prob_matrix)[0] - 1:
                    gamilton_tour.append([gamilton_tour[-1][1], gamilton_tour[0][0]])
                    break
            current_solutions.append(gamilton_tour)

        way_cost_matrix = np.zeros((np.shape(self.adj_mat)[0], np.shape(self.adj_mat)[0]))
        for tour in current_solutions:
            for p, direct in enumerate(tour):
                way_cost_matrix[direct[0], direct[1]] += self.com / self.get_distance(tour[:p + 1])

        self.update_pher(way_cost_matrix)

        return current_solutions
