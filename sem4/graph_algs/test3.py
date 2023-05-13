import sys
import networkx as nx
import pyqtgraph as pg
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class NetworkGraph(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Network Graph")
        self.setGeometry(100, 100, 800, 600)

        # Create a widget for the graph
        self.graph_widget = pg.GraphicsLayoutWidget()
        self.setCentralWidget(self.graph_widget)

        # Create a toolbar for adding, deleting, and moving nodes
        self.toolbar = self.addToolBar("Graph Toolbar")

        self.add_node_action = QAction("Add Node", self)
        self.add_node_action.triggered.connect(self.add_node)

        self.delete_node_action = QAction("Delete Node", self)
        self.delete_node_action.triggered.connect(self.delete_node)

        self.move_node_action = QAction("Move Node", self)
        self.move_node_action.setCheckable(True)
        self.move_node_action.toggled.connect(self.move_node)

        self.toolbar.addAction(self.add_node_action)
        self.toolbar.addAction(self.delete_node_action)
        self.toolbar.addAction(self.move_node_action)

        # Create a networkx graph
        self.graph = nx.Graph()

        # Add some nodes and edges to the graph
        self.graph.add_nodes_from([1, 2, 3, 4])
        self.graph.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1)])

        # Create a pyqtgraph PlotItem for drawing the graph
        self.plot_item = self.graph_widget.addPlot()
        self.plot_item.setAspectLocked(True)
        self.plot_item.showGrid(x=True, y=True)

        # Create a pyqtgraph GraphItem from the networkx graph
        self.graph_item = pg.GraphItem()
        self.plot_item.addItem(self.graph_item)

        pos = nx.spring_layout(self.graph)
        self.graph_item.setData(pos=pos, adj=self.graph.adjacency())

        # Show the main window
        self.show()

    def add_node(self):
        node_id, ok = QInputDialog.getInt(self, "Add Node", "Enter the node ID:")
        if ok:
            self.graph.add_node(node_id)
            pos = nx.spring_layout(self.graph)
            self.graph_item.setData(pos=pos, adj=self.graph.adjacency())

    def delete_node(self):
        node_id, ok = QInputDialog.getInt(self, "Delete Node", "Enter the node ID:")
        if ok:
            self.graph.remove_node(node_id)
            pos = nx.spring_layout(self.graph)
            self.graph_item.setData(pos=pos, adj=self.graph.adjacency())

    def move_node(self, checked):
        if checked:
            self.graph_item.setMovable(True)
        else:
            self.graph_item.setMovable(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    graph = NetworkGraph()
    sys.exit(app.exec())
