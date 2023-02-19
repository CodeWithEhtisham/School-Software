
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
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.add_fee)
        self.btn_cancel.clicked.connect(self.close)
        self.txt_monthly_fee.textChanged.connect(self.calculate_total)
        self.txt_annual_fund.textChanged.connect(self.calculate_total)
        self.txt_comp_lab_fee.textChanged.connect(self.calculate_total)
        self.txt_sci_lab_fee.textChanged.connect(self.calculate_total)
        self.txt_addmission_fee.textChanged.connect(self.calculate_total)

    
    def calculate_total(self):
        try:
            monthly_fee = self.txt_monthly_fee.text()
            annual_fund = self.txt_annual_fund.text()
            com_lab_fee = self.txt_comp_lab_fee.text()
            sci_lab_fee = self.txt_sci_lab_fee.text()
            addmission_fee = self.txt_addmission_fee.text()
            total= int(monthly_fee if monthly_fee else 0)*12+int(annual_fund if annual_fund else 0)+int(com_lab_fee if com_lab_fee else 0)+int(sci_lab_fee if sci_lab_fee else 0)+int(addmission_fee if addmission_fee else 0)
            self.txt_total.setText(str(total))
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def add_fee(self):
        # get date from date edit
        add_fee_date = self.txt_add_fee_date.date().toString("yyyy/MM/dd")
        monthly_fee = self.txt_monthly_fee.text()
        annual_fund = self.txt_annual_fund.text()
        com_lab_fee = self.txt_comp_lab_fee.text()
        sci_lab_fee = self.txt_sci_lab_fee.text()
        addmission_fee = self.txt_addmission_fee.text()
        total= self.txt_total.text()

        if monthly_fee and annual_fund and com_lab_fee and sci_lab_fee and addmission_fee and total:
            try:
                self.db.insert(
                    table_name='fee',
                    columns="std_id,date,monthly_fee,annual_fund,computer_lab_fee,science_lab_fee,addmission_fee,total",
                    values=f"'{self.std_id}','{add_fee_date}','{monthly_fee}','{annual_fund}','{com_lab_fee}','{sci_lab_fee}','{addmission_fee}','{total}'")
                last_id = self.db.conn.execute(
                    "SELECT id FROM fee ORDER BY id DESC LIMIT 1").fetchone()[0]
                
                self.db.insert(
                    table_name='transactions',
                    columns="paid_fee,date,challan_no,description,fee_id,remaining_fee",
                    values=f"'{0}','{add_fee_date}','-','Add Fee','{last_id}','{total}'"
                )
                self.db.update(
                    table_name='students',
                    columns="remaining_fee",
                    values=f"'{total}'",
                    condition=f"id = '{self.std_id}'"
                )
                QMessageBox.information(self, "Success", "Fee Added Successfully")
                self.close()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))

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
