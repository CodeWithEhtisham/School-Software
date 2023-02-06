
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

FORM_MAIN, _ = loadUiType('ui/add_class.ui')


class AddClassWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()

        self.Handle_Buttons()

     # HANDLE BUTTONS
    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.save_class)
        self.btn_cancel.clicked.connect(self.close)

    def save_class(self):
        class_name = self.txt_class.text()
        if class_name:
            try:
                self.db.insert(
                    table_name='classes',
                    columns="class_name",
                    values=f"'{class_name}'")
                QMessageBox.information(self, "Success", "Class added successfully")
                self.close()
            except Exception as e:
                QMessageBox.information(self, "Error", str(e))
        else:
            QMessageBox.information(self, "Error", "Class name is required")


    # def home(self):
    #     self.stackedWidget.setCurrentWidget(self.home_page)

    # def students(self):
    #     self.stackedWidget.setCurrentWidget(self.students_page)

    # def add_student(self):
    #     self.add_student_window = AddStudnetWindow()
    #     self.add_student_window.show()


def main():
    app = QApplication(sys.argv)
    window = AddClassWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
