
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui, QtPrintSupport
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
        self.btn_print.clicked.connect(self.print_report)

    def month_changed(self):
        year = self.select_year.date().year()
        self.update(year)

    def update(self, year):
        if not year:
            year = QDate.currentDate().year()
        # create a list of all the days in the month

        days = [datetime(year, month, day).strftime('%Y/%m/%d') for month in range(1, 13)
                for day in range(1, calendar.monthrange(year, month)[1]+1)]
        report = [[month] for month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']]
        # print(report)
        # for day in days:
            # received = self.db.select(
            #     table_name='transactions',
            #     columns='sum(paid_fee)',
            #     condition=f"date = '{day}'"
            # )
        received = self.db.conn.execute(
            f"""SELECT 
                substr(date, 6, 2) || '-' || substr(date, 1, 4) AS month, 
                SUM(paid_fee) AS total_paid_fees,
                CASE substr(date, 6, 2)
                    WHEN '01' THEN 'January'
                    WHEN '02' THEN 'February'
                    WHEN '03' THEN 'March'
                    WHEN '04' THEN 'April'
                    WHEN '05' THEN 'May'
                    WHEN '06' THEN 'June'
                    WHEN '07' THEN 'July'
                    WHEN '08' THEN 'August'
                    WHEN '09' THEN 'September'
                    WHEN '10' THEN 'October'
                    WHEN '11' THEN 'November'
                    WHEN '12' THEN 'December'
                    ELSE 'Unknown'
                END AS month_name
                FROM transactions
                GROUP BY substr(date, 1, 7)
                ORDER BY date;
            """
        ).fetchall()
        # print(received)
        expense = self.db.conn.execute(
            f"""SELECT
                substr(date, 6, 2) || '-' || substr(date, 1, 4) AS month,
                SUM(amount) AS total_expense,
                CASE substr(date, 6, 2)
                    WHEN '01' THEN 'January'
                    WHEN '02' THEN 'February'
                    WHEN '03' THEN 'March'
                    WHEN '04' THEN 'April'
                    WHEN '05' THEN 'May'
                    WHEN '06' THEN 'June'
                    WHEN '07' THEN 'July'
                    WHEN '08' THEN 'August'
                    WHEN '09' THEN 'September'
                    WHEN '10' THEN 'October'
                    WHEN '11' THEN 'November'
                    WHEN '12' THEN 'December'
                    ELSE 'Unknown'
                END AS month_name
                FROM expenses
                GROUP BY substr(date, 1, 7)
                ORDER BY date;
            """
        ).fetchall()
        
        if received:
            for m in report:
                for r in received:
                    if m[0] == r[2]:
                        m.append(r[1])
                        break
                else:
                    m.append(0)
        if expense:
            for m in report:
                for e in expense:
                    if m[0] == e[2]:
                        m.append(e[1])
                        break
                else:
                    m.append(0)

        self.accounts_table.setRowCount(len(report))
        for index, row in enumerate(report):
            for col_index, item in enumerate(row):
                self.accounts_table.setItem(
                    index, col_index, QTableWidgetItem(str(item)))

        start_date = datetime(year, 1, 1).strftime('%Y/%m/%d')
        end_date = datetime(year, 12, 31).strftime('%Y/%m/%d')
        monthly_expense_report = self.db.conn.execute(
            f"SELECT date,hoa,SUM(amount) FROM expenses WHERE date BETWEEN '{start_date}' AND '{end_date}' GROUP BY hoa"
        ).fetchall()
        for month in monthly_expense_report:
            if month[0] not in days:
                monthly_expense_report.remove(month)

        self.expense_table.setRowCount(len(monthly_expense_report))
        for index, row in enumerate(monthly_expense_report):
            for col_index, item in enumerate(row):
                self.expense_table.setItem(
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

    # PRINT YEARLY
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
                <h1>Yearly Report</h1>

                <h3>Print Date: """+str(QDate.currentDate().toString('dd-MM-yyyy'))+"""</h3>
                <p> Summary of the Year </p>
                <table>
                    <thead>
                        <tr>
                            <th>Month</th>
                            <th>Amount Received</th>
                            <th>Expense</th>
                        </tr>
                    </thead>
                    <tbody>
            """
            for i in range(self.accounts_table.rowCount()):
                html += """<tr>"""
                for j in range(self.accounts_table.columnCount()):
                    html += """<td>"""
                    if self.accounts_table.item(i, j) is None:
                        html += """-</td>"""
                    else:
                        html += self.accounts_table.item(
                            i, j).text()+"</td>"
                html += "</tr>"
            html += """
                    </tbody>
    
                </table>
                <p> Yearly Expense </p>
                <table>
                    <thead>
                        <tr>
                            <th>Month</th>
                            <th>Head of Account</th>
                            <th>Amount</th>
                        </tr>
                    </thead>
                    <tbody>
            """
            for i in range(self.expense_table.rowCount()):
                html += """<tr>"""
                for j in range(self.expense_table.columnCount()):
                    html += """<td>"""
                    if self.expense_table.item(i, j) is None:
                        html += """-</td>"""
                    else:
                        html += self.expense_table.item(
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
    window = YearlyReportWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
