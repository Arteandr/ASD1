from PyQt5 import QtWidgets
import Designs.StepForm as sf


class StepApp(QtWidgets.QMainWindow, sf.Ui_Stepform):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)

        self.main = main

        self.steps = []

        self.current_step = 0

        self.pushButton.clicked.connect(self.prev_btn_onclick)
        self.pushButton_2.clicked.connect(self.next_btn_onclick)

    def set_step_text(self):
        self.label.setText("Шаг: " + str(self.current_step + 1))

    def prev_btn_onclick(self):
        if self.current_step - 1 < 0: return

        self.print(self.current_step - 1)
        self.current_step -= 1
        self.set_step_text()

    def next_btn_onclick(self):
        if self.current_step + 1 > len(self.steps): return

        self.print(self.current_step + 1)
        self.current_step += 1
        self.set_step_text()

    def print(self, index=0):
        print(len(self.steps))
        if len(self.steps) <= 0: return

        self.tableWidget.setRowCount(0)

        for row in self.steps[index]:
            row_count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_count)

            self.tableWidget.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(row_count, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(row[2])))
