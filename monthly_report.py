
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
        pass

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
            if received[0][0] or expense[0][0]:
                report.append([day,received[0][0],expense[0][0]])
        
        self.monthly_accounts_table.setRowCount(len(report))
        for index , row in enumerate(report):
            for col_index, item in enumerate(row):
                self.monthly_accounts_table.setItem(index,col_index,QTableWidgetItem(str(item)))




def main():
    app = QApplication(sys.argv)
    window = MonthlyReportWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
