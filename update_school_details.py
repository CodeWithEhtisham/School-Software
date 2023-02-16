import datetime
import sqlite3
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

FORM_MAIN, _ = loadUiType('ui/update_school_details.ui')


class UpdateBusinessWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()
        self.Handle_Buttons()
        self.update()

    def update(self):
        data=self.db.select(table_name='school_info',columns="*",condition="id=1")
        if data:
            self.txt_business_name.setText(data[0][1])
            self.txt_business_contact.setText(data[0][2])
            self.txt_business_address.setText(data[0][3])
            self.txt_business_logo.setPixmap(QPixmap(data[0][4]))
            self.txt_business_logo.setScaledContents(True)
            self.txt_business_logo.setAlignment(QtCore.Qt.AlignCenter)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.update_business()
            
    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.update_business)
        self.btn_cancel.clicked.connect(self.close)
        self.txt_business_logo.mousePressEvent = self.select_logo

    def select_logo(self, event):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Logo',
                                                   '', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if file_name:
            pixel = QPixmap(file_name)
            self.txt_business_logo.setPixmap(pixel)
            self.txt_business_logo.setScaledContents(True)
            self.txt_business_logo.setAlignment(Qt.AlignCenter)

    def update_business(self):
        name=self.txt_business_name.text()
        contact=self.txt_business_contact.text()
        address=self.txt_business_address.text()
        logo = self.txt_business_logo.pixmap()
        logo.save('assets/business_logo.png')

        if name and contact and address:
            self.db.conn.execute("UPDATE school_info SET school_name=?, contact=?, address=?, logo=? WHERE id=1",
                                 (name, contact, address, 'assets/business_logo.png'))
            self.db.conn.commit()
            QMessageBox.information(self, 'Success', 'Business details updated successfully')
            self.close()
        else:
            QMessageBox.information(self, 'Error', 'Please fill all the fields')



def main():
    app = QApplication(sys.argv)
    window = UpdateBusinessWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()