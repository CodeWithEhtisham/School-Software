
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

FORM_MAIN, _ = loadUiType('ui/student_details.ui')


class StudentDetailWindow(QMainWindow, FORM_MAIN):
    def __init__(self,std_id):
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
    
    def update_student_details(self):
        student = self.db.conn.execute(
            f"SELECT s.addmission_date,s.addmission_no,s.name,s.f_name,s.dob,s.address,s.contact,s.gender,s.section,s.last_school,s.special_case,s.student_image,c.class_name FROM students s INNER JOIN classes c ON s.class_id = c.id WHERE s.id = '{self.std_id}'").fetchone()
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


    def student(self):
        self.stackedWidget.setCurrentWidget(self.student_page)
        self.update_student_details()

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
    window = StudentDetailWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
