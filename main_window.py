
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
from add_student import AddStudentWindow
from add_fees import AddFeesWindow
from add_class import AddClassWindow
from add_subject import AddSubjectWindow
from expenses import ExpensesWindow
from exam_details import ExamDetailsWindow
from student_details import StudentDetailWindow
from pay_fee import PayFeeWindow

FORM_MAIN, _ = loadUiType('ui/main_window.ui')


class MainWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.showMaximized()
        self.Handle_Buttons()

     # HANDLE BUTTONS
    def Handle_Buttons(self):
        self.btn_home.clicked.connect(self.home)
        self.btn_students.clicked.connect(self.students)
        self.btn_class.clicked.connect(self.student_class)
        self.btn_reports.clicked.connect(self.reports)
        self.btn_expense.clicked.connect(self.expenses)
        self.btn_settings.clicked.connect(self.settings)

        self.btn_add_student.clicked.connect(self.add_student)
        self.btn_add_fees.clicked.connect(self.add_fees)
        self.btn_add_result.clicked.connect(self.exam_details)
        self.btn_pay_fee.clicked.connect(self.pay_fee)

        self.btn_add_class.clicked.connect(self.add_class)
        self.btn_add_subject.clicked.connect(self.add_subject)

        self.btn_add_expense.clicked.connect(self.add_expense)

        self.students_table.doubleClicked.connect(self.student_details)


        # self.btn_driver.clicked.connect(self.Driver)
        # self.btn_admin.clicked.connect(self.Admin)

    def home(self):
        self.stackedWidget.setCurrentWidget(self.home_page)

    def students(self):
        self.stackedWidget.setCurrentWidget(self.students_page)

    def student_class(self):
        self.stackedWidget.setCurrentWidget(self.class_page)

    def reports(self):
        self.stackedWidget.setCurrentWidget(self.reports_page)

    def expenses(self):
        self.stackedWidget.setCurrentWidget(self.expense_page)

    def settings(self):
        self.stackedWidget.setCurrentWidget(self.settings_page)


    def add_student(self):
        self.add_student_window = AddStudentWindow()
        self.add_student_window.show()

    def add_fees(self):
        self.add_fees_window = AddFeesWindow()
        self.add_fees_window.show()

    def pay_fee(self):
        self.pay_fee_window = PayFeeWindow()
        self.pay_fee_window.show()

    def exam_details(self):
        self.exam_details_window = ExamDetailsWindow()
        self.exam_details_window.show()

    def add_class(self):
        self.add_class_window = AddClassWindow()
        self.add_class_window.show()

    def add_subject(self):
        self.add_subject_window = AddSubjectWindow()
        self.add_subject_window.show()

    def add_expense(self):
        self.add_expense_window = ExpensesWindow()
        self.add_expense_window.show()

    def student_details(self):
        self.student_details_window = StudentDetailWindow()
        self.student_details_window.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
