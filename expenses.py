
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

FORM_MAIN, _ = loadUiType('ui/expenses.ui')


class ExpensesWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.expense_date.setDate(QDate.currentDate())
        self.db=DBHandler()
        self.Handle_Buttons()

     # HANDLE BUTTONS
    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.save_expense)
        self.btn_cancel.clicked.connect(self.close)
        self.txt_amount.textChanged.connect(self.amount_changed)
        self.select_hoa.addItems(
            [item[0] for item in self.db.select_all(table_name="expense_types", columns="head_of_account")]
        )

    def amount_changed(self):
        # add separator to amount
        amount=self.txt_amount.text()
        if amount:
            amount=amount.replace(",","")
            self.txt_amount.setText("{:,}".format(int(amount)))

    def save_expense(self):
        date=self.expense_date.date().toString("yyyy/MM/dd")
        head_of_account=self.select_hoa.currentText()
        amount=self.txt_amount.text().replace(",","")
        payment_type=self.txt_payment_type.text()
        recipient=self.txt_recipient.text()
        comment=self.txt_comment.text()

        if head_of_account and amount and payment_type and recipient:
            try:
                self.db.insert(
                    table_name="expenses",
                    columns="date,hoa,amount,payment_type,recipient_name,comment",
                    values=f"'{date}','{head_of_account}','{int(amount)}','{payment_type}','{recipient}','{comment if comment else 'No comment'}'"
                )
                QMessageBox.information(self, "Success", "Expense added successfully")
                self.close()
            
            except Exception as e:
                QMessageBox.information(self, "Error", str(e))




def main():
    app = QApplication(sys.argv)
    window = ExpensesWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
