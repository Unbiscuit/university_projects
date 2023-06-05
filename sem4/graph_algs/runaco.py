import sys
import matplotlib; matplotlib.use("Qt5Agg")
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from GUIs.aco_interface.interface import Ui_MainWindow
import numpy as np
from Algs.all_algs import ACO_TSP, network_graph
import networkx as nx
from optional import find_unique_number


class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        super(MplCanvas, self).__init__(Figure(figsize=(width, height), dpi=dpi))
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111)
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

 
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    best_tour = 1000
    init_tour = True

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('NVM')

        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.canvas1 = MplCanvas(self, width=8, height=8, dpi=80)
        self.ax = self.canvas1.ax
        self.toolbar1 = NavigationToolbar2QT(self.canvas1, self)
        self.verticalLayout_2.addWidget(self.toolbar1)
        self.verticalLayout_2.addWidget(self.canvas1)

        self.G = nx.complete_graph(5)
        self.pos = nx.spring_layout(self.G)

        self.initialize_graph()
        self.update_graph()

        self.start_button.clicked.connect(self.do_aco)

        self.canvas1.mpl_connect('button_press_event', self.add_node)
        self.canvas1.mpl_connect('button_press_event', self.delete_node)

        self.canvas1.draw()


    def initialize_graph(self):
        for node1, position1 in self.pos.items():
            for node2, position2 in self.pos.items():
                if node1 != node2:
                    distance = np.linalg.norm(np.array(position1) - np.array(position2))
                    self.G.add_edge(node1, node2, weight=np.round(distance, 3))


    def add_node(self, event):
        if event.button == 1 and event.inaxes is not None:  # Triggered by left mouse button
            x, y = event.xdata, event.ydata
            list_of_nodes = list(self.G.nodes)
            if not list_of_nodes:
                node = 0
            else: 
                node = max(list_of_nodes) + 1
                node = find_unique_number(np.arange(node + 1), list_of_nodes)
            self.G.add_node(node)
            self.G.add_edges_from([(node, n) for n in self.G.nodes() if n != node])  # Exclude self-loop
            self.pos[node] = (x, y)

            # Connect new node with all existing nodes and assign edge weight as distance
            for n, position in self.pos.items():
                if n != node:
                    distance = np.linalg.norm(np.array(position) - np.array((x, y)))
                    self.G.add_edge(node, n, weight=np.round(distance, 3))

            self.update_graph()


    def delete_node(self, event):
        if event.button == 3 and event.inaxes is not None:  # Triggered by right mouse button
            x, y = event.xdata, event.ydata
            min_dist = float('inf')
            delete_node = None
            for node, position in self.pos.items():
                dist = ((position[0] - x) ** 2 + (position[1] - y) ** 2) ** 0.5
                if dist < min_dist:
                    min_dist = dist
                    delete_node = node

            if delete_node is not None:
                del self.pos[delete_node]
                self.G.remove_node(delete_node)
                self.update_graph()

    def update_graph(self):
        self.ax.cla()
        nx.draw(self.G, self.pos, ax=self.ax, with_labels=True, node_color='lightblue', node_size=800, font_size=12, font_weight='bold')
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, self.pos, ax=self.ax, edge_labels=edge_labels)
        self.canvas1.draw()


    def do_aco(self):
        if self.init_tour:
            n = max(list(self.G.nodes())) + 1
            adj_mat = np.ones((n, n)) + 10
            for edge, weight in nx.get_edge_attributes(self.G, 'weight').items():
                adj_mat[edge[0], edge[1]] = weight
                adj_mat[edge[1], edge[0]] = weight

            self.rows_to_keep = np.any(adj_mat != 11, axis=1)
            self.cols_to_keep = np.any(adj_mat != 11, axis=0)
            self.matrix_for_best_route = np.copy(adj_mat)
            adj_mat = adj_mat[self.rows_to_keep][:, self.cols_to_keep]

            self.alg = ACO_TSP(np.copy(adj_mat), int(self.population_line_edit.text()), int(self.pher_line_edit.text()), 
                        int(self.distance_line_edit.text()), float(self.cond_line_edit.text()), int(self.optimal_solution_line_edit.text()))
            self.init_tour = False
        
        for i in range(self.iter_spin_box.value()):

            tours = self.alg.update_swarm()
            obj = network_graph(self.matrix_for_best_route)

            this_round_best_distance = 1000
            tour = None

            for variant in tours:
                current_distance = obj.get_distance(variant)
                if current_distance < this_round_best_distance:
                    this_round_best_distance = current_distance
                    tour = variant

            if type(tour) == str:
                self.info_textedit.setText('Тур отсутствует')
            else:
                new_graph = self.G.copy()

                new_graph.clear_edges()
                num_false_values = len(self.rows_to_keep) - np.count_nonzero(self.rows_to_keep)
                first_false_index = np.argmax(~self.rows_to_keep)
                for move in tour:
                    if move[0] >= first_false_index and num_false_values != 0: move[0] = move[0] + num_false_values
                    if move[1] >= first_false_index and num_false_values != 0: move[1] = move[1] + num_false_values
                    new_graph.add_edge(move[0], move[1])

                self.ax.cla()
                nx.draw(new_graph, pos=self.pos, ax=self.ax, with_labels=True, node_color='lightblue')
                nx.draw_networkx_edges(new_graph, pos=self.pos, edge_color='gray')
                self.canvas1.draw()

                if obj.get_distance(tour) < self.best_tour: self.best_tour = this_round_best_distance
                self.info_textedit.setText(f'This tour distance = {this_round_best_distance}\nBest tour distance = {self.best_tour}')


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()


if __name__ == "__main__":
    main()