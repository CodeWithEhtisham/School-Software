
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

FORM_MAIN, _ = loadUiType('ui/update_subject.ui')


class UpdateSubjectWindow(QMainWindow, FORM_MAIN):
    def __init__(self,id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db= DBHandler()
        self.id = id
        self.Handle_Buttons()
        data=self.db.select(
            table_name='subjects',
            columns="subject_name,passing_mark,total_mark",
            condition=f"id={self.id}"
        )[0]
        self.txt_subject_name.setText(data[0])
        self.txt_passing_marks.setText(str(data[1]))
        self.txt_total_marks.setText(str(data[2]))

     # HANDLE BUTTONS
    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.save_subject)
        self.btn_cancel.clicked.connect(self.close)

    def save_subject(self):
        subject_name = self.txt_subject_name.text()
        passing_mark = self.txt_passing_marks.text()
        total_mark = self.txt_total_marks.text()
        if subject_name and passing_mark and total_mark:
            try:
                self.db.conn.execute(
                    f"UPDATE subjects SET subject_name='{subject_name}', passing_mark={passing_mark}, total_mark={total_mark} WHERE id={self.id}"
                )
                self.db.conn.commit()
                QMessageBox.information(self, "Success", "Subject updated successfully")
                self.close()
            except Exception as e:
                QMessageBox.information(self, "Error", str(e))
        else:
            QMessageBox.information(self, "Error", "All fields are required")


def main():
    app = QApplication(sys.argv)
    window = UpdateSubjectWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
