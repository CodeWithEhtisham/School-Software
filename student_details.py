
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
from add_fees import AddFeesWindow
from exam_details import ExamDetailsWindow
from pay_fee import PayFeeWindow

FORM_MAIN, _ = loadUiType('ui/student_details.ui')


class StudentDetailWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

     # HANDLE BUTTONS
    def Handle_Buttons(self):
        self.btn_student.clicked.connect(self.student)
        self.btn_fees.clicked.connect(self.fees)
        self.btn_results.clicked.connect(self.results)
        
        self.btn_add_fees.clicked.connect(self.add_fees)
        self.btn_add_result.clicked.connect(self.exam_details)
        self.btn_pay_fee.clicked.connect(self.pay_fee)
        # self.btn_driver.clicked.connect(self.Driver)
        # self.btn_admin.clicked.connect(self.Admin)

    def student(self):
        self.stackedWidget.setCurrentWidget(self.student_page)

    def fees(self):
        self.stackedWidget.setCurrentWidget(self.fees_page)

    def results(self):
        self.stackedWidget.setCurrentWidget(self.result_page)

    def add_fees(self):
        self.add_fees_window = AddFeesWindow()
        self.add_fees_window.show()

    def pay_fee(self):
        self.pay_fee_window = PayFeeWindow()
        self.pay_fee_window.show()

    def exam_details(self):
        self.exam_details_window = ExamDetailsWindow()
        self.exam_details_window.show()


def main():
    app = QApplication(sys.argv)
    window = StudentDetailWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
