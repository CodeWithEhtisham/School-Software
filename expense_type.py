
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from db_handler import DBHandler
import sys
from os import path
from PyQt5.uic import loadUiType

FORM_MAIN, _ = loadUiType('ui/expense_type.ui')


class ExpenseTypeWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.btn_save.clicked.connect(self.save_expense_type)
        self.db = DBHandler()

    def save_expense_type(self):
        hoa=self.txt_expense_type.text()
        if hoa:
            try:
                self.db.insert(
                    table_name='expense_types',
                    columns="head_of_account",
                    values=f"'{hoa}'"
                )
                QMessageBox.information(self, "Success", "Expense Type Added Successfully")
                self.txt_expense_type.setText("")
                self.txt_expense_type.setFocus()
            except Exception as e:
                QMessageBox.information(self, "Error", str(e))
        else:
            QMessageBox.information(self, "Error", "Please Enter Expense Type")

def main():
    app = QApplication(sys.argv)
    window = ExpenseTypeWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
