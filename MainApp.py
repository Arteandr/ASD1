from PyQt5 import QtWidgets
import Designs.MainForm as mf
from AddRowApp import AddRowApp


class MainApp(QtWidgets.QMainWindow, mf.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_row_form = AddRowApp(self.src_table)

        self.add_btn.clicked.connect(self.test)

    def test(self):
        self.add_row_form.show()
        return
