
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
        self.update()

    def update(self):
        # get all subjects of student
        class_id = self.db.conn.execute(
            f"SELECT class_id FROM students WHERE id={self.std_id}").fetchone()[0]
        subject= self.db.conn.execute(
            f"SELECT id,subject_name FROM subjects WHERE class_id={class_id}").fetchall()
        subject = [i[1] for i in subject]

        # create lable and line edit for each subject
        for i in range(len(subject)):
            self.label = QtWidgets.QLabel(self.centralwidget)
            font = QtGui.QFont()
            font.setFamily("Calibri")
            font.setPointSize(18)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setAlignment(QtCore.Qt.AlignCenter)
            self.label.setObjectName("label")
            self.frame.layout().addWidget(self.label, 0, QtCore.Qt.AlignTop)





            # self.frame.layout().addWidget(QLabel(subject[i]),i,0,1,1)
            # # add name of above label 
            # # self.frame_2.layout().addWidget(QLineEdit(

            # # ),
            # # i,0,1,1)


def main():
    app = QApplication(sys.argv)
    window = ExamDetailsWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
