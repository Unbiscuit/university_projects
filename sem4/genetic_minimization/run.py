# This Python file uses the following encoding: utf-8
import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QTableWidgetItem, QHeaderView
from GUI.interface import Ui_MainWindow
from GA import GA


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowTitle('Genetic minimization')

        self.best_x1 = 0
        self.best_x2 = 0
        self.best_fit = 0

        self.button_is_checked = False

        self.amount_of_chromosomes.setReadOnly(False)
        self.crossover_chance.setReadOnly(False)
        self.mutation_chance.setReadOnly(False)
        self.min_gen_value.setReadOnly(False)
        self.max_gen_value.setReadOnly(False)

        # optimize header
        header = self.generation_table.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        # set only int where needed
        validator = QIntValidator()
        self.amount_of_chromosomes.setValidator(validator)
        self.mutation_chance.setValidator(validator)
        self.crossover_chance.setValidator(validator)
        self.max_gen_value.setValidator(validator)
        self.generation_table.setRowCount(int(self.amount_of_chromosomes.text()))
        
        # connect all buttons to functions
        self.initial_population_button.clicked.connect(self.show_initial_population)
        self.plusone_generation.clicked.connect(self.add_one_generation)
        self.plusten_generation.clicked.connect(self.add_ten_generations)
        self.plushundred_generation.clicked.connect(self.add_hundred_generations)
        self.plusthousand_generation.clicked.connect(self.add_thousand_generations)
        self.calculate_generation.clicked.connect(self.recalculate_generation)

    # show initial population in table, top genes in qtextedit and best fittness in qlineedit, set only read where needed
    def show_initial_population(self):
        if self.button_is_checked == False:
            self.population = GA.GA(int(self.amount_of_chromosomes.text()), int(self.crossover_chance.text())/100, int(self.mutation_chance.text())/100, float(self.min_gen_value.text()), float(self.max_gen_value.text()))
            speciemens = self.population.get_population()
            for i, row in enumerate(speciemens):
                for j, element in enumerate(row):
                    self.generation_table.setItem(i, j, QTableWidgetItem(str(element)))
            self.best_x1 = speciemens[0][0]
            self.best_x2 = speciemens[0][1]
            fit = speciemens[0][2]
            self.best_fit = fit
            self.Best_solution.append(f'x1 = {self.best_x1}, x2 = {self.best_x2}')
            self.function_value.setText(str(fit))
            self.previous_generations.setText(str(int(self.previous_generations.text()) + 1))
            self.button_is_checked = True
            self.amount_of_chromosomes.setReadOnly(True)
            self.crossover_chance.setReadOnly(True)
            self.mutation_chance.setReadOnly(True)
            self.min_gen_value.setReadOnly(True)
            self.max_gen_value.setReadOnly(True)

        else:
            pass
    
    # buttons to set amount of population for skip
    def add_one_generation(self):
        self.amount_of_generations.setValue(1)

    def add_ten_generations(self):
        self.amount_of_generations.setValue(10)

    def add_hundred_generations(self):
        self.amount_of_generations.setValue(100)

    def add_thousand_generations(self):
        self.amount_of_generations.setValue(1000)

    #  recalculate and show new population according to given options
    def recalculate_generation(self):
        for i in range(int(self.amount_of_generations.text())):
            self.population.tournament5()
            self.population.crossover()
            self.population.mutation(float(self.min_gen_value.text()), float(self.max_gen_value.text()))
            self.population.recalculate_fitness()
        speciemens = self.population.get_population()
        self.generation_table.clear()
        for i, row in enumerate(speciemens):
            for j, element in enumerate(row):
                self.generation_table.setItem(i, j, QTableWidgetItem(str(element)))
        
        dominant_fit = speciemens[0][2]
        dominant_x1 = speciemens[0][0]
        dominant_x2 = speciemens[0][1]
        if dominant_fit < self.best_fit:
            self.best_fit = dominant_fit
            self.best_x1 = dominant_x1
            self.best_x2 = dominant_x2
            self.Best_solution.clear()
            self.Best_solution.append(f'x1 = {self.best_x1}, x2 = {self.best_x2}')
            self.function_value.setText(str(self.best_fit))
            self.previous_generations.setText(str(int(self.previous_generations.text()) + int(self.amount_of_generations.text())))

        self.generation_table.setHorizontalHeaderLabels(["Хромосома 1", "Хромосома 2", "Результат"])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()