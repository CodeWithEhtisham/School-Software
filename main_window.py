
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
from expense_type import ExpenseTypeWindow
from exam_details import ExamDetailsWindow
from student_details import StudentDetailWindow
from monthly_report import MonthlyReportWindow
from yearly_report import YearlyReportWindow
from pay_fee import PayFeeWindow
from db_handler import DBHandler


FORM_MAIN, _ = loadUiType('ui/main_window.ui')


class MainWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()
        self.showMaximized()
        self.Handle_Buttons()
        # self.update()

     # HANDLE BUTTONS
    def Handle_Buttons(self):
        self.btn_logout.clicked.connect(self.logout)
        self.btn_change_password.clicked.connect(self.change_password)
        self.btn_edit_user.clicked.connect(self.edit_user)
        self.btn_add_school_details.clicked.connect(self.add_school_details)
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
        self.btn_expense_type.clicked.connect(self.expense_type)

        self.btn_monthly.clicked.connect(self.monthly_report)
        self.btn_yearly.clicked.connect(self.yearly_report)

        self.students_table.doubleClicked.connect(self.student_details)

        # self.btn_driver.clicked.connect(self.Driver)
        # self.btn_admin.clicked.connect(self.Admin)

    # def udpate(self):
    #     self.update_expense_table()

    def update_expense_table(self):
        data = self.db.select_all(
            table_name='expenses',
            columns="date,hoa,amount,payment_type,recipient_name"
        )
        if data:
            amount = 0
            self.expense_table.setRowCount(0)
            for row, form in enumerate(data):
                self.expense_table.insertRow(row)
                amount += int(form[2])
                for column, item in enumerate(form):
                    self.expense_table.setItem(
                        row, column, QTableWidgetItem(str(item)))
        self.total_expense.setText(str(amount))

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
        self.update_expense_table()

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
        self.add_expense_window.btn_save.clicked.connect(
            self.update_expense_table)

    def expense_type(self):
        self.expense_type_window = ExpenseTypeWindow()
        self.expense_type_window.show()

    def student_details(self):
        self.student_details_window = StudentDetailWindow()
        self.student_details_window.show()

    def logout(self):
        self.close()
        from login_page import LoginWindow
        self.login_window = LoginWindow()
        self.login_window.show()

    def change_password(self):
        from update_password import ChangePasswordWindow
        self.change_password_window = ChangePasswordWindow()
        self.change_password_window.show()

    def edit_user(self):
        from update_user_details import UpdateUserWindow
        self.update_user_window = UpdateUserWindow()
        self.update_user_window.show()

    def add_school_details(self):
        pass

    def monthly_report(self):
        self.monthly_report_window = MonthlyReportWindow()
        self.monthly_report_window.show()

    def yearly_report(self):
        self.yearly_report_window = YearlyReportWindow()
        self.yearly_report_window.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
