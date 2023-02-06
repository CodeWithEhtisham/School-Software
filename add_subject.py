
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

FORM_MAIN, _ = loadUiType('ui/add_subject.ui')


class AddSubjectWindow(QMainWindow, FORM_MAIN):
    def __init__(self,class_name):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db= DBHandler()
        self.class_id = self.db.select(
            table_name='classes',
            columns="id",
            condition=f"class_name='{class_name}'"
        )
        self.Handle_Buttons()

     # HANDLE BUTTONS
    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.save_subject)
        self.btn_cancel.clicked.connect(self.close)

    def save_subject(self):
        subject_name = self.txt_subject_name.text()
        passing_mark = self.txt_passing_marks.text()
        total_mark = self.txt_total_marks.text()
        if subject_name and passing_mark and total_mark:
            try:
                self.db.insert(
                    table_name='subjects',
                    columns="subject_name,passing_mark,total_mark,class_id",
                    values=f"'{subject_name}',{passing_mark},{total_mark},{self.class_id[0][0]}")
                QMessageBox.information(self, "Success", "Subject added successfully")
                self.close()
            except Exception as e:
                QMessageBox.information(self, "Error", str(e))
        else:
            QMessageBox.information(self, "Error", "All fields are required")


def main():
    app = QApplication(sys.argv)
    window = AddSubjectWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
