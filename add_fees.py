
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
        
        # 
        # self.months_frame.hide()
        self.txt_monthly_fee.setFocus()
        
    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.add_fee)
        self.btn_cancel.clicked.connect(self.close)
        self.txt_monthly_fee.textChanged.connect(self.calculate_total)
        self.txt_annual_fund.textChanged.connect(self.calculate_total)
        self.txt_comp_lab_fee.textChanged.connect(self.calculate_total)
        self.txt_sci_lab_fee.textChanged.connect(self.calculate_total)
        self.txt_addmission_fee.textChanged.connect(self.calculate_total)
        # self.show_months.stateChanged.connect(self.show_months_frame)
        # self.show_months.stateChanged.connect(self.calculate_total)
        
        # 
        self.txt_jan.textChanged.connect(self.calculate_total)
        self.txt_feb.textChanged.connect(self.calculate_total)
        self.txt_march.textChanged.connect(self.calculate_total)
        self.txt_april.textChanged.connect(self.calculate_total)
        self.txt_may.textChanged.connect(self.calculate_total)
        self.txt_june.textChanged.connect(self.calculate_total)
        self.txt_july.textChanged.connect(self.calculate_total)
        self.txt_august.textChanged.connect(self.calculate_total)
        self.txt_sep.textChanged.connect(self.calculate_total)
        self.txt_oct.textChanged.connect(self.calculate_total)
        self.txt_nov.textChanged.connect(self.calculate_total)
        self.txt_dec.textChanged.connect(self.calculate_total)
        
    
    # def show_months_frame(self, state):
    #     if state == Qt.Checked:
    #         self.months_frame.show()
    #     else:
    #         self.months_frame.hide()
    
    def calculate_total(self):
        try:
            # monthly_fee = self.txt_monthly_fee.text()
            #
            # self.txt_jan.setText(monthly_fee)
            # self.txt_feb.setText(monthly_fee)
            # self.txt_march.setText(monthly_fee)
            # self.txt_april.setText(monthly_fee)
            # self.txt_may.setText(monthly_fee)
            # self.txt_june.setText(monthly_fee)
            # self.txt_july.setText(monthly_fee)
            # self.txt_august.setText(monthly_fee)
            # self.txt_sep.setText(monthly_fee)
            # self.txt_oct.setText(monthly_fee)
            # self.txt_nov.setText(monthly_fee)
            # self.txt_dec.setText(monthly_fee)
            
            # 
            jan_fee = self.txt_jan.text()
            feb_fee = self.txt_feb.text()
            march_fee = self.txt_march.text()
            april_fee = self.txt_april.text()
            may_fee = self.txt_may.text()
            june_fee = self.txt_june.text()
            july_fee = self.txt_july.text()
            aug_fee = self.txt_august.text()
            sep_fee = self.txt_sep.text()
            oct_fee = self.txt_oct.text()
            nov_fee = self.txt_nov.text()
            dec_fee = self.txt_dec.text()
            
            annual_fund = self.txt_annual_fund.text()
            com_lab_fee = self.txt_comp_lab_fee.text()
            sci_lab_fee = self.txt_sci_lab_fee.text()
            addmission_fee = self.txt_addmission_fee.text()
            
            total = int(
                jan_fee if jan_fee else 0)+int(
                feb_fee if feb_fee else 0)+int(
                march_fee if march_fee else 0)+int(
                april_fee if april_fee else 0)+int(
                may_fee if may_fee else 0)+int(
                june_fee if june_fee else 0)+int(
                july_fee if july_fee else 0)+int(
                aug_fee if aug_fee else 0)+int(
                sep_fee if sep_fee else 0)+int(
                oct_fee if oct_fee else 0)+int(
                nov_fee if nov_fee else 0)+int(
                dec_fee if dec_fee else 0) + int(
                annual_fund if annual_fund else 0)+int(
                com_lab_fee if com_lab_fee else 0)+int(
                sci_lab_fee if sci_lab_fee else 0)+int(
                addmission_fee if addmission_fee else 0)
            
            # total= int(monthly_fee if monthly_fee else 0)*12+int(annual_fund if annual_fund else 0)+int(com_lab_fee if com_lab_fee else 0)+int(sci_lab_fee if sci_lab_fee else 0)+int(addmission_fee if addmission_fee else 0)
            
            self.txt_total.setText(str(total))
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def add_fee(self):
        # get date from date edit
        add_fee_date = self.txt_add_fee_date.date().toString("yyyy/MM/dd")
        # monthly_fee = self.txt_monthly_fee.text()
        #
        jan_fee = self.txt_jan.text()
        feb_fee = self.txt_feb.text()
        march_fee = self.txt_march.text()
        april_fee = self.txt_april.text()
        may_fee = self.txt_may.text()
        june_fee = self.txt_june.text()
        july_fee = self.txt_july.text()
        aug_fee = self.txt_august.text()
        sep_fee = self.txt_sep.text()
        oct_fee = self.txt_oct.text()
        nov_fee = self.txt_nov.text()
        dec_fee = self.txt_dec.text()
        annual_fund = self.txt_annual_fund.text()
        com_lab_fee = self.txt_comp_lab_fee.text()
        sci_lab_fee = self.txt_sci_lab_fee.text()
        addmission_fee = self.txt_addmission_fee.text()
        total= self.txt_total.text()

        if annual_fund and com_lab_fee and sci_lab_fee and addmission_fee and total:
            try:
                self.db.insert(
                    table_name='fee',
                    columns="std_id,date,jan_fee,feb_fee,march_fee,april_fee,may_fee,june_fee,july_fee,august_fee,sep_fee,oct_fee,nov_fee,dec_fee,annual_fund,computer_lab_fee,science_lab_fee,addmission_fee,total",
                    values=f"'{self.std_id}','{add_fee_date}','{jan_fee}','{feb_fee}','{march_fee}','{april_fee}','{may_fee}','{june_fee}','{july_fee}','{aug_fee}','{sep_fee}','{oct_fee}','{nov_fee}','{dec_fee}','{annual_fund}','{com_lab_fee}','{sci_lab_fee}','{addmission_fee}','{total}'")
                last_id = self.db.conn.execute(
                    "SELECT id FROM fee ORDER BY id DESC LIMIT 1").fetchone()[0]
                
                self.db.insert(
                    table_name='transactions',
                    columns="paid_fee,discount,date,challan_no,description,fee_id,remaining_fee",
                    values=f"'{0}','{0}','{add_fee_date}','-','Add Fee','{last_id}','{total}'"
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
