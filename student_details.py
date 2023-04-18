
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
from add_fees import AddFeesWindow
from exam_details import ExamDetailsWindow
from pay_fee import PayFeeWindow
from left_school import LeftSchoolWindow
from update_fees import UpdatePayFeeWindow
from exam_details import ExamDetailsWindow

FORM_MAIN, _ = loadUiType('ui/student_details.ui')


class StudentDetailWindow(QMainWindow, FORM_MAIN):
    def __init__(self, std_id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.std_id = std_id
        self.db = DBHandler()
        self.label.setText(
            self.db.select(
                table_name='students',
                columns="name",
                condition=f"id = '{self.std_id}'")[0][0])
        self.Handle_Buttons()
        self.update_student_details()


    def Handle_Buttons(self):
        self.btn_student.clicked.connect(self.student)
        self.btn_fees.clicked.connect(self.fees)
        self.btn_results.clicked.connect(self.results)

        self.btn_add_fees.clicked.connect(self.add_fees)
        self.btn_add_result.clicked.connect(self.exam_details)
        self.btn_pay_fee.clicked.connect(self.pay_fee)
        self.btn_student_leaving.clicked.connect(self.student_leaving)
        self.btn_edit_fee.clicked.connect(self.edit_fee)
        self.select_term.currentTextChanged.connect(self.update_exam_details)
        # self.btn_add_result
    def update_exam_details(self):
        try:
            selected=self.select_term.currentText()
            if selected == "1st Term":
                print(selected)
                # get all optained marks and total marks from the table_1st_term
                total_mark=0
                obtained_mark=0
                for i in range(self.table_1st_term.rowCount()):
                    total_mark+=int(self.table_1st_term.item(i,1).text())
                    obtained_mark+=int(self.table_1st_term.item(i,3).text())
                self.lbl_total_marks.setText(str(total_mark))
                self.lbl_obtain_marks.setText(str(obtained_mark))
            
            elif selected == "2nd Term":
                print(selected)
                # get all optained marks and total marks from the table_2nd_term
                total_mark=0
                obtained_mark=0
                for i in range(self.table_2nd_term.rowCount()):
                    total_mark+=int(self.table_2nd_term.item(i,1).text())
                    obtained_mark+=int(self.table_2nd_term.item(i,3).text())
                self.lbl_total_marks.setText(str(total_mark))
                self.lbl_obtain_marks.setText(str(obtained_mark))

            elif selected == "3rd Term":
                print(selected)
                # get all optained marks and total marks from the table_3rd_term
                total_mark=0
                obtained_mark=0
                for i in range(self.table_3rd_term.rowCount()):
                    total_mark+=int(self.table_3rd_term.item(i,1).text())
                    obtained_mark+=int(self.table_3rd_term.item(i,3).text())
                self.lbl_total_marks.setText(str(total_mark))
                self.lbl_obtain_marks.setText(str(obtained_mark))

            else:
                print("else")
                self.lbl_total_marks.setText(str('0'))
                self.lbl_obtain_marks.setText(str('0'))
        except Exception as e:
            QMessageBox.warning(self, "Error", f"no data found {e}")

    def edit_fee(self):
        row = self.fees_table.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Error", "Please select a row")
            return
        date = self.fees_table.item(row, 0).text()
        challan_no = self.fees_table.item(row, 3).text()
        description = self.fees_table.item(row, 4).text()
        print(date, challan_no, description)
        fee_id = self.db.select(
            table_name='transactions',
            columns="id,fee_id",
            condition=f"date = '{date}' and challan_no = '{challan_no}' and description = '{description}'")[0]
        self.edit_fee_window = UpdatePayFeeWindow(self.std_id, fee_id[1], fee_id[0])
        self.edit_fee_window.show()
        self.edit_fee_window.btn_save.clicked.connect(self.update_fee)
        self.edit_fee_window.btn_delete.clicked.connect(self.update_fee)


    def update_fee(self):
        try:
            fee = self.db.select(
                table_name='fee',
                columns="*",
                condition=f"std_id = '{self.std_id}'")[-1]
            self.lbl_jan_fee.setText(str(fee[2]))
            self.lbl_feb_fee.setText(str(fee[3]))
            self.lbl_march_fee.setText(str(fee[4]))
            self.lbl_april_fee.setText(str(fee[5]))
            self.lbl_may_fee.setText(str(fee[6]))
            self.lbl_june_fee.setText(str(fee[7]))
            self.lbl_july_fee.setText(str(fee[8]))
            self.lbl_august_fee.setText(str(fee[9]))
            self.lbl_sep_fee.setText(str(fee[10]))
            self.lbl_oct_fee.setText(str(fee[11]))
            self.lbl_nov_fee.setText(str(fee[12]))
            self.lbl_dec_fee.setText(str(fee[13]))
            self.lbl_addmission_fee.setText(str(fee[1]))
            # self.lbl_monthly_fee.setText(str(fee[2]))
            self.lbl_annual_fund.setText(str(fee[14]))
            self.lbl_comp_lab_fee.setText(str(fee[15]))
            self.lbl_sci_lab_fee.setText(str(fee[16]))
            self.lbl_total_fee.setText(str(fee[18]))

            transactions = self.db.select(
                table_name='transactions',
                columns="date,paid_fee,discount,challan_no,description,remaining_fee",
                condition=f"fee_id = '{fee[0]}'")

            self.fees_table.setRowCount(0)
            remaining_fee = 0
            for row_number, row_data in enumerate(transactions):
                self.fees_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    if column_number == 5:
                        remaining_fee = data
                    self.fees_table.setItem(
                        row_number, column_number, QTableWidgetItem(str(data)))
            self.lbl_remaining_fee.setText(str(remaining_fee))
        except Exception as e:
            QMessageBox.warning(self, "Error", f"no data found {e}")
     # HANDLE BUTTONS

    

    def update_student_details(self):
        student = self.db.conn.execute(
            f"SELECT s.addmission_date,s.addmission_no,s.name,s.f_name,s.dob,s.address,s.contact,s.gender,s.section,s.last_school,s.special_case,s.student_image,c.class_name,s.status,s.addmission_date,description FROM students s INNER JOIN classes c ON s.class_id = c.id WHERE s.id = '{self.std_id}'").fetchone()
        self.lbl_admission_date.setText(student[0])
        self.lbl_admission_no.setText(student[1])
        self.lbl_father_name.setText(student[3])
        self.lbl_dob.setText(student[4])
        self.lbl_address.setText(student[5])
        self.lbl_contact.setText(student[6])
        self.lbl_gender.setText(student[7])
        self.lbl_class.setText(student[12])
        self.lbl_section.setText(student[8])
        self.lbl_last_school.setText(student[9])
        self.lbl_special_case.setText(student[10])
        self.std_image.setPixmap(QPixmap(student[11]))
        self.std_image.setScaledContents(True)
        self.std_image.setAlignment(Qt.AlignCenter)
        self.label_7.setText(student[13])
        if student[13] == 'InActive':
            self.label_23.setText(str(student[14]))
            self.label_25.setText(str(student[15]))
        else:
            self.label_23.setText(str(''))
            self.label_25.setText(str(''))

    def student(self):
        self.stackedWidget.setCurrentWidget(self.student_page)
        self.update_student_details()

    def fees(self):
        self.stackedWidget.setCurrentWidget(self.fees_page)
        self.update_fee()

    def update_result(self):
        self.update_first_term_table()
        self.update_second_term_table()
        self.update_third_term_table()

    def results(self):
        self.stackedWidget.setCurrentWidget(self.result_page)
        self.update_result()

    def add_fees(self):
        self.add_fees_window = AddFeesWindow(self.std_id)
        self.add_fees_window.show()
        self.add_fees_window.btn_save.clicked.connect(self.update_fee)

    def pay_fee(self):
        reg_no = self.db.select(
            table_name='students',
            columns="addmission_no",
            condition=f"id = '{self.std_id}'")[0][0]
        self.pay_fee_window = PayFeeWindow(reg_no)
        self.pay_fee_window.show()
        self.pay_fee_window.btn_save.clicked.connect(self.update_fee)

    def exam_details(self):
        self.exam_details_window = ExamDetailsWindow(self.std_id)
        self.exam_details_window.show()
        self.exam_details_window.btn_save.clicked.connect(self.update_result)
        

    def student_leaving(self):
        self.school_leaving_window = LeftSchoolWindow(self.std_id)
        self.school_leaving_window.show()
        self.school_leaving_window.btn_save.clicked.connect(self.close)

    def update_first_term_table(self):
        try:
            class_id = self.db.select(
                table_name='students',
                columns="class_id",
                condition=f"id = '{self.std_id}'")[0][0]
            exam_id = self.db.select(
                table_name='exams',
                columns="id",
                condition=f"class_id = '{class_id}' and student_id = '{self.std_id}' and exam_name = '1st Term'")[0][0]
            first_term_results = self.db.conn.execute(
                f"SELECT s.subject_name,s.total_mark,s.passing_mark,r.marks FROM subjects s INNER JOIN exam_details r ON s.id = r.subject_id WHERE r.exam_id = '{exam_id}'").fetchall()
        
            if first_term_results:
                self.table_1st_term.setRowCount(0)
                for row_number, row_data in enumerate(first_term_results):
                    self.table_1st_term.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.table_1st_term.setItem(
                            row_number, column_number, QTableWidgetItem(str(data)))
                    # calculate percentage
                    percentage = (int(row_data[3]) / int(row_data[1])) * 100
                    self.table_1st_term.setItem(
                        row_number, 4, QTableWidgetItem(str(round(percentage, 0))))
        except:
            pass
                
    def update_second_term_table(self):
        try:
            class_id = self.db.select(
                table_name='students',
                columns="class_id",
                condition=f"id = '{self.std_id}'")[0][0]
            exam_id = self.db.select(
                table_name='exams',
                columns="id",
                condition=f"class_id = '{class_id}' and student_id = '{self.std_id}' and exam_name = '2nd Term'")[0][0]
            second_term_results = self.db.conn.execute(
                f"SELECT s.subject_name,s.total_mark,s.passing_mark,r.marks FROM subjects s INNER JOIN exam_details r ON s.id = r.subject_id WHERE r.exam_id = '{exam_id}'").fetchall()
            if second_term_results:
                self.table_2nd_term.setRowCount(0)
                for row_number, row_data in enumerate(second_term_results):
                    self.table_2nd_term.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.table_2nd_term.setItem(
                            row_number, column_number, QTableWidgetItem(str(data)))
                    # calculate percentage
                    percentage = (int(row_data[3]) / int(row_data[1])) * 100
                    self.table_2nd_term.setItem(
                        row_number, 4, QTableWidgetItem(str(round(percentage, 0))))
                    # add first term marks first table to second table
                    try:
                        first_term_marks = self.table_1st_term.item(row_number, 3).text()
                        self.table_2nd_term.setItem(
                            row_number, 5, QTableWidgetItem(str(first_term_marks)))
                    except AttributeError:
                        self.table_2nd_term.setItem(
                            row_number, 5, QTableWidgetItem(str(0)))
        except:
            pass

                
    def update_third_term_table(self):
        try:
            class_id = self.db.select(
                table_name='students',
                columns="class_id",
                condition=f"id = '{self.std_id}'")[0][0]
            exam_id = self.db.select(
                table_name='exams',
                columns="id",
                condition=f"class_id = '{class_id}' and student_id = '{self.std_id}' and exam_name = '3rd Term'")[0][0]
            third_term_results = self.db.conn.execute(
                f"SELECT s.subject_name,s.total_mark,s.passing_mark,r.marks FROM subjects s INNER JOIN exam_details r ON s.id = r.subject_id WHERE r.exam_id = '{exam_id}'").fetchall()
            if third_term_results:
                self.table_3rd_term.setRowCount(0)
                for row_number, row_data in enumerate(third_term_results):
                    self.table_3rd_term.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.table_3rd_term.setItem(
                            row_number, column_number, QTableWidgetItem(str(data)))
                    # calculate percentage
                    percentage = (int(row_data[3]) / int(row_data[1])) * 100
                    self.table_3rd_term.setItem(
                        row_number, 4, QTableWidgetItem(str(round(percentage, 0))))
                    # add first term marks first table to second table
                    try:
                        first_term_marks = self.table_1st_term.item(row_number, 3).text()
                        self.table_3rd_term.setItem(
                            row_number, 5, QTableWidgetItem(str(first_term_marks)))
                    except AttributeError:
                        self.table_3rd_term.setItem(
                            row_number, 5, QTableWidgetItem(str(0)))
                    # add second term marks first table to second table
                    try:
                        second_term_marks = self.table_2nd_term.item(row_number, 3).text()
                        self.table_3rd_term.setItem(
                            row_number, 6, QTableWidgetItem(str(second_term_marks)))
                    except AttributeError:
                        self.table_3rd_term.setItem(
                            row_number, 6, QTableWidgetItem(str(0)))
                        
        except:
            pass


def main():
    app = QApplication(sys.argv)
    window = StudentDetailWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
