import sys
import matplotlib; matplotlib.use("Qt5Agg")
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import Qt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
import matplotlib.pyplot as plt
from netgraph import EditableGraph, Graph
from GUIs.nvms_interface.interface import Ui_MainWindow
import numpy as np
from scipy.spatial import distance
from Algs.all_algs import NVM
import converters
from mpl_toolkits.axisartist.axislines import Subplot

np.random.seed(300)
START_DIRECTIONS = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3)]

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        super(MplCanvas, self).__init__(Figure(figsize=(width, height), dpi=dpi))
        self.setParent(parent)
        self.ax = self.figure.add_subplot(111)
        self.plot_instance = EditableGraph(START_DIRECTIONS, 
                                    arrows=True, ax=self.ax, node_labels=True, edge_labels=True)
        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

 
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle('NVM')

        self.setFocusPolicy(Qt.FocusPolicy.ClickFocus)

        self.canvas1 = MplCanvas(self, width=8, height=8, dpi=80)
        self.toolbar1 = NavigationToolbar2QT(self.canvas1, self)
        self.verticalLayout_2.addWidget(self.toolbar1)
        self.verticalLayout_2.addWidget(self.canvas1)

        self.fig2 = plt.figure(figsize=(8, 8), dpi=80)
        ax = Subplot(self.fig2, 111)
        self.fig2.add_subplot(ax)
        self.canvas2 = FigureCanvasQTAgg(self.fig2)
        self.toolbar2 = NavigationToolbar2QT(self.canvas2, self)
        self.verticalLayout.addWidget(self.toolbar2)
        self.verticalLayout.addWidget(self.canvas2)

        self.do_alg_button.clicked.connect(self.get_tour)

    def remove_widgets(self):
        for i in reversed(range(self.verticalLayout_2.count())): 
            self.verticalLayout.itemAt(i).widget().setParent(None)

    def get_tour(self):
        self.remove_widgets()
        widget = QtWidgets.QWidget()
        widget.setSizePolicy(QtWidgets.QSizePolicy.setHorizontalPolicy(QtWidgets.QSizePolicy.Expanding), QtWidgets.QSizePolicy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding))
        self.verticalLayout.addWidget(widget)
        positions = converters.get_positions(self.canvas1.plot_instance.node_label_artists)
        directions =  converters.get_directions(self.canvas1.plot_instance.edge_label_artists)
        adj_mat = converters.get_adj_mat(positions, directions)
        nvm = NVM(adj_mat)
        tour = nvm.gamilton_tour_with_nvm()
        ax = self.fig2.axes[0]
        graph = Graph(tour, arrows=True, ax=ax, node_labels=True, edge_labels=True)
        self.fig2.canvas.draw()
        canvas = FigureCanvasQTAgg(self.fig2)
        toolbar = NavigationToolbar2QT(canvas, self)
        self.verticalLayout.addWidget(toolbar)
        self.verticalLayout.addWidget(canvas)





def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()


if __name__ == "__main__":
    main()