
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui, QtPrintSupport
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
        self.update(month=None, year=None)
        
        self.monthly_accounts_table.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Fixed)

    def Handle_Buttons(self):
        self.select_month.dateChanged.connect(self.month_changed)
        self.btn_print.clicked.connect(self.print_report)

    def month_changed(self):
        month = self.select_month.date().month()
        year = self.select_month.date().year()
        self.update(month, year)

    def update(self, month, year):
        if not month or not year:
            month = QDate.currentDate().month()
            year = QDate.currentDate().year()
        # create a list of all the days in the month
        num_days = calendar.monthrange(year, month)[1]

        days = [datetime(year, month, day).strftime('%Y/%m/%d')
                for day in range(1, num_days+1)]
        report = []
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
            # print(received, expense)
            if received[0][0] or expense[0][0]:
                report.append([day, received[0][0], expense[0][0]])

        self.monthly_accounts_table.setRowCount(len(report))
        for index, row in enumerate(report):
            for col_index, item in enumerate(row):
                self.monthly_accounts_table.setItem(
                    index, col_index, QTableWidgetItem(str(item)))

        start_date = datetime(year, month, 1).strftime('%Y/%m/%d')
        end_date = datetime(year, month, num_days).strftime('%Y/%m/%d')
        # print(start_date, end_date)
        monthly_expense_report = self.db.conn.execute(
            f"SELECT date,hoa,SUM(amount) FROM expenses WHERE date BETWEEN '{start_date}' AND '{end_date}' GROUP BY hoa"
        ).fetchall()
        for month in monthly_expense_report:
            if month[0] not in days:
                monthly_expense_report.remove(month)
        # print(monthly_expense_report)
        self.monthly_expense_table.setRowCount(len(monthly_expense_report))
        for index, row in enumerate(monthly_expense_report):
            for col_index, item in enumerate(row):
                self.monthly_expense_table.setItem(
                    index, col_index, QTableWidgetItem(str(item)))
        amount_received = self.db.select(
            table_name='transactions',
            columns='sum(paid_fee)',
            condition=f"date BETWEEN '{start_date}' AND '{end_date}'"
        )[0][0]
        if not amount_received:
            amount_received = 0
        self.lbl_total_amount_received.setText(str(amount_received))
        try:
            remaining = self.db.select_all(
                table_name='students',
                columns='sum(remaining_fee)'
            )[0][0]
        except:
            remaining = 0
        if not remaining:
            remaining = 0
        self.lbl_total_amount_remaining.setText(str(remaining))
        expensees = self.db.select(
            table_name='expenses',
            columns='sum(amount)',
            condition=f"date BETWEEN '{start_date}' AND '{end_date}'"
        )[0][0]
        if not expensees:
            expensees = 0
        self.lbl_total_expense.setText(str(f"{expensees:,}"))
        self.lbl_net_balance.setText(str(amount_received-expensees))

    # PRINT MONTHLY
    def print_report(self):
        school_info = self.db.select_all(
            table_name="school_info", columns="school_name, contact, address")

        filename = QFileDialog.getSaveFileName(
            self, "Save File", "", "PDF(*.pdf)")
        if filename[0]:
            printer = QtPrintSupport.QPrinter(
                QtPrintSupport.QPrinter.PrinterResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setPaperSize(QtPrintSupport.QPrinter.A4)
            printer.setPageMargins(
                1, 1, 1, 1, QtPrintSupport.QPrinter.Millimeter)
            printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
            printer.setOutputFileName(filename[0])
            document = QtGui.QTextDocument()
            style_sheet = """
                body {
                    width: 100vw;
                    height: 100vh;
                    margin: 0;
                    padding: 0;
                }
                h1 {
                    text-align: center;
                }
                h2 {
                    text-align: right;
                    font-weight: 400;
                    font-size: 12px;
                    margin: 0px;
                }
                h3 {
                    text-align: left;
                    margin: 1px;
                }
                p {
                    text-align: center;
                    font-size: 12px;
                }
                table {
                  border-collapse: collapse;
                  width: 100%;
                }
                .full-width {
                    width: 100%;
                    background-color: #00bcd4;
                }
                th, td {
                    border: 1px solid black;
                    padding: 4px;
                    font-size: 10px;
                    text-align: left;
                }
                th {
                  background-color: #29b6f6;
                  font-weight: bold;
                  font-size: 10px;
                }
                
            """
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <body>
                <h1> """+school_info[0][0]+"""</h1>
                <p> """+school_info[0][2]+""" </p>
                <h2> Contact : """+school_info[0][1]+""" </h2>
                <h1>Monthly Report</h1>
                <h3>Print Date: """+str(QDate.currentDate().toString('dd-MM-yyyy'))+"""</h3>
                <p> Summary of the Month </p>
                <table class="full-width">
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Amount Received</th>
                            <th>Expense</th>
                        </tr>
                    </thead>
                    <tbody>
                    """
            for i in range(self.monthly_accounts_table.rowCount()):
                html += """<tr>"""
                for j in range(self.monthly_accounts_table.columnCount()):
                    html += """<td>"""
                    if self.monthly_accounts_table.item(i, j) is None:
                        html += """-</td>"""
                    else:
                        html += self.monthly_accounts_table.item(
                            i, j).text()+"</td>"
                html += "</tr>"
            html += """
                    </tbody>
    
                </table>
                <p> Monthly Expense </p>
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Head of Account</th>
                            <th>Amount</th>
                        </tr>
                    </thead>
                    <tbody>
                    """
            for i in range(self.monthly_expense_table.rowCount()):
                html += """<tr>"""
                for j in range(self.monthly_expense_table.columnCount()):
                    html += """<td>"""
                    if self.monthly_expense_table.item(i, j) is None:
                        html += """-</td>"""
                    else:
                        html += self.monthly_expense_table.item(
                            i, j).text()+"</td>"
                html += "</tr>"
            html += """
                    </tbody>
    
                </table>
                <hr>
                <h2>Total Amount Received:"""+self.lbl_total_amount_received.text()+"""</h2>
                <h2>Total Amount Remaining:"""+self.lbl_total_amount_remaining.text()+""" </h2>
                <h2>Total Expense: """+self.lbl_total_expense.text()+"""</h2>
                <hr>
                <h2>Net Balance: """+self.lbl_net_balance.text()+"""</h2>
            </body>
            </html>
            """

            document.setDefaultStyleSheet(style_sheet)
            document.setHtml(html)
            document.print_(printer)
            QMessageBox.information(self, "Success", "PDF Saved Successfully")


def main():
    app = QApplication(sys.argv)
    window = MonthlyReportWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
