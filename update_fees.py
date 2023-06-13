
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

FORM_MAIN, _ = loadUiType('ui/update_fees.ui')


class UpdatePayFeeWindow(QMainWindow, FORM_MAIN):
    def __init__(self,std_id,fee_id,trans_id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()
        self.std_id = std_id
        self.fee_id = fee_id
        self.trans_id=trans_id
        std= self.db.select(table_name='students',columns='name',condition=f"id = '{self.std_id}'")[0]
        self.lbl_student_name.setText(str(std[0]))
        self.txt_pay_fee_date.setDate(QtCore.QDate.currentDate())
        self.Handle_Buttons()
        self.update_fee_details()
        
        # Create a list of all the checkboxes
        self.checkboxes = [
            self.jan_cb,
            self.feb_cb,
            self.march_cb,
            self.april_cb,
            self.may_cb,
            self.june_cb,
            self.july_cb,
            self.aug_cb,
            self.sep_cb,
            self.oct_cb,
            self.nov_cb,
            self.dec_cb,
            self.adm_cb,
            self.annual_cb,
            self.comp_cb,
            self.sci_cb,
            self.activity_cb
        ]
        for checkbox in self.checkboxes:
            checkbox.stateChanged.connect(self.update_description)

    def update_description(self, state):
        description = ""
        for checkbox in self.checkboxes:
            if checkbox.isChecked():
                month = checkbox.text().capitalize()
                description += month + " "
        self.txt_description.setText(description.strip())


    def update_fee_details(self):
        # get previous fee details
        previous_fee_details = self.db.conn.execute(
            f"select remaining_fee from transactions where id < '{self.trans_id}' and fee_id = '{self.fee_id}' order by id desc limit 1").fetchall()
        if previous_fee_details:
            previous_fee_details = previous_fee_details[-1]
            self.txt_remaining_fee.setText(str(int(previous_fee_details[0])))

        fee_details = self.db.select(
            table_name='transactions',
            columns='paid_fee,date,challan_no,description,remaining_fee',
            condition=f"id = '{self.trans_id}'"
        )
        if fee_details:
            fee_details = fee_details[-1]
            self.txt_paid_fee.setText(str(int(fee_details[0])))
            self.txt_pay_fee_date.setDate(QtCore.QDate.fromString(fee_details[1], 'yyyy/MM/dd'))
            self.txt_challan_no.setText(str(fee_details[2]))
            self.txt_description.setText(str(fee_details[3]))
            # self.txt_remaining_fee.setText(str(fee_details[4]))
            self.txt_total_remaining.setText(str(fee_details[4]))

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.pay_fee)
        self.btn_cancel.clicked.connect(self.close)
        self.txt_paid_fee.textChanged.connect(self.remaining_fee)
        self.btn_delete.clicked.connect(self.delete_fee)

    def delete_fee(self):
        ret = QMessageBox.question(self, 'Delete Fee', 'Are you sure you want to delete this fee?',
                                      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ret == QMessageBox.Yes:
            after_ids = self.db.conn.execute(
                f"SELECT id,paid_fee,remaining_fee from transactions where id> {self.trans_id} and fee_id = '{self.fee_id}' order by id asc").fetchall()
            previous_remaining_fee = self.db.conn.execute(
                f"SELECT remaining_fee from transactions where id<{self.trans_id} and fee_id = '{self.fee_id}' order by id desc limit 1").fetchall()
            if previous_remaining_fee:
                previous_remaining_fee = previous_remaining_fee[-1][0]
            else:
                previous_remaining_fee = 0
            if after_ids:
                for fee in after_ids:
                    remaining_fee = previous_remaining_fee - fee[1]
                    self.db.conn.execute(
                        f"UPDATE transactions SET remaining_fee = '{remaining_fee}' WHERE id = '{fee[0]}'")
                    self.db.conn.commit()
                    previous_remaining_fee = remaining_fee
            self.db.conn.execute(
                f"DELETE FROM transactions where id = {self.trans_id}")
            self.db.conn.execute(
                f"UPDATE students SET remaining_fee = '{previous_remaining_fee}' WHERE id = '{self.std_id}'"
            )
            self.db.conn.commit()
            self.close()
        else:
            return


    def remaining_fee(self):
        try:
            remaining_fee = float(self.txt_remaining_fee.text())
            pay_fee = float(self.txt_paid_fee.text())
            self.txt_total_remaining.setText(str(remaining_fee - pay_fee))
        except Exception as e:
            print('error',e)

    def pay_fee(self):
        try:
            paid_fee= float(self.txt_paid_fee.text())
            date= self.txt_pay_fee_date.date().toString('yyyy/MM/dd')
            challan_no= self.txt_challan_no.text()
            description = self.txt_description.toPlainText()
            remaining_fee= float(self.txt_total_remaining.text())
            if paid_fee and date and challan_no and description and remaining_fee:
                self.db.conn.execute(
                    f"UPDATE transactions SET paid_fee = '{paid_fee}', date = '{date}', challan_no = '{challan_no}', description = '{description}', remaining_fee = '{remaining_fee}' WHERE id = '{self.trans_id}'")
                self.db.conn.commit()
                # update next all remaining fee
                next_fee_details = self.db.conn.execute(
                    f"SELECT id,paid_fee,remaining_fee from transactions where id > {self.trans_id} and fee_id = '{self.fee_id}' order by id asc").fetchall()
                if next_fee_details:
                    for fee in next_fee_details:
                        remaining_fee = remaining_fee - fee[1]
                        self.db.conn.execute(
                            f"UPDATE transactions SET remaining_fee = '{remaining_fee}' WHERE id = '{fee[0]}'")
                        self.db.conn.commit()
                self.db.conn.execute(
                    f"UPDATE students SET remaining_fee = '{remaining_fee}' WHERE id = '{self.std_id}'")
                self.db.conn.commit()

                QMessageBox.information(self, 'Success', 'Fee Updated Successfully')
                self.close()
            else:
                QMessageBox.information(self, 'Error', 'All Fields Are Required')
        except Exception as e:
            QMessageBox.information(self, 'Error', f'Please Enter Valid Data {e}')


def main():
    app = QApplication(sys.argv)
    window = UpdatePayFeeWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
