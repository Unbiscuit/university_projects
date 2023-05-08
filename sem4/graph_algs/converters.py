import numpy as np
from scipy.spatial import distance


def get_positions(node_dict):
    positions = []
    for node in node_dict.values():
        positions.append([node._x, node._y])
    return positions


def get_directions(directions_list):
    directions = []
    for direction in directions_list.keys():
        directions.append(list(direction))
    return directions


def get_adj_mat(positions, directions):
    adj_mat = np.ones((len(positions), len(positions))) + 10
    for direction in directions:
        adj_mat[direction[0], direction[1]] = distance.euclidean(positions[direction[0]], positions[direction[1]])
    return adj_mat