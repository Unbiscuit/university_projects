# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 640)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.functions_box = QtWidgets.QComboBox(parent=self.centralwidget)
        self.functions_box.setObjectName("functions_box")
        self.functions_box.addItem("")
        self.horizontalLayout_2.addWidget(self.functions_box, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.amount_of_chromosomes = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.amount_of_chromosomes.setObjectName("amount_of_chromosomes")
        self.horizontalLayout.addWidget(self.amount_of_chromosomes)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.mutation_chance = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.mutation_chance.setObjectName("mutation_chance")
        self.horizontalLayout_6.addWidget(self.mutation_chance)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.crossover_chance = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.crossover_chance.setObjectName("crossover_chance")
        self.horizontalLayout_4.addWidget(self.crossover_chance, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.max_gen_value = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.max_gen_value.setObjectName("max_gen_value")
        self.horizontalLayout_5.addWidget(self.max_gen_value)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.min_gen_value = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.min_gen_value.setMaxLength(32774)
        self.min_gen_value.setReadOnly(True)
        self.min_gen_value.setObjectName("min_gen_value")
        self.horizontalLayout_3.addWidget(self.min_gen_value, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.initial_population_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.initial_population_button.setObjectName("initial_population_button")
        self.verticalLayout_2.addWidget(self.initial_population_button)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.amount_of_generations = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.amount_of_generations.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.amount_of_generations.setMinimum(1)
        self.amount_of_generations.setMaximum(1000)
        self.amount_of_generations.setObjectName("amount_of_generations")
        self.horizontalLayout_8.addWidget(self.amount_of_generations)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.plusone_generation = QtWidgets.QPushButton(parent=self.centralwidget)
        self.plusone_generation.setObjectName("plusone_generation")
        self.horizontalLayout_7.addWidget(self.plusone_generation)
        self.plusten_generation = QtWidgets.QPushButton(parent=self.centralwidget)
        self.plusten_generation.setObjectName("plusten_generation")
        self.horizontalLayout_7.addWidget(self.plusten_generation)
        self.plushundred_generation = QtWidgets.QPushButton(parent=self.centralwidget)
        self.plushundred_generation.setObjectName("plushundred_generation")
        self.horizontalLayout_7.addWidget(self.plushundred_generation)
        self.plusthousand_generation = QtWidgets.QPushButton(parent=self.centralwidget)
        self.plusthousand_generation.setObjectName("plusthousand_generation")
        self.horizontalLayout_7.addWidget(self.plusthousand_generation)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.previous_generations = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.previous_generations.setReadOnly(True)
        self.previous_generations.setObjectName("previous_generations")
        self.horizontalLayout_9.addWidget(self.previous_generations)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.calculate_generation = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculate_generation.setObjectName("calculate_generation")
        self.verticalLayout_2.addWidget(self.calculate_generation)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.Best_solution = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.Best_solution.setReadOnly(True)
        self.Best_solution.setObjectName("Best_solution")
        self.verticalLayout_3.addWidget(self.Best_solution)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.function_value = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.function_value.setReadOnly(True)
        self.function_value.setObjectName("function_value")
        self.horizontalLayout_10.addWidget(self.function_value)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_11.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_14 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_5.addWidget(self.label_14)
        self.generation_table = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.generation_table.setObjectName("generation_table")
        self.generation_table.setColumnCount(3)
        self.generation_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.generation_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.generation_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.generation_table.setHorizontalHeaderItem(2, item)
        self.verticalLayout_5.addWidget(self.generation_table)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Параметры"))
        self.label_4.setText(_translate("MainWindow", "Функция"))
        self.functions_box.setItemText(0, _translate("MainWindow", "-12*x2 + 4*x1^ 2 + 4*x2^2 - 4*x1*x2"))
        self.label_2.setText(_translate("MainWindow", "Количество хромосом"))
        self.amount_of_chromosomes.setText(_translate("MainWindow", "100"))
        self.label_5.setText(_translate("MainWindow", "Вероятность мутации %"))
        self.mutation_chance.setText(_translate("MainWindow", "1"))
        self.label_3.setText(_translate("MainWindow", "Вероятность кроссинговера %"))
        self.crossover_chance.setText(_translate("MainWindow", "60"))
        self.label_7.setText(_translate("MainWindow", "Максимальное значение гена"))
        self.max_gen_value.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "Минимальное значение гена"))
        self.min_gen_value.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Управление"))
        self.initial_population_button.setText(_translate("MainWindow", "Рассчитать первую популяцию"))
        self.label_10.setText(_translate("MainWindow", "Количество поколений"))
        self.plusone_generation.setText(_translate("MainWindow", "1"))
        self.plusten_generation.setText(_translate("MainWindow", "10"))
        self.plushundred_generation.setText(_translate("MainWindow", "100"))
        self.plusthousand_generation.setText(_translate("MainWindow", "1000"))
        self.label_8.setText(_translate("MainWindow", "Номер поколения"))
        self.previous_generations.setText(_translate("MainWindow", "0"))
        self.calculate_generation.setText(_translate("MainWindow", "Рассчитать"))
        self.label_11.setText(_translate("MainWindow", "Результаты"))
        self.label_13.setText(_translate("MainWindow", "Лучшее решение:"))
        self.label_12.setText(_translate("MainWindow", "Значение функции"))
        self.label_14.setText(_translate("MainWindow", "Результат"))
        item = self.generation_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Хромосома 1"))
        item = self.generation_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Хромосома 2"))
        item = self.generation_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Результат"))
