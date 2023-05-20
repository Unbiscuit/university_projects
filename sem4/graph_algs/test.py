import matplotlib.pyplot as plt
import networkx as nx

def add_node(event):
    if event.button == 1:  # Left mouse button
        x, y = event.xdata, event.ydata
        node_id = len(graph.nodes) + 1
        node_label = f"Node {node_id}"
        graph.add_node(node_id, label=node_label, x=x, y=y)
        draw_graph()

def add_edge(event):
    if event.button == 3:  # Right mouse button
        selected_node = None
        for node, data in graph.nodes.items():
            x, y = data['x'], data['y']
            if abs(event.xdata - x) < 0.05 and abs(event.ydata - y) < 0.05:
                selected_node = node
                break
        if selected_node is not None:
            if selected_node not in selected_nodes:
                selected_nodes.append(selected_node)
            if len(selected_nodes) == 2:
                source, target = selected_nodes
                graph.add_edge(source, target)
                selected_nodes.clear()
                draw_graph()



def delete_edge(event):
    if event.button == 2:  # Middle mouse button
        selected_edge = None
        min_distance = float('inf')
        for edge in graph.edges:
            source = edge[0]
            target = edge[1]
            x1, y1 = graph.nodes[source]['x'], graph.nodes[source]['y']
            x2, y2 = graph.nodes[target]['x'], graph.nodes[target]['y']
            a = event.xdata
            b = event.ydata
            distance = (
                (event.xdata - x1) ** 2 + (event.ydata - y1) ** 2 +
                (event.xdata - x2) ** 2 + (event.ydata - y2) ** 2
            )
            if distance < min_distance:
                selected_edge = edge
                min_distance = distance
        if selected_edge is not None:
            graph.remove_edge(*selected_edge)
            draw_graph()

def delete_node(event):
    if event.button == 2:  # Middle mouse button
        selected_node = None
        min_distance = float('inf')
        for node, data in graph.nodes.items():
            x, y = data['x'], data['y']
            distance = (event.xdata - x) ** 2 + (event.ydata - y) ** 2
            if distance < min_distance:
                selected_node = node
                min_distance = distance
        if selected_node is not None:
            graph.remove_node(selected_node)
            draw_graph()


def draw_graph():
    plt.clf()  # Clear the current figure
    pos = {node: (data['x'], data['y']) for node, data in graph.nodes.items()}
    nx.draw(graph, pos, with_labels=True, node_color='lightblue')
    nx.draw_networkx_edges(graph, pos, edge_color='gray')
    plt.draw()

# Create an empty graph
graph = nx.Graph()

# Add initial nodes
initial_nodes = [
    (1, "Node 1", 0, 0),
    (2, "Node 2", 1, 1),
    (3, "Node 3", 2, 0)
]
for node in initial_nodes:
    node_id, node_label, x, y = node
    graph.add_node(node_id, label=node_label, x=x, y=y)

# Add initial edges
initial_edges = [
    (1, 2),
    (2, 3),
    (3, 1)
]
for edge in initial_edges:
    source, target = edge
    graph.add_edge(source, target)

# Create a figure and register the mouse click events
fig = plt.figure()
fig.canvas.mpl_connect('button_press_event', add_node)
fig.canvas.mpl_connect('button_press_event', add_edge)
fig.canvas.mpl_connect('button_press_event', delete_edge)
fig.canvas.mpl_connect('button_press_event', delete_node)
fig.canvas.mpl_connect('button_press_event', move_node)

# Store the selected nodes for adding edges
selected_nodes = []

# Display the graph
draw_graph()
plt.show()
