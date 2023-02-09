
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
        self.txt_expense_search.textChanged.connect(self.search_expense)
        self.btn_expense_refresh.clicked.connect(self.update_expense_table)
        self.class_table.doubleClicked.connect(self.update_subject_table)
        self.btn_refresh_student.clicked.connect(self.update_student_table)
        self.txt_search_student.textChanged.connect(self.search_student)


    def search_student(self):
        search = self.txt_search_student.text()
        print(search)
        if search != '':
            students = self.db.conn.execute(
                f"SELECT s.addmission_date,s.addmission_no,s.name,s.f_name,c.class_name,s.student_image,s.remaining_fee FROM students s INNER JOIN classes c ON s.class_id=c.id WHERE s.name LIKE '%{search}%' OR s.f_name LIKE '%{search}%' OR c.class_name LIKE '%{search}%' OR s.addmission_no LIKE '%{search}%' OR s.addmission_date LIKE '%{search}%'").fetchall()
            if students:
                self.update_student_table(students)
            else:
                self.students_table.setRowCount(0)
            # self.update_student_table(students)
        else:
            self.update_student_table()


    def update_student_table(self,students=None):
        print(students)
        if students is None or students==False:
            students = self.db.conn.execute(
                f"SELECT s.addmission_date,s.addmission_no,s.name,s.f_name,c.class_name,s.student_image,s.remaining_fee FROM students s INNER JOIN classes c ON s.class_id=c.id").fetchall()
        if students:
            ln=str(len(students))
            self.students_table.setRowCount(0)
            for row, form in enumerate(students):
                self.students_table.insertRow(row)
                for column, item in enumerate(form):
                    if column == 5:
                        if item == None:
                            item = 'images/default.png'
                        self.students_table.setCellWidget(
                            row, column, QLabel())
                        self.students_table.cellWidget(
                            row, column).setPixmap(QPixmap(item))
                        self.students_table.cellWidget(
                            row, column).setScaledContents(True)
                        self.students_table.cellWidget(
                            row, column).setAlignment(QtCore.Qt.AlignCenter)
                    else:
                        self.students_table.setItem(
                            row, column, QTableWidgetItem(str(item)))
                    # self.students_table.setItem(
                        # row, column, QTableWidgetItem(str(item)))
            self.lbl_total_students.setText(ln)


    def update_subject_table(self):
        class_id = self.class_table.currentItem().text()
        class_id = self.db.select(
            table_name='classes',
            columns="id",
            condition=f"class_name = '{class_id}'")
        class_id = class_id[0][0]
        data = self.db.select(
            table_name='subjects',
            columns="subject_name,passing_mark,total_mark",
            condition=f"class_id = '{class_id}'")
        if data:
            ln=str(len(data))
            self.subjects_table.setRowCount(0)
            for row, form in enumerate(data):
                self.subjects_table.insertRow(row)
                for column, item in enumerate(form):
                    self.subjects_table.setItem(
                        row, column, QTableWidgetItem(str(item)))
            self.lbl_total_subjects.setText(ln)
        else:
            self.subjects_table.setRowCount(0)
            self.lbl_total_subjects.setText("0")

    def update_class_table(self,classes=None):
        print("classes",classes)
        if classes is None or classes==False:
            classes = self.db.select_all(
                table_name='classes',
                columns="class_name",
            )
        if classes:
            ln=str(len(classes))
            self.class_table.setRowCount(0)
            for row, form in enumerate(classes):
                self.class_table.insertRow(row)
                for column, item in enumerate(form):
                    self.class_table.setItem(
                        row, column, QTableWidgetItem(str(item)))

            self.lbl_total_classes.setText(ln)



    def search_expense(self):
        search = self.txt_expense_search.text()
        data = self.db.select(
            table_name='expenses',
            columns="date,hoa,amount,payment_type,recipient_name,comment",
            condition=f"date LIKE '%{search}%' OR hoa LIKE '%{search}%' OR amount LIKE '%{search}%' OR payment_type LIKE '%{search}%' OR recipient_name LIKE '%{search}%' OR comment LIKE '%{search}%'")
        if data:
            self.update_expense_table(data)
        else:
            self.update_expense_table()

    # def udpate(self):
    #     self.update_expense_table()

    def update_expense_table(self,expense=None):
        if expense is None or expense==False:
            expense = self.db.select_all(
                table_name='expenses',
                columns="date,hoa,amount,payment_type,recipient_name,comment",
            )
        if expense:
            amount = 0
            self.expense_table.setRowCount(0)
            for row, form in enumerate(expense):
                self.expense_table.insertRow(row)
                amount += int(form[2])
                for column, item in enumerate(form):
                    self.expense_table.setItem(
                        row, column, QTableWidgetItem(str(item)))
            self.total_expense.setText(str(amount))
    
    def update_daily_report_table(self,reports=None):
        if reports is None or reports==False:
            reports = self.db.conn.execute(
                f"SELECT s.name,s.f_name,c.class_name,t.challan_no,t.paid_fee,t.remaining_fee,t.description FROM students s INNER JOIN classes c ON s.class_id=c.id INNER JOIN fee f ON s.id=f.std_id INNER JOIN transactions t ON f.id=t.fee_id WHERE t.date = '{QDate.currentDate().toString('dd/MM/yyyy')}' and t.paid_fee != 0").fetchall()
        # print(reports)
        if reports:
            reciceved = 0
            self.daily_reports_table.setRowCount(0)
            for row, form in enumerate(reports):
                self.daily_reports_table.insertRow(row)
                for column, item in enumerate(form):
                    if column == 4:
                        reciceved += int(item)
                    self.daily_reports_table.setItem(
                        row, column, QTableWidgetItem(str(item)))
            self.lbl_total_amount_received.setText(str(reciceved))
            remaining=self.db.conn.execute(
                # f"SELECT SUM(remaining_fee) FROM transactions WHERE date = '{QDate.currentDate().toString('dd/MM/yyyy')}'").fetchone()
                f"SELECT SUM(remaining_fee) FROM students").fetchone()
            self.lbl_total_amount_remaining.setText(str(remaining[0]))
            expense=self.db.conn.execute(
                f"SELECT SUM(amount) FROM expenses WHERE date = '{QDate.currentDate().toString('dd/MM/yyyy')}'").fetchone()
            print(expense)
            if expense[0] is not None:
                self.lbl_total_expense.setText(str(expense[0]))
                self.lbl_net_balance.setText(str(reciceved-expense[0]))
            else:
                self.lbl_total_expense.setText("0")
                self.lbl_net_balance.setText(str(reciceved))

    def home(self):
        self.stackedWidget.setCurrentWidget(self.home_page)

    def students(self):
        self.stackedWidget.setCurrentWidget(self.students_page)
        self.update_student_table()

    def student_class(self):
        self.stackedWidget.setCurrentWidget(self.class_page)
        self.update_class_table()

    def reports(self):
        self.stackedWidget.setCurrentWidget(self.reports_page)
        self.update_daily_report_table()

    def expenses(self):
        self.stackedWidget.setCurrentWidget(self.expense_page)
        self.update_expense_table()

    def settings(self):
        self.stackedWidget.setCurrentWidget(self.settings_page)

    def add_student(self):
        self.add_student_window = AddStudentWindow()
        self.add_student_window.show()
        self.add_student_window.btn_save.clicked.connect(self.update_student_table)

    def add_fees(self):
        selected_row = self.students_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(
                self, "Error", "Please select a student to view details")
            return
        registration_no = self.students_table.item(selected_row, 1).text()
        student_id = self.db.select(
            table_name='students',
            columns='id',
            condition=f"addmission_no='{registration_no}'"
        )[0][0]
        self.add_fees_window = AddFeesWindow(student_id)
        self.add_fees_window.show()

    def pay_fee(self):
        selected_row = self.students_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(
                self, "Error", "Please select a student to view details")
            return
        registration_no = self.students_table.item(selected_row, 1).text()
        self.pay_fee_window = PayFeeWindow(registration_no)
        self.pay_fee_window.show()

    def exam_details(self):
        self.exam_details_window = ExamDetailsWindow()
        self.exam_details_window.show()

    def add_class(self):
        self.add_class_window = AddClassWindow()
        self.add_class_window.show()
        self.add_class_window.btn_save.clicked.connect(self.update_class_table)

    def add_subject(self):
        selected_row = self.class_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(
                self, "Error", "Please select a class to add subject")
            return
        selected_class = self.class_table.item(selected_row, 0).text()
        if selected_class:
            self.add_subject_window = AddSubjectWindow(selected_class)
            self.add_subject_window.show()
            self.add_subject_window.btn_save.clicked.connect(
                self.update_subject_table)

    def add_expense(self):
        self.add_expense_window = ExpensesWindow()
        self.add_expense_window.show()
        self.add_expense_window.btn_save.clicked.connect(
            self.update_expense_table)

    def expense_type(self):
        self.expense_type_window = ExpenseTypeWindow()
        self.expense_type_window.show()

    def student_details(self):
        selected_row = self.students_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(
                self, "Error", "Please select a student to view details")
            return
        registration_no = self.students_table.item(selected_row, 1).text()
        student_id = self.db.select(
            table_name='students',
            columns='id',
            condition=f"addmission_no='{registration_no}'"
        )[0][0]
        self.student_details_window = StudentDetailWindow(student_id)
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
