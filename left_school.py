
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

FORM_MAIN, _ = loadUiType('ui/left_school.ui')


class LeftSchoolWindow(QMainWindow, FORM_MAIN):
    def __init__(self,std_id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.std_id = std_id
        self.db = DBHandler()
        self.Handle_Buttons()
        self.lbl_student_name.setText(
            self.db.select(table_name='students', columns='name', condition=f"id = '{self.std_id}'")[0][0]
        )

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.left_school)
        self.btn_cancel.clicked.connect(self.close)
        self.txt_leaving_date.setDate(QDate.currentDate())
        
    def left_school(self):
        date = self.txt_leaving_date.date().toString("yyyy/MM/dd")
        reason = self.txt_leaving_purpose.text()

        if date and reason:
            try:
                self.db.conn.execute(
                    f"update students set  description = '{reason}',addmission_date='{date}',remaining_fee=0, status = 'Left' where id = '{self.std_id}'")
                self.db.conn.commit()
                QMessageBox.information(self, "Success", "Student left school")
                self.close()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
        else:
            QMessageBox.warning(self, "Error", "Please fill all fields")



def main():
    app = QApplication(sys.argv)
    window = LeftSchoolWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
