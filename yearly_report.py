
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from datetime import datetime
import calendar
from db_handler import DBHandler
import sys
from os import path
from PyQt5.uic import loadUiType

FORM_MAIN, _ = loadUiType('ui/yearly_report.ui')


class YearlyReportWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()
        self.Handle_Buttons()
        self.update(year=None)
        
    def Handle_Buttons(self):
        self.select_year.dateChanged.connect(self.month_changed)

    def month_changed(self):
        year = self.select_year.date().year()
        self.update(year)

    def update(self,year):
        if not year:
            year = QDate.currentDate().year()
        # create a list of all the days in the month
        

        days = [datetime(year, month, day).strftime('%d/%m/%Y') for month in range(1, 13) for day in range(1, calendar.monthrange(year,month)[1]+1)]
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
            if received[0][0] or expense[0][0]:
                report.append([day,received[0][0],expense[0][0]])
        
        self.accounts_table.setRowCount(len(report))
        for index , row in enumerate(report):
            for col_index, item in enumerate(row):
                self.accounts_table.setItem(index,col_index,QTableWidgetItem(str(item)))

        start_date = datetime(year, 1, 1).strftime('%d/%m/%Y')
        end_date = datetime(year, 12, 31).strftime('%d/%m/%Y')
        print(start_date,end_date)
        monthly_expense_report=self.db.conn.execute(
            f"SELECT date,hoa,SUM(amount) FROM expenses WHERE date BETWEEN '{start_date}' AND '{end_date}' GROUP BY hoa"
        ).fetchall()
        for month in monthly_expense_report:
            if month[0] not in days:
                monthly_expense_report.remove(month)
        print(monthly_expense_report)
        self.expense_table.setRowCount(len(monthly_expense_report))
        for index , row in enumerate(monthly_expense_report):
            for col_index, item in enumerate(row):
                self.expense_table.setItem(index,col_index,QTableWidgetItem(str(item)))
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
    window = YearlyReportWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
