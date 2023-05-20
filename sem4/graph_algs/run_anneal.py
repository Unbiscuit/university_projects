import sys
import matplotlib; matplotlib.use("Qt5Agg")
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from GUIs.sim_anneal_interface.interface import Ui_MainWindow
import numpy as np
from Algs.all_algs import SimAnneal, network_graph
import networkx as nx

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        super(MplCanvas, self).__init__(Figure(figsize=(width, height), dpi=dpi))
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111)
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

 
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('simAnneal')

        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.canvas1 = MplCanvas(self, width=8, height=8, dpi=80)
        self.ax = self.canvas1.ax
        self.toolbar1 = NavigationToolbar2QT(self.canvas1, self)
        self.verticalLayout_2.addWidget(self.toolbar1)
        self.verticalLayout_2.addWidget(self.canvas1)

        # Create an empty graph
        self.graph = nx.DiGraph()

        # Add initial nodes
        initial_nodes = [
            (1, "Node 1", 0, 0),
            (2, "Node 2", 1, 1),
            (3, "Node 3", 2, 0)
        ]

        for node in initial_nodes:
            node_id, node_label, x, y = node
            self.graph.add_node(node_id, label=node_label, x=x, y=y)

        initial_edges = [
            (1, 2,),
            (2, 3),
            (3, 1)
        ]
        for edge in initial_edges:
            source, target = edge
            weight = np.sqrt((self.graph.nodes[target]['x'] - self.graph.nodes[source]['x']) ** 2 + (self.graph.nodes[target]['y'] - self.graph.nodes[source]['y']) ** 2)
            self.graph.add_edge(source, target, weight=weight)

        self.canvas1.mpl_connect('button_press_event', self.add_node)
        self.canvas1.mpl_connect('button_press_event', self.add_edge)
        self.canvas1.mpl_connect('button_press_event', self.delete_edge)
        self.canvas1.mpl_connect('button_press_event', self.delete_node)

        # Store the selected nodes for adding edges
        self.selected_nodes = []

        # Display the graph
        self.draw_graph()

    def add_node(self, event):
        if event.button == 1:  # Left mouse button
            x, y = event.xdata, event.ydata
            node_id = len(self.graph.nodes) + 1
            node_label = f"Node {node_id}"
            self.graph.add_node(node_id, label=node_label, x=x, y=y)
            self.draw_graph()

    def add_edge(self, event):
        if event.button == 3:  # Right mouse button
            selected_node = None
            for node, data in self.graph.nodes.items():
                x, y = data['x'], data['y']
                if abs(event.xdata - x) < 0.05 and abs(event.ydata - y) < 0.05:
                    selected_node = node
                    break
            if selected_node is not None:
                if selected_node not in self.selected_nodes:
                    self.selected_nodes.append(selected_node)
                if len(self.selected_nodes) == 2:
                    source, target = self.selected_nodes
                    weight = np.sqrt((self.graph.nodes[target]['x'] - self.graph.nodes[source]['x']) ** 2 + (self.graph.nodes[target]['y'] - self.graph.nodes[source]['y']) ** 2)
                    self.graph.add_edge(source, target, weight=weight)
                    self.selected_nodes.clear()
                    self.draw_graph()

    def delete_edge(self, event):
        if event.button == 2:  # Middle mouse button
            selected_edge = None
            min_distance = float('inf')
            for edge in self.graph.edges:
                source = edge[0]
                target = edge[1]
                x1, y1 = self.graph.nodes[source]['x'], self.graph.nodes[source]['y']
                x2, y2 = self.graph.nodes[target]['x'], self.graph.nodes[target]['y']
                distance = (
                    (event.xdata - x1) ** 2 + (event.ydata - y1) ** 2 +
                    (event.xdata - x2) ** 2 + (event.ydata - y2) ** 2
                )
                if distance < min_distance:
                    selected_edge = edge
                    min_distance = distance
            if selected_edge is not None:
                self.graph.remove_edge(*selected_edge)
                self.draw_graph()

    def delete_node(self, event):
        if event.button == 2:  # Middle mouse button
            selected_node = None
            min_distance = float('inf')
            for node, data in self.graph.nodes.items():
                x, y = data['x'], data['y']
                distance = (event.xdata - x) ** 2 + (event.ydata - y) ** 2
                if distance < min_distance:
                    selected_node = node
                    min_distance = distance
            if selected_node is not None:
                self.graph.remove_node(selected_node)
                self.draw_graph()


    def draw_graph(self):
        pos = {node: (data['x'], data['y']) for node, data in self.graph.nodes.items()}
        nx.draw(self.graph, pos, ax=self.ax, with_labels=True, node_color='lightblue')
        nx.draw_networkx_edges(self.graph, pos, edge_color='gray')
        edge_labels = {edge: round(weight, 3) for edge, weight in nx.get_edge_attributes(self.graph, 'weight').items()}
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, ax=self.ax)
        self.canvas1.draw()



def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()


if __name__ == "__main__":
    main()