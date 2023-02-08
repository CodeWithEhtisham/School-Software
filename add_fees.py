
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

FORM_MAIN, _ = loadUiType('ui/add_fees.ui')


class AddFeesWindow(QMainWindow, FORM_MAIN):
    def __init__(self,std_id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.std_id = std_id
        self.db = DBHandler()
        self.lbl_student_name.setText(
            self.db.select(
                table_name='students',
                columns="name",
                condition=f"id = '{self.std_id}'")[0][0])
        self.txt_add_fee_date.setDate(QtCore.QDate.currentDate())
        # self.Handle_Buttons()

     # HANDLE BUTTONS
    # def Handle_Buttons(self):
    #     self.btn_home.clicked.connect(self.home)
    #     self.btn_students.clicked.connect(self.students)
    #     self.btn_add_student.clicked.connect(self.add_student)
    #     # self.btn_driver.clicked.connect(self.Driver)
    #     # self.btn_admin.clicked.connect(self.Admin)

    # def home(self):
    #     self.stackedWidget.setCurrentWidget(self.home_page)

    # def students(self):
    #     self.stackedWidget.setCurrentWidget(self.students_page)

    # def add_student(self):
    #     self.add_student_window = AddStudnetWindow()
    #     self.add_student_window.show()


def main():
    app = QApplication(sys.argv)
    window = AddFeesWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
