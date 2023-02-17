
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
import os
FORM_MAIN,_= loadUiType('ui/add_student.ui')


class AddStudentWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()
        self.update()
        self.Handle_Buttons()
        self.txt_admission_date.setDate(QtCore.QDate.currentDate())
        
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.save()

    def update(self):
        # clear classes combobox
        self.select_class.clear()
        # add classes to combobox
        self.select_class.addItems(["select Class"])
        self.select_class.addItems(
            [str(i[0]) for i in self.db.conn.execute(
                "SELECT class_name FROM classes ORDER BY class_name ASC"
            ).fetchall()])
        
    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.save)
        self.btn_cancel.clicked.connect(self.close)
        self.std_image.mousePressEvent = self.select_image

    def select_image(self, event):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Image',
                                                   '', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if file_name:
            pixel = QPixmap(file_name)
            self.std_image.setPixmap(pixel)
            self.std_image.setScaledContents(True)
            self.std_image.setAlignment(Qt.AlignCenter)

    def save(self):
        addmission_date= self.txt_admission_date.date().toString("dd/MM/yyyy")
        addmission_no= self.txt_admission_no.text()
        name = self.txt_student_name.text()
        father_name = self.txt_student_father_name.text()
        dob = self.txt_student_dob.text()
        address = self.txt_student_address.text()
        contact = self.txt_student_contact.text()
        gender = self.txt_student_gender.text()
        class_name = self.select_class.currentText()
        if class_name == "select Class":
            QMessageBox.warning(self, "Error", "Please select class")
            return
        section = self.select_class_section.currentText()
        last_school = self.txt_last_school.text()
        special_case = self.txt_special_case.text()
        image= self.std_image.pixmap()
        if addmission_date and addmission_no and name and father_name and dob and address and contact and gender and class_name:
            try:
                if image:
                    if not path.exists('assets/students'):
                        os.mkdir('assets/students')
                    
                    image.save('assets/students/{}.png'.format(name.replace(' ', '_')))
                    image = 'assets/students/{}.png'.format(name.replace(' ', '_'))
                else:
                    image = ''
                
                self.db.insert(
                    table_name='students',
                    columns="addmission_date,addmission_no,name,f_name,dob,address,contact,gender,section,last_school,special_case,student_image,class_id",
                    values=f"'{addmission_date}','{addmission_no}','{name}','{father_name}','{dob}','{address}','{contact}','{gender}','{section if section else ''}','{last_school if last_school else ''}','{special_case if special_case else ''}','{image}',{self.db.conn.execute('SELECT id FROM classes WHERE class_name=?', (class_name,)).fetchone()[0]}"
                )
                QMessageBox.information(self, "Success", "Student added successfully")
                self.close()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
        else:
            QMessageBox.warning(self, "Error", "Please fill all fields")


def main():
    app = QApplication(sys.argv)
    window = AddStudentWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
