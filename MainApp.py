import copy
import time
import typing

from PyQt5 import QtWidgets
import Designs.MainForm as mf

from AddRowApp import AddRowApp
from GenerationApp import GenerationApp
from Sort import quicksort, quicksort_name, quicksort_age


class MainApp(QtWidgets.QMainWindow, mf.Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.out_data = list()
        self.setupUi(self)

        self.table_data = list()

        self.add_row_form = AddRowApp(self)
        self.generation_form = GenerationApp(self)

        self.add_btn.clicked.connect(self.add_btn_onclick)
        self.gen_btn.clicked.connect(self.generate_btn_onclick)
        self.sort_btn.clicked.connect(self.sort_btn_onclick)

    def sort_btn_onclick(self):
        try:
            selected_text = self.method_select.currentText().strip()
            if selected_text == "Быстрая сортировка":
                self.quicksort_emit()
            elif selected_text == "Прямыми включениями":
                self.inclusionsort_emit()
        except Exception as e:
            print(e)

    def quicksort_emit(self):
        if len(self.table_data) < 2:
            return
        try:
            self.out_data = copy.deepcopy(self.table_data)

            start_time = time.time()
            key = self.key_select.currentText().strip()
            print(key)
            if key == "ID":
                sravn, perest = quicksort(self.out_data, 0, len(self.out_data) - 1)
            elif key == "Name":
                sravn, perest = quicksort_name(self.out_data, 0, len(self.out_data) - 1)
            elif key == "Age":
                sravn, perest = quicksort_age(self.out_data, 0, len(self.out_data) - 1)

            end_time = time.time() - start_time
            self.set_ex_time(str(end_time))
            self.set_ex_perest(str(perest))
            self.set_ex_srav(str(sravn))
            self.print_out_table()

        except Exception as e:
            print(e)

    def set_ex_perest(self, src):
        self.label_6.setText("Количество перестановок: " + src)

    def set_ex_time(self, src):
        self.label_7.setText("Время: " + src + "s")

    def set_ex_srav(self, src):
        self.label_8.setText("Количество сравнений: " + src)

    def inclusionsort_emit(self):
        self.print_out_table()

    def add_btn_onclick(self):
        self.add_row_form.show()

    def generate_btn_onclick(self):
        self.generation_form.show()
        return

    def set_rows_count_text(self):
        self.row_count_label.setText(str(len(self.table_data)))

    def print_src_table(self):
        self.src_table.setRowCount(0)

        self.set_rows_count_text()

        for row in self.table_data:
            try:
                row_count = self.src_table.rowCount()
                self.src_table.insertRow(row_count)

                self.src_table.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(row.id)))
                self.src_table.setItem(row_count, 1, QtWidgets.QTableWidgetItem(row.name))
                self.src_table.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(row.age)))
            except Exception as e:
                print(e)

    def print_out_table(self):
        self.out_table.setRowCount(0)

        for row in self.out_data:
            try:
                row_count = self.out_table.rowCount()
                self.out_table.insertRow(row_count)

                self.out_table.setItem(row_count, 0, QtWidgets.QTableWidgetItem(str(row.id)))
                self.out_table.setItem(row_count, 1, QtWidgets.QTableWidgetItem(str(row.name)))
                self.out_table.setItem(row_count, 2, QtWidgets.QTableWidgetItem(str(row.age)))
            except Exception as e:
                print(e)

    def id_exist(self, id: int) -> bool:
        if len(self.table_data) < 1:
            return
        state = False

        for item in self.table_data:
            if int(item.id) == id:
                state = True
                break

        return state
