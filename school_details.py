
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

FORM_MAIN, _ = loadUiType('ui/school_details.ui')


class SchoolDetailsWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()
        self.Handle_Buttons()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.save_business()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.save_business)
        self.btn_clear.clicked.connect(self.clear_fields)
        self.btn_cancel.clicked.connect(self.close)
        # logo frame is an image frame
        self.txt_business_logo.mousePressEvent = self.select_logo

    def select_logo(self, event):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Logo',
                                                   '', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if file_name:
            pixel = QPixmap(file_name)
            self.txt_business_logo.setPixmap(pixel)
            self.txt_business_logo.setScaledContents(True)
            self.txt_business_logo.setAlignment(Qt.AlignCenter)
        # add for loop to check if the file is an image file

    def save_business(self):
        business_name = self.txt_business_name.text()
        business_contact = self.txt_business_contact.text()
        business_address = self.txt_business_address.text()
        logo = self.txt_business_logo.pixmap()
        logo.save('assets/school_logo.png')

        if business_name and business_contact and business_address:
            try:
                self.db.insert(table_name='school_info', columns="school_name, contact, address, logo",
                               values=f"'{business_name}', '{business_contact}', '{business_address}', 'assets/school_logo.png'")
                QMessageBox.information(
                    self, 'Success', 'Business details saved successfully')
                self.close()
            except Exception as e:
                QMessageBox.warning(self, 'Error', str(e))
        else:
            QMessageBox.warning(self, 'Error', 'Fields cannot be empty')

    def clear_fields(self):
        self.txt_business_name.setText('')
        self.txt_business_contact.setText('')
        self.txt_business_address.setText('')
        self.txt_business_logo.clear()


def main():
    app = QApplication(sys.argv)
    window = SchoolDetailsWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
