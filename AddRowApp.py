from PyQt5 import QtWidgets
import Designs.AddRowForm as ar
from Row import Row


class AddRowApp(QtWidgets.QMainWindow, ar.Ui_AddRowWindow):
    def __init__(self, main):
        super().__init__()
        self.setupUi(self)

        self.main = main

        self.add_row_confirm_btn.clicked.connect(self.btn_click)

    def btn_click(self):
        if not self.is_full():
            return

        if not self.is_num(self.age_input.toPlainText().strip()) or not self.is_num(
                self.id_input.toPlainText().strip()):
            return

        if self.main.id_exist(int(self.id_input.toPlainText().strip())):
            return

        self.add_to_table()
        self.hide()
        self.clear_inputs()
        pass

    def add_to_table(self):
        try:
            row = self.main.src_table.rowCount()
            self.main.src_table.insertRow(row)

            self.main.src_table.setItem(row, 0, QtWidgets.QTableWidgetItem(self.id_input.toPlainText().strip()))
            self.main.src_table.setItem(row, 1, QtWidgets.QTableWidgetItem(self.name_input.toPlainText().strip()))
            self.main.src_table.setItem(row, 2, QtWidgets.QTableWidgetItem(self.age_input.toPlainText().strip()))

            self.main.table_data.append(
                Row(
                    int(self.id_input.toPlainText().strip()),
                    str(self.name_input.toPlainText().strip()),
                    int(self.age_input.toPlainText().strip()),
                )
            )

            print(self.main.table_data[len(self.main.table_data) - 1].name, self.main.table_data[len(self.main.table_data) - 1].id, self.main.table_data[len(self.main.table_data) - 1].age)
        except Exception as e:
            print(e)

        self.main.set_rows_count_text()

    def is_full(self) -> bool:
        state = True

        if len(self.id_input.toPlainText().strip()) < 1 or len(self.name_input.toPlainText().strip()) < 1 or len(
                self.age_input.toPlainText().strip()) < 1:
            state = False

        return state

    def is_num(self, str: str) -> bool:
        state = True
        try:
            int(str)
        except Exception:
            state = False

        return state

    def clear_inputs(self):
        self.id_input.setText(None)
        self.name_input.setText(None)
        self.age_input.setText(None)
