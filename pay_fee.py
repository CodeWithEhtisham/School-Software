
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

FORM_MAIN, _ = loadUiType('ui/pay_fee.ui')


class PayFeeWindow(QMainWindow, FORM_MAIN):
    def __init__(self,reg_no):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()
        std= self.db.select(table_name='students',columns='id,name,remaining_fee',condition=f"addmission_no = '{reg_no}'")[0]
        self.std_id = std[0]
        self.lbl_student_name.setText(str(std[1]))
        self.txt_remaining_fee.setText(str(std[2]))
        self.txt_pay_fee_date.setDate(QtCore.QDate.currentDate())
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.pay_fee)
        self.btn_cancel.clicked.connect(self.close)
        self.txt_paid_fee.textChanged.connect(self.remaining_fee)
        self.txt_discount.textChanged.connect(self.deduct_discount)

    def deduct_discount(self):
        try:
            paid_fee = self.txt_paid_fee.text()
            if not paid_fee:
                QMessageBox.warning(self, "Warning", "Please enter paid fee first")
                self.txt_discount.setText("")
                return 
            remaining_fee = float(self.txt_remaining_fee.text())
            discount = float(self.txt_discount.text())
            print(f"remaining fee {remaining_fee} discount {discount}, paid fee {paid_fee}")
            if discount >= 0:
                paid_fee = float(paid_fee)
                total_remaining = remaining_fee - discount - paid_fee
                print(f"total remaining {total_remaining}")
                if total_remaining >= 0:
                    self.txt_total_remaining.setText(str(total_remaining))
                else:
                    QMessageBox.warning(self, "Warning", "Discount cannot be greater than remaining fee")
                    self.txt_discount.setText("")
                    self.txt_total_remaining.setText(str(remaining_fee))
            else:
                self.txt_total_remaining.setText(str(remaining_fee-float(paid_fee)))

        except Exception as e:
            print(f"disscount error {e}")
            self.txt_total_remaining.setText(str(remaining_fee-float(paid_fee)))


    def remaining_fee(self):
        try:
            remaining_fee = float(self.txt_remaining_fee.text())
            pay_fee = float(self.txt_paid_fee.text())
            if pay_fee >= 0:
                total_remaining = remaining_fee - pay_fee
                if total_remaining >= 0:
                    self.txt_total_remaining.setText(str(total_remaining))
                else:
                    QMessageBox.warning(self, "Warning", "Paid fee cannot be greater than remaining fee")
                    self.txt_paid_fee.setText(str(0))
                    self.txt_total_remaining.setText(str(remaining_fee))
            else:
                self.txt_total_remaining.setText(str(remaining_fee))
                self.txt_paid_fee.setText(str(0))

        except Exception as e:
            self.txt_total_remaining.setText(str(remaining_fee))

    def pay_fee(self):
        try:
            paid_fee= float(self.txt_paid_fee.text())
            discount= float(self.txt_discount.text())
            date= self.txt_pay_fee_date.date().toString('yyyy/MM/dd')
            challan_no= self.txt_challan_no.text()
            description= self.txt_description.text()
            remaining_fee= float(self.txt_total_remaining.text())
            if paid_fee and date and challan_no and description:
                fee_id = self.db.select(
                    table_name='fee',
                    columns='id',
                    condition=f"std_id = '{self.std_id}'"
                )
                if fee_id:
                    fee_id = fee_id[-1][0]
                    self.db.insert(
                        table_name='transactions',
                        columns='fee_id,paid_fee,discount,date,challan_no,description,remaining_fee',
                        values=f"'{fee_id}','{paid_fee}','{discount}','{date}','{challan_no}','{description}','{remaining_fee}'"
                    )
                    self.db.update(
                        table_name='students',
                        columns='remaining_fee',
                        values=f"'{remaining_fee}'",
                        condition=f"id = '{self.std_id}'"
                    )
                    QMessageBox.information(self, 'Success', 'Fee Paid Successfully')
                    self.close()
                else:
                    QMessageBox.information(self, 'Error', 'Fee Not Found')
            else:
                QMessageBox.information(self, 'Error', 'All Fields Are Required')
        except Exception as e:
            QMessageBox.information(self, 'Error', f'Please Enter Valid Data {e}')


def main():
    app = QApplication(sys.argv)
    window = PayFeeWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
