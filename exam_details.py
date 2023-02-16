
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from db_handler import DBHandler
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from os import path
from PyQt5.uic import loadUiType

FORM_MAIN, _ = loadUiType('ui/exam_details.ui')


class ExamDetailsWindow(QMainWindow, FORM_MAIN):
    def __init__(self,std_id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.std_id = std_id
        self.db = DBHandler()
        self.class_id = self.db.conn.execute(
            f"SELECT class_id FROM students WHERE id={self.std_id}").fetchone()[0]
        s= self.db.conn.execute(
            f"SELECT id,subject_name FROM subjects WHERE class_id={self.class_id}").fetchall()
        self.subject = [i[1] for i in s]
        self.update()
        self.btn_save.clicked.connect(self.exam_save)
        self.btn_cancel.clicked.connect(self.close)

    def update(self):
        # create lable and line edit for each subject
        for i in self.subject:
            self.label = QtWidgets.QLabel(self.centralwidget)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(100)
            self.label.setFont(font)
            # self.label.setAlignment(QtCore.Qt.AlignCenter)
            # add padding to label
            self.label.setContentsMargins(0,20,0,5)
            self.label.setObjectName(i)
            self.label.setText(i)
            self.frame.layout().addWidget(self.label, 3, QtCore.Qt.AlignTop)
            
            self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(100)
            self.lineEdit.setFont(font)
            self.lineEdit.setObjectName("txt_"+i)
            self.frame_2.layout().addWidget(self.lineEdit, 3, QtCore.Qt.AlignTop)

    def exam_save(self):
        exam=self.select_term.currentText()
        try:
            self.db.insert(
                table_name='exams',
                columns="exam_name,date,class_id,student_id",
                values=f"'{exam}','{QDate.currentDate().toString('dd/MM/yyyy') }',{self.class_id},{self.std_id}"
            )
            # self.db.conn.execute(
            #     f"INSERT INTO exams (exam_name,date,class_id,student_id) VALUES ('{exam}','{QDate.currentDate().toString('dd/MM/yyyy') }',{self.class_id},{self.std_id})"
            # )
            exam_id = self.db.conn.execute(
                f"SELECT id FROM exams order by id desc limit 1").fetchone()[0]
            
            for i in self.subject:
                subject_id = self.db.conn.execute(
                    f"SELECT id FROM subjects WHERE subject_name='{i}' and class_id={self.class_id}").fetchone()[0]
                # self.db.insert(
                #     table_name='exam_details',
                #     columns="exam_id,subject_id,marks",
                #     values=f"{exam_id},{subject_id},{self.findChild(QtWidgets.QLineEdit, 'txt_'+i).text()}")
                self.db.conn.execute(
                    f"INSERT INTO exam_details (exam_id,subject_id,marks) VALUES ({exam_id},{subject_id},{self.findChild(QtWidgets.QLineEdit, 'txt_'+i).text()})")
                
            self.db.conn.commit()
            QMessageBox.information(self, "Success", "Exam details saved successfully")
            self.close()
        except Exception as e:
            QMessageBox.information(self, "Error", str(e))





def main():
    app = QApplication(sys.argv)
    window = ExamDetailsWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
