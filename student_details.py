
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

    def edit_fee(self):
        row = self.fees_table.currentRow()
        if row == -1:
            QMessageBox.warning(self, "Error", "Please select a row")
            return
        date = self.fees_table.item(row, 0).text()
        challan_no = self.fees_table.item(row, 2).text()
        description = self.fees_table.item(row, 3).text()
        fee_id = self.db.select(
            table_name='transactions',
            columns="id,fee_id",
            condition=f"date = '{date}' and challan_no = '{challan_no}' and description = '{description}'")[0]
        self.edit_fee_window = UpdatePayFeeWindow(self.std_id, fee_id[1], fee_id[0])
        self.edit_fee_window.show()
        self.edit_fee_window.btn_save.clicked.connect(self.update_fee)


    def update_fee(self):
        fee = self.db.select(
            table_name='fee',
            columns="*",
            condition=f"std_id = '{self.std_id}'")[-1]

        self.lbl_addmission_fee.setText(str(fee[1]))
        self.lbl_monthly_fee.setText(str(fee[2]))
        self.lbl_annual_fund.setText(str(fee[3]))
        self.lbl_comp_lab_fee.setText(str(fee[4]))
        self.lbl_sci_lab_fee.setText(str(fee[5]))
        self.lbl_total_fee.setText(str(fee[7]))

        transactions = self.db.select(
            table_name='transactions',
            columns="date,paid_fee,challan_no,description,remaining_fee",
            condition=f"fee_id = '{fee[0]}'")

        self.fees_table.setRowCount(0)
        remaining_fee = 0
        for row_number, row_data in enumerate(transactions):
            self.fees_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                if column_number == 4:
                    remaining_fee = data
                self.fees_table.setItem(
                    row_number, column_number, QTableWidgetItem(str(data)))
        self.lbl_remaining_fee.setText(str(remaining_fee))

     # HANDLE BUTTONS

    

    def update_student_details(self):
        student = self.db.conn.execute(
            f"SELECT s.addmission_date,s.addmission_no,s.name,s.f_name,s.dob,s.address,s.contact,s.gender,s.section,s.last_school,s.special_case,s.student_image,c.class_name,s.status FROM students s INNER JOIN classes c ON s.class_id = c.id WHERE s.id = '{self.std_id}'").fetchone()
        self.lbl_admission_date.setText(student[0])
        self.lbl_admission_no.setText(student[1])
        self.lbl_father_name.setText(student[3])
        self.lbl_dob.setText(student[4])
        self.lbl_address.setText(student[5])
        self.lbl_contact.setText(student[6])
        self.lbl_gender.setText(student[7])
        self.lbl_class.setText(student[-1])
        self.lbl_section.setText(student[8])
        self.lbl_last_school.setText(student[9])
        self.lbl_special_case.setText(student[10])
        self.std_image.setPixmap(QPixmap(student[11]))
        self.std_image.setScaledContents(True)
        self.std_image.setAlignment(Qt.AlignCenter)
        self.label_7.setText(student[-1])

    def student(self):
        self.stackedWidget.setCurrentWidget(self.student_page)
        self.update_student_details()

    def fees(self):
        self.stackedWidget.setCurrentWidget(self.fees_page)
        self.update_fee()

    def results(self):
        self.stackedWidget.setCurrentWidget(self.result_page)

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
        
        self.exam_details_window = ExamDetailsWindow()
        self.exam_details_window.show()
        

    def student_leaving(self):
        self.school_leaving_window = LeftSchoolWindow()
        self.school_leaving_window.show()



def main():
    app = QApplication(sys.argv)
    window = StudentDetailWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
