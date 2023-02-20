
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui, QtPrintSupport
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
from school_details import SchoolDetailsWindow
from update_class import UpdateClassWindow
from update_subject import UpdateSubjectWindow
from db_handler import DBHandler
from update_expense import UpdateExpensesWindow
from update_student import UpdateStudentWindow
import datetime


FORM_MAIN, _ = loadUiType('ui/main_window.ui')

class MainWindow(QMainWindow, FORM_MAIN):
    def __init__(self,status):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()
        self.is_admin = status
        self.showMaximized()
        self.Handle_Buttons()
        # self.update()
        self.home()

        self.students_table.setColumnWidth(0, 120)
        self.students_table.setColumnWidth(1, 170)
        self.students_table.setColumnWidth(2, 180)
        self.students_table.setColumnWidth(3, 180)
        self.students_table.setColumnWidth(4, 120)
        self.students_table.setColumnWidth(5, 120)
        self.students_table.setColumnWidth(6, 140)
        self.students_table.setColumnWidth(7, 120)

        # REPORTS TABLE
        self.daily_reports_table.setColumnWidth(0, 180)
        self.daily_reports_table.setColumnWidth(1, 180)

        # EXPENSE TABLE
        self.expense_table.setColumnWidth(3, 200)
        self.expense_table.setColumnWidth(4, 200)
        self.expense_table.setColumnWidth(5, 300)
        self.report_from_date.setDate(QDate.currentDate())
        self.report_to_date.setDate(QDate.currentDate())

     # HANDLE BUTTONS

    def Handle_Buttons(self):
        self.btn_logout.clicked.connect(self.logout)
        self.btn_change_password.clicked.connect(self.change_password)
        self.btn_edit_user.clicked.connect(self.edit_user)
        self.btn_add_school_details.clicked.connect(self.add_school_details)
        # self.btn_add_user.clicked.connect(self.add_users)
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

        self.btn_reports_print.clicked.connect(self.print_daily_report)
        self.btn_print_expense.clicked.connect(self.print_expense)
        self.btn_print_student.clicked.connect(self.print_students)

        self.students_table.doubleClicked.connect(self.student_details)

        self.txt_expense_search.textChanged.connect(self.search_expense)
        self.btn_expense_refresh.clicked.connect(self.update_expense_table)
        self.class_table.doubleClicked.connect(self.update_subject_table)
        self.btn_refresh_student.clicked.connect(self.update_student_table)
        self.txt_search_student.textChanged.connect(self.search_student)
        self.select_class.currentIndexChanged.connect(
            self.student_search_class)
        self.btn_edit_class.clicked.connect(self.edit_class)
        self.btn_edit_subject.clicked.connect(self.edit_subject)
        self.btn_edit_expense.clicked.connect(self.edit_expense)
        self.btn_edit_student.clicked.connect(self.edit_student)
        self.btn_date_search.clicked.connect(self.search_date_report)
        self.btn_reports_refresh.clicked.connect(
            self.update_daily_report_table)
        self.txt_search_report.textChanged.connect(self.search_report)
        self.btn_defaulters.clicked.connect(self.defaulters)
        self.btn_add_user.clicked.connect(self.add_user)
        

    def add_user(self):
        from create_user import CreateUserWindow
        self.add_user_window = CreateUserWindow(1)
        self.add_user_window.show()
        self.add_user_window.btn_save.clicked.connect(self.user_table_update)

    def user_status(self):
        if self.is_admin==0:
            self.btn_edit_user.show()
            self.btn_add_school_details.show()
            # self.btn_add_user.show()
        else:
            self.btn_edit_user.hide()
            self.btn_add_school_details.hide()
            # self.btn_add_user.hide()

    def defaulters(self):
        # get only last transaction of each student
        # reports = self.db.conn.execute(
        #     f"SELECT s.name,s.f_name,c.class_name,t.challan_no,t.paid_fee,s.remaining_fee,t.date FROM students s INNER JOIN classes c ON s.class_id=c.id INNER JOIN fee f ON s.id=f.std_id INNER JOIN transactions t ON f.id=t.fee_id ORDER BY s.remaining_fee DESC").fetchall()
        first_date_of_this_month = datetime.date.today().replace(day=1).strftime("%Y/%m/%d")
        print(first_date_of_this_month)

        query = f"""SELECT s.name, s.f_name, c.class_name, t.challan_no, t.paid_fee, s.remaining_fee, MAX(t.date) as last_transaction_date ,t.id
FROM students s 
LEFT JOIN fee f ON s.id = f.std_id 
LEFT JOIN transactions t ON f.id = t.fee_id   
INNER JOIN classes c ON s.class_id = c.id 
WHERE t.date < '{first_date_of_this_month}' 
  AND t.id = (SELECT MAX(id) FROM transactions WHERE fee_id = f.id)
GROUP BY s.id, s.name, s.f_name, c.class_name, t.challan_no, t.paid_fee, s.remaining_fee;
        """
        print(query)
# SELECT s.name, s.f_name, c.class_name, t.challan_no, t.paid_fee, s.remaining_fee, MAX(t.date) as last_transaction_date ,t.id
# FROM students s 
# LEFT JOIN fee f ON s.id = f.std_id 
# LEFT JOIN transactions t ON f.id = t.fee_id   
# INNER JOIN classes c ON s.class_id = c.id 
# WHERE t.date < '2023/02/01' 
#   AND t.id = (SELECT MAX(id) FROM transactions WHERE fee_id = f.id)
# GROUP BY s.id, s.name, s.f_name, c.class_name, t.challan_no, t.paid_fee, s.remaining_fee;
        reports = self.db.conn.execute(query).fetchall()
        print(reports)
        if reports:
            # reciceved = 0
            self.daily_reports_table.setRowCount(0)
            for row, form in enumerate(reports):
                self.daily_reports_table.insertRow(row)
                for column, item in enumerate(form):
                    # if column == 4 or column == 3:
                    #     self.daily_reports_table.setItem(
                    #         row, column, QTableWidgetItem(str('-')))
                    #     # continue
                    # else:
                        # reciceved += int(item)
                    self.daily_reports_table.setItem(
                        row, column, QTableWidgetItem(str(item)))

            # self.lbl_total_amount_received.setText(str(reciceved))
            # remaining = self.db.conn.execute(
            #     # f"SELECT SUM(remaining_fee) FROM transactions WHERE date = '{QDate.currentDate().toString('yyyy/MM/dd')}'").fetchone()
            #     f"SELECT SUM(remaining_fee) FROM students").fetchone()
            # self.lbl_total_amount_remaining.setText(str(remaining[0]))
            # expense = self.db.conn.execute(
            #     f"SELECT SUM(amount) FROM expenses WHERE date = '{QDate.currentDate().toString('yyyy/MM/dd')}'").fetchone()
            # # print(expense)
            # if expense[0] is not None:
            #     self.lbl_total_expense.setText(str(expense[0]))
            #     self.lbl_net_balance.setText(str(reciceved-expense[0]))
            # else:
            #     self.lbl_total_expense.setText("0")
            #     self.lbl_net_balance.setText(str(reciceved))

    def edit_student(self):
        row = self.students_table.currentRow()
        if row == -1:
            QMessageBox.warning(
                self, 'Warning', 'Please select a student to edit')
            return
        reg_no = self.students_table.item(row, 1).text()
        student_id = self.db.conn.execute(
            f"SELECT id FROM students WHERE addmission_no='{reg_no}'").fetchone()[0]
        self.edit_student_window = UpdateStudentWindow(student_id)
        self.edit_student_window.show()
        self.edit_student_window.btn_save.clicked.connect(
            self.update_student_table)

    def edit_expense(self):
        row = self.expense_table.currentRow()
        if row == -1:
            QMessageBox.warning(
                self, 'Warning', 'Please select a expense to edit')
            return
        date = self.expense_table.item(row, 0).text()
        hoa = self.expense_table.item(row, 1).text()
        payment_type = self.expense_table.item(row, 3).text()
        recipient_name = self.expense_table.item(row, 4).text()
        expense_id = self.db.conn.execute(
            f"SELECT id FROM expenses WHERE date='{date}' and hoa='{hoa}' and payment_type='{payment_type}' and recipient_name='{recipient_name}'").fetchone()[0]
        self.edit_expense_window = UpdateExpensesWindow(expense_id)
        self.edit_expense_window.show()
        self.edit_expense_window.btn_save.clicked.connect(
            self.update_expense_table)
        self.edit_expense_window.btn_delete.clicked.connect(
            self.update_expense_table)

    def edit_subject(self):
        row = self.subjects_table.currentRow()
        if row == -1:
            QMessageBox.warning(
                self, 'Warning', 'Please select a subject to edit')
            return
        subject_name = self.subjects_table.item(row, 0).text()
        row = self.class_table.currentRow()
        class_name = self.class_table.item(row, 0).text()
        class_id = self.db.conn.execute(
            f"SELECT id FROM classes WHERE class_name='{class_name}'").fetchone()[0]
        subject_id = self.db.conn.execute(
            f"SELECT id FROM subjects WHERE subject_name='{subject_name}' and class_id={class_id}").fetchone()[0]
        self.edit_subject_window = UpdateSubjectWindow(subject_id)
        self.edit_subject_window.show()
        self.edit_subject_window.btn_save.clicked.connect(
            self.update_subject_table)

    def edit_class(self):
        row = self.class_table.currentRow()
        if row == -1:
            QMessageBox.warning(
                self, 'Warning', 'Please select a class to edit')
            return
        class_name = self.class_table.item(row, 0).text()
        class_id = self.db.conn.execute(
            f"SELECT id FROM classes WHERE class_name='{class_name}'").fetchone()[0]
        self.edit_class_window = UpdateClassWindow(class_id)
        self.edit_class_window.show()
        self.edit_class_window.btn_save.clicked.connect(
            self.update_class_table)

    def student_search_class(self):
        class_name = self.select_class.currentText()
        if class_name != 'Select Class':
            students = self.db.conn.execute(
                f"SELECT s.addmission_date,s.addmission_no,s.name,s.f_name,c.class_name,s.student_image,s.remaining_fee,status FROM students s INNER JOIN classes c ON s.class_id=c.id WHERE c.class_name LIKE '%{class_name}%'").fetchall()
            # print(students)
            if students:
                self.update_student_table(students)
            else:
                self.students_table.setRowCount(0)
        else:
            self.students_table.setRowCount(0)

    def search_student(self):
        search = self.txt_search_student.text()
        # print(search)
        if search != '':
            students = self.db.conn.execute(
                f"SELECT s.addmission_date,s.addmission_no,s.name,s.f_name,c.class_name,s.student_image,s.remaining_fee,status FROM students s INNER JOIN classes c ON s.class_id=c.id WHERE s.name LIKE '%{search}%' OR s.f_name LIKE '%{search}%' OR c.class_name LIKE '%{search}%' OR s.addmission_no LIKE '%{search}%' OR s.addmission_date LIKE '%{search}%' OR s.status LIKE '%{search}%'").fetchall()
            if students:
                self.update_student_table(students)
            else:
                self.students_table.setRowCount(0)
            # self.update_student_table(students)
        else:
            self.update_student_table()

    def update_student_table(self, students=None):
        if students == None or students == False or QtGui.QCloseEvent == False:
            students = self.db.conn.execute(
                f"SELECT s.addmission_date,s.addmission_no,s.name,s.f_name,c.class_name,s.student_image,s.remaining_fee,status FROM students s INNER JOIN classes c ON s.class_id=c.id").fetchall()
        if students:
            ln = str(len(students))
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

    def update_student_table_x_button(self, students=None):
        # if students == None or students == False or QtGui.QCloseEvent == False:
        students = self.db.conn.execute(
            f"SELECT s.addmission_date,s.addmission_no,s.name,s.f_name,c.class_name,s.student_image,s.remaining_fee,status FROM students s INNER JOIN classes c ON s.class_id=c.id").fetchall()
        if students:
            ln = str(len(students))
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
            ln = str(len(data))
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

    def update_class_table(self, classes=None):
        # print("classes", classes)
        if classes is None or classes == False:
            classes = self.db.select_all(
                table_name='classes',
                columns="class_name",
            )
        if classes:
            ln = str(len(classes))
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
            self.expense_table.setRowCount(0)
            self.total_expense.setText("0")

    # def udpate(self):
    #     self.update_expense_table()

    def update_expense_table(self, expense=None):
        if expense is None or expense == False:
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

    def update_daily_report_table(self, reports=None):
        if reports is None or reports == False:
            reports = self.db.conn.execute(
                f"SELECT s.name,s.f_name,c.class_name,t.challan_no,t.paid_fee,t.remaining_fee,t.description FROM students s INNER JOIN classes c ON s.class_id=c.id INNER JOIN fee f ON s.id=f.std_id INNER JOIN transactions t ON f.id=t.fee_id WHERE t.date = '{QDate.currentDate().toString('yyyy/MM/dd')}' and t.paid_fee != 0").fetchall()
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
            remaining = self.db.conn.execute(
                # f"SELECT SUM(remaining_fee) FROM transactions WHERE date = '{QDate.currentDate().toString('yyyy/MM/dd')}'").fetchone()
                f"SELECT SUM(remaining_fee) FROM students").fetchone()
            self.lbl_total_amount_remaining.setText(str(remaining[0]))
            expense = self.db.conn.execute(
                f"SELECT SUM(amount) FROM expenses WHERE date = '{QDate.currentDate().toString('yyyy/MM/dd')}'").fetchone()
            # print(expense)
            if expense[0] is not None:
                self.lbl_total_expense.setText(str(expense[0]))
                self.lbl_net_balance.setText(str(reciceved-expense[0]))
            else:
                self.lbl_total_expense.setText("0")
                self.lbl_net_balance.setText(str(reciceved))

    def search_date_report(self):
        from_date = self.report_from_date.date().toString('yyyy/MM/dd')
        to_date = self.report_to_date.date().toString('yyyy/MM/dd')
        reports = self.db.conn.execute(
            f"SELECT s.name,s.f_name,c.class_name,t.challan_no,t.paid_fee,t.remaining_fee,t.description FROM students s INNER JOIN classes c ON s.class_id=c.id INNER JOIN fee f ON s.id=f.std_id INNER JOIN transactions t ON f.id=t.fee_id WHERE t.date BETWEEN '{from_date}' and '{to_date}' and t.paid_fee != 0").fetchall()
        if reports:
            self.update_daily_report_table(reports)
        else:
            self.daily_reports_table.setRowCount(0)
            self.lbl_total_amount_received.setText("0")
            self.lbl_total_amount_remaining.setText("0")
            self.lbl_total_expense.setText("0")
            self.lbl_net_balance.setText("0")

    def search_report(self):
        search = self.txt_search_report.text()
        reports = self.db.conn.execute(
            f"SELECT s.name,s.f_name,c.class_name,t.challan_no,t.paid_fee,t.remaining_fee,t.description FROM students s INNER JOIN classes c ON s.class_id=c.id INNER JOIN fee f ON s.id=f.std_id INNER JOIN transactions t ON f.id=t.fee_id WHERE t.date = '{QDate.currentDate().toString('yyyy/MM/dd')}' and t.paid_fee != 0 and s.name LIKE '%{search}%' or s.f_name LIKE '%{search}%' or c.class_name LIKE '%{search}%' or t.challan_no LIKE '%{search}%' or t.description LIKE '%{search}%'").fetchall()
        if reports:
            self.update_daily_report_table(reports)
        else:
            self.daily_reports_table.setRowCount(0)
            self.lbl_total_amount_received.setText("0")
            self.lbl_total_amount_remaining.setText("0")
            self.lbl_total_expense.setText("0")
            self.lbl_net_balance.setText("0")

    def home(self):
        self.stackedWidget.setCurrentWidget(self.home_page)
        school_info = self.db.select_all(
            table_name='school_info',
            columns="school_name,contact,address,logo",
        )
        if school_info:
            self.lbl_school_name.setText(school_info[0][0])
            self.lbl_school_contact.setText(school_info[0][1])
            self.lbl_school_address.setText(school_info[0][2])
            self.lbl_logo.setPixmap(QPixmap(school_info[0][3]))
            self.lbl_logo.setScaledContents(True)

    def add_select_class(self):
        self.select_class.clear()
        self.select_class.addItem('Select Class')
        self.select_class.addItems([i[0] for i in self.db.conn.execute(
            f"SELECT class_name FROM classes").fetchall()])

    def students(self):
        self.stackedWidget.setCurrentWidget(self.students_page)
        self.add_select_class()
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

    def user_table_update(self):
        data = self.db.select(
            table_name='users',
            columns='name,email,contact,username,password',
            condition=f"is_admin != 0"
        )
        self.users_table.setRowCount(0)
        for row, form in enumerate(data):
            self.users_table.insertRow(row)
            for column, item in enumerate(form):
                self.users_table.setItem(row, column, QTableWidgetItem(str(item)))

    def settings(self):
        self.stackedWidget.setCurrentWidget(self.settings_page)
        self.user_table_update()


    def add_student(self):
        self.add_student_window = AddStudentWindow()
        self.add_student_window.show()
        self.add_student_window.btn_save.clicked.connect(
            self.update_student_table)

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
        self.add_fees_window.btn_save.clicked.connect(
            self.update_student_table)

    def pay_fee(self):
        selected_row = self.students_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(
                self, "Error", "Please select a student to view details")
            return
        registration_no = self.students_table.item(selected_row, 1).text()
        self.pay_fee_window = PayFeeWindow(registration_no)
        self.pay_fee_window.show()
        self.pay_fee_window.btn_save.clicked.connect(self.update_student_table)

    def exam_details(self):
        row = self.students_table.currentRow()
        if row == -1:
            QMessageBox.warning(
                self, "Error", "Please select a student to view details")
            return
        registration_no = self.students_table.item(row, 1).text()
        student_id = self.db.select(
            table_name='students',
            columns='id',
            condition=f"addmission_no='{registration_no}'"
        )[0][0]
        self.exam_details_window = ExamDetailsWindow(student_id)
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
        # print(student_id)
        self.student_details_window = StudentDetailWindow(student_id)
        self.student_details_window.show()
        # when pressin red x button on student details window
        self.student_details_window.closeEvent = self.update_student_table_x_button

        # self.student_details_window.edit_fee_window.btn_save.clicked.connect(
        #     self.update_student_table)
        # self.add_fees_window.btn_save.clicked.connect(
        #     self.update_student_table)
        # self.pay_fee_window.btn_save.clicked.connect(
        #     self.update_student_table)
        # self.school_leaving_window.btn_save.clicked.connect(
        #     self.update_student_table)

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
        self.add_school_window = SchoolDetailsWindow()
        self.add_school_window.show()

    # def add_users(self):
    #     self.add_users_window = CreateUserWindow()
    #     self.add_users_window.show()

    def monthly_report(self):
        self.monthly_report_window = MonthlyReportWindow()
        self.monthly_report_window.show()

    def yearly_report(self):
        self.yearly_report_window = YearlyReportWindow()
        self.yearly_report_window.show()

    # PRINT DAILY REPORTS
    def print_daily_report(self):
        school_info = self.db.select_all(
            table_name="school_info", columns="school_name, contact, address")

        filename = QFileDialog.getSaveFileName(
            self, "Save File", "", "PDF(*.pdf)")
        if filename[0]:
            printer = QtPrintSupport.QPrinter(
                QtPrintSupport.QPrinter.PrinterResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setPaperSize(QtPrintSupport.QPrinter.A4)
            printer.setPageMargins(
                1, 1, 1, 1, QtPrintSupport.QPrinter.Millimeter)
            printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
            printer.setOutputFileName(filename[0])
            document = QtGui.QTextDocument()
            style_sheet = """
                body {
                    width: 100vw;
                    height: 100vh;
                    margin: 0;
                    padding: 0;
                }
                h1 {
                    text-align: center;
                }
                h2 {
                    text-align: right;
                    font-weight: 400;
                    font-size: 12px;
                    margin: 0px;
                }
                h3 {
                    text-align: left;
                    margin: 1px;
                }
                p {
                    text-align: center;
                    font-size: 12px;
                }
                table {
                  border-collapse: collapse;
                  width: 100%;
                }
                th, td {
                    border: 1px solid black;
                    padding: 4px;
                    font-size: 10px;
                    text-align: left;
                }
                th {
                  background-color: #29b6f6;
                  font-weight: bold;
                  font-size: 10px;
                }
                
            """
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <body>
                <h1> """+school_info[0][0]+"""</h1>
                <p> """+school_info[0][2]+""" </p>
                <h2> Contact : """+school_info[0][1]+""" </h2>
                <h1> Daily Report </h1>
                <h3>Print Date: """+str(QDate.currentDate().toString('dd-MM-yyyy'))+"""</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Student Name</th>
                            <th>Father Name</th>
                            <th>Class</th>
                            <th>Challan No.</th>
                            <th>Paid Amount</th>
                            <th>Remaining Fee</th>
                            <th>Description</th>
                        </tr>
                    </thead>
                    <tbody style="font-size: 10px;">
            """
            for i in range(self.daily_reports_table.rowCount()):
                html += """<tr>"""
                for j in range(self.daily_reports_table.columnCount()):
                    html += """<td>"""
                    if self.daily_reports_table.item(i, j) is None:
                        html += """-</td>"""
                    else:
                        html += self.daily_reports_table.item(
                            i, j).text()+"</td>"
                html += "</tr>"
            html += """
                    </tbody>
    
                </table>
                
                <h2>Total Amount Received: """+self.lbl_total_amount_received.text()+"""</h2>
                <h2>Total Amount Remaining: """+self.lbl_total_amount_remaining.text()+"""</h2>
                <h2>Total Expense: """+self.lbl_total_expense.text()+"""</h2>
                <h2>Net Balance: """+self.lbl_net_balance.text()+"""</h2>
            </body>
            </html>
            """

            document.setDefaultStyleSheet(style_sheet)
            document.setHtml(html)
            document.print_(printer)
            QMessageBox.information(self, "Success", "PDF Saved Successfully")

    # PRINT EXPENSE
    def print_expense(self):
        school_info = self.db.select_all(
            table_name="school_info", columns="school_name, contact, address")
        filename = QFileDialog.getSaveFileName(
            self, "Save File", "", "PDF(*.pdf)")
        if filename[0]:
            printer = QtPrintSupport.QPrinter(
                QtPrintSupport.QPrinter.PrinterResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setPaperSize(QtPrintSupport.QPrinter.A4)
            printer.setPageMargins(
                1, 1, 1, 1, QtPrintSupport.QPrinter.Millimeter)
            printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
            printer.setOutputFileName(filename[0])
            document = QtGui.QTextDocument()
            style_sheet = """
                body {
                    width: 100vw;
                    height: 100vh;
                    margin: 0;
                    padding: 0;
                }
                h1 {
                    text-align: center;
                }
                h2 {
                    text-align: right;
                    font-weight: 400;
                    font-size: 12px;
                    margin: 0px;
                }
                h3 {
                    text-align: left;
                    margin: 1px;
                }
                p {
                    text-align: center;
                    font-size: 12px;
                }
                table {
                  border-collapse: collapse;
                  width: 100%;
                }
                th, td {
                    border: 1px solid black;
                    padding: 4px;
                    font-size: 10px;
                    text-align: left;
                }
                th {
                  background-color: #29b6f6;
                  font-weight: bold;
                  font-size: 10px;
                }
            """
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <body>
                <h1> """+school_info[0][0]+"""</h1>
                <p> """+school_info[0][2]+""" </p>
                <h2> Contact : """+school_info[0][1]+""" </h2>
                <h1>Expense</h1>

                <h3>Print Date: """+str(QDate.currentDate().toString('dd-MM-yyyy'))+"""</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Head of Account</th>
                            <th>Amount</th>
                            <th>Payment Type</th>
                            <th>Recipient Name</th>
                            <th>Comments</th>
                        </tr>
                    </thead>
                    <tbody>
                    """
            for i in range(self.expense_table.rowCount()):
                html += """<tr>"""
                for j in range(self.expense_table.columnCount()):
                    html += """<td>""" + \
                        self.expense_table.item(i, j).text()+"</td>"
                html += "</tr>"
            html += """
                    </tbody>
    
                </table>
            </body>
            </html>
            """

            document.setDefaultStyleSheet(style_sheet)
            document.setHtml(html)
            document.print_(printer)
            QMessageBox.information(self, "Success", "PDF Saved Successfully")

    # PRINT STUDENTS
    def print_students(self):
        school_info = self.db.select_all(
            table_name="school_info", columns="school_name, contact, address")

        filename = QFileDialog.getSaveFileName(
            self, "Save File", "", "PDF(*.pdf)")
        if filename[0]:
            printer = QtPrintSupport.QPrinter(
                QtPrintSupport.QPrinter.PrinterResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setPaperSize(QtPrintSupport.QPrinter.A4)
            printer.setPageMargins(
                1, 1, 1, 1, QtPrintSupport.QPrinter.Millimeter)
            printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
            printer.setOutputFileName(filename[0])
            document = QtGui.QTextDocument()
            style_sheet = """
                body {
                    width: 100vw;
                    height: 100vh;
                    margin: 0;
                    padding: 0;
                }
                h1 {
                    text-align: center;
                }
                h2 {
                    text-align: right;
                    font-weight: 400;
                    font-size: 12px;
                    margin: 0px;
                }
                h3 {
                    text-align: left;
                    margin: 1px;
                }
                p {
                    text-align: center;
                    font-size: 12px;
                }
                table {
                  border-collapse: collapse;
                  width: 100%;
                }
                th, td {
                    border: 1px solid black;
                    padding: 4px;
                    font-size: 10px;
                    text-align: left;
                }
                th {
                  background-color: #29b6f6;
                  font-weight: bold;
                  font-size: 10px;
                }
                
            """
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <body>
                <h1> """+school_info[0][0]+"""</h1>
                <p> """+school_info[0][2]+""" </p>
                <h2> Contact : """+school_info[0][1]+""" </h2>
                <h1>Students</h1>

                <h3>Print Date: """+str(QDate.currentDate().toString('dd-MM-yyyy'))+"""</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Admission Date</th>
                            <th>Registration / Admission No</th>
                            <th>Student Name</th>
                            <th>Father Name</th>
                            <th>Class</th>
                            <th>Image</th>
                            <th>Remaining Fee</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                    """
            for i in range(self.students_table.rowCount()):
                html += """<tr>"""
                for j in range(self.students_table.columnCount()):
                    if j == 5:
                        html += "<td>-</td>"
                        continue
                    html += """<td>""" + \
                        self.students_table.item(i, j).text()+"</td>"
                html += "</tr>"
            html += """
                    </tbody>
    
                </table>
            
            </body>
            </html>
            """

            document.setDefaultStyleSheet(style_sheet)
            document.setHtml(html)
            document.print_(printer)
            QMessageBox.information(self, "Success", "PDF Saved Successfully")


def main():
    app = QApplication(sys.argv)
    window = MainWindow(0)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
