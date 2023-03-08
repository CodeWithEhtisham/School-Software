
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
FORM_MAIN,_= loadUiType('ui/update_student.ui')


class UpdateStudentWindow(QMainWindow, FORM_MAIN):
    def __init__(self,student_id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.student_id = student_id
        self.db = DBHandler()
        self.update()
        self.Handle_Buttons()

    def update(self):
        # clear classes combobox
        self.select_class.clear()
        # add classes to combobox
        self.select_class.addItems(
            [str(i[0]) for i in self.db.conn.execute(
                f"SELECT c.class_name FROM classes c, students s WHERE s.class_id = c.id AND s.id = {self.student_id}")])
        
        self.select_class.addItems(
            [str(i[0]) for i in self.db.conn.execute(
                "SELECT class_name FROM classes ORDER BY class_name ASC"
            ).fetchall()])
        student = self.db.conn.execute(
            f"SELECT addmission_date,addmission_no,name,f_name,dob,address,contact,gender,section,last_school,special_case,student_image FROM students WHERE id = {self.student_id}").fetchone()
        self.txt_admission_date.setDate(QDate.fromString(student[0], "yyyy/MM/dd"))
        self.txt_admission_no.setText(student[1])
        self.txt_student_name.setText(student[2])
        self.txt_student_father_name.setText(student[3])
        self.txt_student_dob.setText(student[4])
        self.txt_student_address.setText(student[5])
        self.txt_student_contact.setText(student[6])
        self.txt_student_gender.setText(student[7])
        # set section 
        if student[8]=='A':
            self.select_class_section.setCurrentIndex(0)
        elif student[8]=='B':
            self.select_class_section.setCurrentIndex(1)
        elif student[8]=='C':
            self.select_class_section.setCurrentIndex(2)
            
        # self.select_class_section.setText(student[9])
        self.txt_last_school.setText(student[9])
        self.txt_special_case.setText(student[10])
        self.std_image.setPixmap(QPixmap(student[11]))
        self.std_image.setScaledContents(True)
        self.std_image.setAlignment(Qt.AlignCenter)

        
    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.save)
        self.btn_cancel.clicked.connect(self.close)
        self.std_image.mousePressEvent = self.select_image
        self.btn_delete.clicked.connect(self.delete)

    def delete(self):
        ret= QMessageBox.question(self, 'Delete Student', 'Are you sure you want to delete this student?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ret == QMessageBox.Yes:
            self.db.conn.execute(f"DELETE FROM students WHERE id = {self.student_id}")
            fee_id = self.db.conn.execute(f"SELECT id FROM fee WHERE std_id = {self.student_id}").fetchall()
            for i in fee_id:
                self.db.conn.execute(f"DELETE FROM transactions WHERE fee_id = {i[0]}")
            self.db.conn.execute(f"DELETE FROM fee WHERE std_id = {self.student_id}")
            self.db.conn.commit()
            self.close()
            
        else:
            pass

    def select_image(self, event):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select Image',
                                                   '', 'Image Files (*.png *.jpg *.jpeg *.bmp)')
        if file_name:
            pixel = QPixmap(file_name)
            self.std_image.setPixmap(pixel)
            self.std_image.setScaledContents(True)
            self.std_image.setAlignment(Qt.AlignCenter)

    def save(self):
        addmission_date= self.txt_admission_date.date().toString("yyyy/MM/dd")
        addmission_no= self.txt_admission_no.text()
        name = self.txt_student_name.text()
        father_name = self.txt_student_father_name.text()
        dob = self.txt_student_dob.text()
        address = self.txt_student_address.text()
        contact = self.txt_student_contact.text()
        gender = self.txt_student_gender.text()
        class_name = self.select_class.currentText()
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
                
                # self.db.update(
                #     table_name='students',
                #     columns="addmission_date,addmission_no,name,f_name,dob,address,contact,gender,section,last_school,special_case,student_image,class_id",
                #     values=f"'{addmission_date}','{addmission_no}','{name}','{father_name}','{dob}','{address}','{contact}','{gender}','{section if section else ''}','{last_school if last_school else ''}','{special_case if special_case else ''}','{image}',{self.db.conn.execute('SELECT id FROM classes WHERE class_name=?', (class_name,)).fetchone()[0]}",
                #     condition=f"id = {self.student_id}"
                # )
                self.db.conn.execute(
                    f"UPDATE students SET addmission_date='{addmission_date}',addmission_no='{addmission_no}',name='{name}',f_name='{father_name}',dob='{dob}',address='{address}',contact='{contact}',gender='{gender}',section='{section if section else ''}',last_school='{last_school if last_school else ''}',special_case='{special_case if special_case else ''}',class_id={self.db.conn.execute('SELECT id FROM classes WHERE class_name=?', (class_name,)).fetchone()[0]} WHERE id = {self.student_id}"
                )
                self.db.conn.commit()
                QMessageBox.information(self, "Success", "Student update successfully")
                self.close()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
        else:
            QMessageBox.warning(self, "Error", "Please fill all fields")



        



def main():
    app = QApplication(sys.argv)
    window = UpdateStudentWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
