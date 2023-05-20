import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import networkx as nx

class NetworkGraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Network Graph")
        self.resize(800, 600)

        # Create an empty graph
        self.graph = nx.Graph()

        # Add initial nodes
        initial_nodes = [
            (1, "Node 1", 0, 0),
            (2, "Node 2", 1, 1),
            (3, "Node 3", 2, 0)
        ]
        for node in initial_nodes:
            node_id, node_label, x, y = node
            self.graph.add_node(node_id, label=node_label, x=x, y=y)

        # Create the Matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        # Create a layout and add the canvas to it
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Create a context menu for adding edges
        self.context_menu = self.createContextMenu()

        # Register the mouse click events
        self.canvas.mpl_connect('button_press_event', self.add_node)
        self.canvas.mpl_connect('button_press_event', self.show_context_menu)

        # Draw the initial graph
        self.draw_graph()

    def createContextMenu(self):
        context_menu = self.canvas.register_context_menu()

        # Add an action for adding edges
        add_edge_action = context_menu.addAction("Add Edge")
        add_edge_action.triggered.connect(self.add_edge)

        return context_menu

    def add_node(self, event):
        if event.button == 1:  # Left mouse button
            x, y = event.xdata, event.ydata
            node_id = len(self.graph.nodes) + 1
            node_label = f"Node {node_id}"
            self.graph.add_node(node_id, label=node_label, x=x, y=y)
            self.draw_graph()

    def add_edge(self):
        selected_nodes = self.context_menu.selected_nodes
        if len(selected_nodes) == 2:
            source, target = selected_nodes
            self.graph.add_edge(source, target)
            self.draw_graph()

    def draw_graph(self):
        self.figure.clear()
        pos = {node: (data['x'], data['y']) for node, data in self.graph.nodes.items()}
        nx.draw(self.graph, pos, with_labels=True, node_color='lightblue', ax=self.figure.gca())
        nx.draw_networkx_edges(self.graph, pos, edge_color='gray', ax=self.figure.gca())
        self.canvas.draw()

    def show_context_menu(self, event):
        if event.button == 3:  # Right mouse button
            x, y = event.xdata, event.ydata
            selected_node = None
            for node, data in self.graph.nodes.items():
                node_x, node_y = data['x'], data['y']
                if abs(x - node_x) < 0.05 and abs(y - node_y) < 0.05:
                    selected_node = node
                    break
            self.context_menu.selected_nodes = [selected_node] if selected_node else []
            self.context_menu

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NetworkGraphWindow()
    window.show()
    sys.exit(app.exec())


