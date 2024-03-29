
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
        self.select_month.setDate(QtCore.QDate.currentDate())
        self.Handle_Buttons()
        self.update(month=None, year=None, number_of_days=None)
        self.showMaximized()

    def Handle_Buttons(self):
        self.select_month.dateChanged.connect(self.month_changed)
        self.btn_print.clicked.connect(self.print_report)
        self.month_list = [
            'jan_fee',
            'feb_fee',
            'march_fee',
            'april_fee',
            'may_fee',
            'june_fee',
            'july_fee',
            'august_fee',
            'sep_fee',
            'oct_fee',
            'nov_fee',
            'dec_fee'

        ]

    def month_changed(self):
        month = self.select_month.date().month()
        year = self.select_month.date().year()
        day = self.select_month.date().day()
        self.update(month, year, day)

    def update(self, month, year, number_of_days):
        if not month or not year:
            month = QDate.currentDate().month()
            year = QDate.currentDate().year()
        month_name = calendar.month_name[month]
        self.lbl_month.setText(f"{month_name} {year}")
        # create a list of all the days in the month
        if not number_of_days:
            number_of_days = calendar.monthrange(year, month)[1]

        days = [datetime(year, month, day).strftime('%Y/%m/%d')
                for day in range(1, number_of_days+1)]
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
        end_date = datetime(year, month, number_of_days).strftime('%Y/%m/%d')
        monthly_expense_report = self.db.conn.execute(
            f"SELECT date,hoa,SUM(amount) FROM expenses WHERE date BETWEEN '{start_date}' AND '{end_date}' GROUP BY hoa"
        ).fetchall()
        for months in monthly_expense_report:
            if months[0] not in days:
                monthly_expense_report.remove(months)
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
        self.lbl_total_amount_received.setText(str(f"{amount_received:,}"))
        try:
            remaining = self.db.select_all(
                table_name='students',
                columns='sum(remaining_fee)'
            )[0][0]
        except:
            remaining = 0
        if not remaining:
            remaining = 0
        self.lbl_total_amount_remaining.setText(str(f"{remaining:,}"))
        expensees = self.db.select(
            table_name='expenses',
            columns='sum(amount)',
            condition=f"date BETWEEN '{start_date}' AND '{end_date}'"
        )[0][0]
        if not expensees:
            expensees = 0
        self.lbl_total_expense.setText(str(f"{expensees:,}"))
        self.lbl_net_balance.setText(str(f"{amount_received-expensees:,}"))

        # get complete year amount which will be received
        year_start_date = datetime(year, 1, 1).strftime('%Y/%m/%d')
        year_end_date = datetime(year, 12, 31).strftime('%Y/%m/%d')
        amount_received = self.db.select(
            table_name='fee',
            columns='sum(total)',
            condition=f"date BETWEEN '{year_start_date}' AND '{year_end_date}'"
        )
        self.lbl_total_amount.setText(
            str(f"{amount_received[0][0] if amount_received[0][0] else 0:,}"))
        # this mount total amount which will be received
        # month_start_date = datetime(year, month, 1).strftime('%Y/%m/%d')
        # month_end_date = datetime(year, month, number_of_days).strftime('%Y/%m/%d')
        # print(month_start_date, month_end_date)

        amount_received = self.db.select(
            table_name='fee',
            columns=f'sum({self.month_list[month-1]})',
            condition=f"date BETWEEN '{year_start_date}' AND '{year_end_date}'"
        )
        self.lbl_total_this_month.setText(
            str(f"{amount_received[0][0] if amount_received[0][0] else 0:,}"))
        self.lbl_remaining_this_month.setText(
            str(f"{amount_received[0][0]-expensees if amount_received[0][0] else 0:,}"))

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
                <table style="float: right;">
                    <tbody style="border: none; border-collapse: separate;">
                        <tr>
                            <td style="border: none; border-collapse: separate;">
                                <table>
                                    <tr>
                                        <td style="border: none; border-collapse: separate;">Total Amount:</td>
                                        <td style="border: none; border-collapse: separate;">"""+self.lbl_total_amount.text()+"""</td>
                                    </tr>
                                    <tr>
                                        <td style="border: none; border-collapse: separate;">Amount Remaining:</td>
                                        <td style="border: none; border-collapse: separate;">"""+self.lbl_total_amount_remaining.text()+"""</td>
                                    </tr>
                                    <tr>
                                        <td style="border: none; border-collapse: separate;">Expense:</td>
                                        <td style="border: none; border-collapse: separate;">"""+self.lbl_total_expense.text()+"""</td>
                                    </tr>
                                </table>
                            </td>
                            <td style="border: none; border-collapse: separate;">
                                <table>
                                    <tr>
                                        <td style="border: none; border-collapse: separate;">Total Amount of this Month:</td>
                                        <td style="border: none; border-collapse: separate;">"""+self.lbl_total_this_month.text()+"""</td>
                                    </tr>
                                    <tr>
                                        <td style="border: none; border-collapse: separate;">Amount Received this Month:</td>
                                        <td style="border: none; border-collapse: separate;">"""+self.lbl_total_amount_received.text()+"""</td>
                                    </tr>
                                    <tr>
                                        <td style="border: none; border-collapse: separate;">Remaining of this Month:</td>
                                        <td style="border: none; border-collapse: separate;">"""+self.lbl_remaining_this_month.text()+"""</td>
                                    </tr>
                                    <tr>
                                        <td style="border: none; border-collapse: separate;">Net Balance:</td>
                                        <td style="border: none; border-collapse: separate;">"""+self.lbl_net_balance.text()+"""</td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </tbody>
                </table>
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
