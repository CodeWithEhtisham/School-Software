
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
from datetime import datetime
import calendar
FORM_MAIN, _ = loadUiType('ui/monthly_report.ui')


class MonthlyReportWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()
        self.Handle_Buttons()
        self.update(month=None,year=None)
        
    def Handle_Buttons(self):
        self.select_month.dateChanged.connect(self.month_changed)

    def month_changed(self):
        month = self.select_month.date().month()
        year = self.select_month.date().year()
        self.update(month,year)

    def update(self,month,year):
        if not month or not year:
            month =QDate.currentDate().month()
            year = QDate.currentDate().year()
        # create a list of all the days in the month
        num_days=calendar.monthrange(year,month)[1]

        days = [datetime(year, month, day).strftime('%d/%m/%Y') for day in range(1, num_days+1)]
        report =[[]]
        for day in days:
            received = self.db.select(
                table_name='transactions',
                columns='sum(paid_fee)',
                condition=f"date = '{day}'"
            )
            expense = self.db.select(
                table_name='expenses',
                columns='sum(amount)',
                condition=f"date = '{day}'"
            )
            print(received,expense)
            if received[0][0] or expense[0][0]:
                report.append([day,received[0][0],expense[0][0]])
        # print(report)
        self.monthly_accounts_table.setRowCount(len(report))
        for index , row in enumerate(report):
            for col_index, item in enumerate(row):
                self.monthly_accounts_table.setItem(index,col_index,QTableWidgetItem(str(item)))

        start_date = datetime(year, month, 1).strftime('%d/%m/%Y')
        end_date = datetime(year, month, num_days).strftime('%d/%m/%Y')
        print(start_date,end_date)
        monthly_expense_report=self.db.conn.execute(
            f"SELECT date,hoa,SUM(amount) FROM expenses WHERE date BETWEEN '{start_date}' AND '{end_date}' GROUP BY hoa"
        ).fetchall()
        for month in monthly_expense_report:
            if month[0] not in days:
                monthly_expense_report.remove(month)
        print(monthly_expense_report)
        self.monthly_expense_table.setRowCount(len(monthly_expense_report))
        for index , row in enumerate(monthly_expense_report):
            for col_index, item in enumerate(row):
                self.monthly_expense_table.setItem(index,col_index,QTableWidgetItem(str(item)))
        amount_received=self.db.select(
            table_name='transactions',
            columns='sum(paid_fee)',
            condition=f"date BETWEEN '{start_date}' AND '{end_date}'"
        )[0][0]
        if not amount_received:
            amount_received=0
        self.lbl_total_amount_received.setText(str(amount_received))
        remaining=self.db.select(
            table_name='transactions',
            columns='sum(remaining_fee)',
            condition=f"date BETWEEN '{start_date}' AND '{end_date}'"
        )[0][0]
        if not remaining:
            remaining=0
        self.lbl_total_amount_remaining.setText(str(remaining))
        expensees=self.db.select(
            table_name='expenses',
            columns='sum(amount)',
            condition=f"date BETWEEN '{start_date}' AND '{end_date}'"
        )[0][0]
        if not expensees:
            expensees=0
        self.lbl_total_expense.setText(str(expensees))
        self.lbl_net_balance.setText(str(amount_received-expensees))



def main():
    app = QApplication(sys.argv)
    window = MonthlyReportWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
