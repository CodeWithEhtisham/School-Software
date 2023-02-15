
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

FORM_MAIN, _ = loadUiType('ui/update_class.ui')


class UpdateClassWindow(QMainWindow, FORM_MAIN):
    def __init__(self,id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()
        self.id = id
        self.Handle_Buttons()
        self.txt_class.setText(
            self.db.select(
                table_name='classes',
                columns="class_name",
                condition=f"id={self.id}"
            )[0][0]
        )

     # HANDLE BUTTONS
    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.save_class)
        self.btn_cancel.clicked.connect(self.close)

    def save_class(self):
        class_name = self.txt_class.text()
        if class_name:
            try:
                self.db.conn.execute(
                    f"UPDATE classes SET class_name='{class_name}' WHERE id={self.id}"
                )
                self.db.conn.commit()
                QMessageBox.information(self, "Success", "Class added successfully")
                self.close()
            except Exception as e:
                QMessageBox.information(self, "Error", str(e))
        else:
            QMessageBox.information(self, "Error", "Class name is required")



def main():
    app = QApplication(sys.argv)
    window = UpdateClassWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
