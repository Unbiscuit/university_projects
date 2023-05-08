import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIntValidator, QPixmap

from GUI.interface import Ui_MainWindow
from PSO.pso import pso
from GUI.statepng import draw_state



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Partical swarm optimization')

        # disable some widgets
        self.plushundred_iters.setEnabled(False)
        self.plusone_iter.setEnabled(False)
        self.plusten_iters.setEnabled(False)
        self.plusthousand_iters.setEnabled(False)
        self.calculate_swarm.setEnabled(False)
        self.amount_of_iters.setEnabled(False)

        # set only int where needed
        validator = QIntValidator()
        self.inertia_weight.setValidator(validator)
        self.cognitive_coef.setValidator(validator)
        self.social_coef.setValidator(validator)
        self.partial_amount.setValidator(validator)
        
        # connect all buttons to functions
        self.initial_swarm_button.clicked.connect(self.initial_swarm)
        self.calculate_swarm.clicked.connect(self.update_swarm)
        self.plusone_iter.clicked.connect(self.one_iter)
        self.plusten_iters.clicked.connect(self.ten_iters)
        self.plushundred_iters.clicked.connect(self.hundred_iters)
        self.plusthousand_iters.clicked.connect(self.thousand_iters)

        # init swarm
        self.swarm = pso(int(self.partial_amount.text()), int(self.inertia_weight.text())/100, int(self.cognitive_coef.text())/100, int(self.social_coef.text())/100)

    def initial_swarm(self) -> None:
        # update info first time
        self.function_value.setText(f'{self.swarm.get_gbest_obj()}')
        x1x2 = self.swarm.get_gbest()
        self.Best_solution.setText(f'x1 = {x1x2[0]}, x2 = {x1x2[1]}')

        draw_state(self.swarm.get_particals(), self.swarm.get_velocity(), self.swarm.get_pbest(), self.swarm.get_gbest())
        pixmap = QPixmap('current_state.png')
        self.state_field.setPixmap(pixmap)

        self.inertia_weight.setReadOnly(True)
        self.cognitive_coef.setReadOnly(True)
        self.social_coef.setReadOnly(True)
        self.partial_amount.setReadOnly(True)

        self.plushundred_iters.setEnabled(True)
        self.plusone_iter.setEnabled(True)
        self.plusten_iters.setEnabled(True)
        self.plusthousand_iters.setEnabled(True)
        self.calculate_swarm.setEnabled(True)
        self.amount_of_iters.setEnabled(True)

        self.initial_swarm_button.setEnabled(False)

    def update_swarm(self) -> None:
        # update swarm n-times (according to qspinbox) and get info
        iters = self.amount_of_iters.value()
        for i in range(iters):
            self.swarm.update()


        self.function_value.setText(f'{self.swarm.get_gbest_obj()}')
        x1x2 = self.swarm.get_gbest()
        self.Best_solution.setText(f'x1 = {x1x2[0]}, x2 = {x1x2[1]}')
        self.previous_iters.setText(str(int(self.previous_iters.text()) + int(i + 1)))

        draw_state(self.swarm.get_particals(), self.swarm.get_velocity(), self.swarm.get_pbest(), self.swarm.get_gbest())
        pixmap = QPixmap('current_state.png')
        self.state_field.setPixmap(pixmap)

    def one_iter(self) -> None:
        self.amount_of_iters.setValue(1)

    def ten_iters(self) -> None:
        self.amount_of_iters.setValue(10)

    def hundred_iters(self) -> None:
        self.amount_of_iters.setValue(100)

    def thousand_iters(self) -> None:
        self.amount_of_iters.setValue(1000)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()