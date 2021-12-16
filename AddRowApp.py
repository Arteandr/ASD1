from PyQt5 import QtWidgets
import Designs.AddRowForm as ar


class AddRowApp(QtWidgets.QMainWindow, ar.Ui_AddRowWindow):
    def __init__(self, table):
        super().__init__()
        self.setupUi(self)

        self.add_row_confirm_btn.clicked.connect(self.btn_click)

    def btn_click(self):
        if not self.is_full():
            return

        print("full")
        self.hide()
        self.clear_inputs()
        pass

    def is_full(self) -> bool:
        state = True

        if len(self.id_input.toPlainText().strip()) < 1 or len(self.name_input.toPlainText().strip()) < 1 or len(self.age_input.toPlainText().strip()) < 1:
            state = False

        return state

    def clear_inputs(self):
        self.id_input.setText(None)
        self.name_input.setText(None)
        self.age_input.setText(None)
