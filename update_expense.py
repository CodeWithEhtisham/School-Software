
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

FORM_MAIN, _ = loadUiType('ui/update_expense.ui')


class UpdateExpensesWindow(QMainWindow, FORM_MAIN):
    def __init__(self,expense_id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.expense_date.setDate(QDate.currentDate())
        self.db=DBHandler()
        self.id=expense_id
        self.Handle_Buttons()

     # HANDLE BUTTONS
    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.update_expense)
        self.btn_delete.clicked.connect(self.delete_expense)
        self.txt_amount.textChanged.connect(self.amount_changed)
        self.update()

    def delete_expense(self):
        try:
            # dialog box to confirm delete
            confirm=QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this expense?", QMessageBox.Yes | QMessageBox.No)
            if confirm==QMessageBox.Yes:
                self.db.delete(table_name="expenses", condition=f"id={self.id}")
                QMessageBox.information(self, "Success", "Expense deleted successfully")
                self.close()
        except Exception as e:
            QMessageBox.information(self, "Error", str(e))

    def update(self):
        expense=self.db.select(
            table_name="expenses",
            columns="date,hoa,amount,payment_type,recipient_name,comment",
            condition=f"id={self.id}"
        )
        if expense:
            self.expense_date.setDate(QDate.fromString(expense[0][1], "dd/MM/yyyy"))
            self.select_hoa.addItems(
                [item[0] for item in self.db.select_all(table_name="expense_types", columns="head_of_account")]
            )
            self.select_hoa.setCurrentText(str(expense[0][1]))
            self.txt_amount.setText(str(int(expense[0][2])))
            self.txt_payment_type.setText(expense[0][3])
            self.txt_recipient.setText(expense[0][4])
            self.txt_comment.setText(expense[0][5])

    def amount_changed(self):
        # add separator to amount
        try:
            amount=self.txt_amount.text()
            if amount:
                amount=amount.replace(",","")
                self.txt_amount.setText("{:,}".format(int(amount)))
        except Exception as e:
            QMessageBox.information(self, "Error", str(e))

    def update_expense(self):
        date=self.expense_date.date().toString("dd/MM/yyyy")
        head_of_account=self.select_hoa.currentText()
        amount=self.txt_amount.text().replace(",","")
        payment_type=self.txt_payment_type.text()
        recipient=self.txt_recipient.text()
        comment=self.txt_comment.text()

        if head_of_account and amount and payment_type and recipient:
            try:
                self.db.conn.execute(
                    f"UPDATE expenses SET date=?,hoa=?,amount=?,payment_type=?,recipient_name=?,comment=? WHERE id={self.id}",
                    (date, head_of_account, amount, payment_type, recipient, comment))
                self.db.conn.commit()
                QMessageBox.information(self, "Success", "Expense updated successfully")
                self.close()
            except Exception as e:
                QMessageBox.information(self, "Error", str(e))




def main():
    app = QApplication(sys.argv)
    window = UpdateExpensesWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()