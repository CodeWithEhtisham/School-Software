
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

import sys
from os import path
from PyQt5.uic import loadUiType

FORM_MAIN, _ = loadUiType('add_class.ui')


class AddClassWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
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
    window = AddClassWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
