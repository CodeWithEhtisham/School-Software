# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exam_details.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_ExamDetailsWindow(object):
    def setupUi(self, ExamDetailsWindow):
        if not ExamDetailsWindow.objectName():
            ExamDetailsWindow.setObjectName(u"ExamDetailsWindow")
        ExamDetailsWindow.resize(500, 544)
        ExamDetailsWindow.setMinimumSize(QSize(500, 0))
        self.centralwidget = QWidget(ExamDetailsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"	background-color: #e3f2fd;\n"
"}\n"
"#std_image {\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"#header_frame, #label {\n"
"	background-color: #90caf9;\n"
"}\n"
"\n"
"#bottom_widget {\n"
"	background-color: #b3e5fc;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #42a5f5;\n"
"	border-radius: 5px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#btn_cancel {\n"
"	background-color: #cfd8dc;\n"
"	border-radius: 5px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #039be5;\n"
"	padding: 5px 5px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #039be5;\n"
"	padding: 5px 5px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(10)

        self.verticalLayout_3.addWidget(self.label)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(14)
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.select_term = QComboBox(self.frame_2)
        self.select_term.addItem("")
        self.select_term.addItem("")
        self.select_term.addItem("")
        self.select_term.setObjectName(u"select_term")
        self.select_term.setFont(font1)

        self.verticalLayout.addWidget(self.select_term)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout_3.addWidget(self.widget)

        self.bottom_widget = QWidget(self.centralwidget)
        self.bottom_widget.setObjectName(u"bottom_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 15, 20, 15)
        self.btn_save = QPushButton(self.bottom_widget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(0, 40))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_save.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon)
        self.btn_save.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_save)

        self.btn_cancel = QPushButton(self.bottom_widget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMinimumSize(QSize(0, 40))
        self.btn_cancel.setFont(font2)
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancel.setIcon(icon1)
        self.btn_cancel.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_cancel)


        self.verticalLayout_3.addWidget(self.bottom_widget)

        ExamDetailsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ExamDetailsWindow)
        self.statusbar.setObjectName(u"statusbar")
        ExamDetailsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ExamDetailsWindow)

        QMetaObject.connectSlotsByName(ExamDetailsWindow)
    # setupUi

    def retranslateUi(self, ExamDetailsWindow):
        ExamDetailsWindow.setWindowTitle(QCoreApplication.translate("ExamDetailsWindow", u"Exam Details", None))
        self.label.setText(QCoreApplication.translate("ExamDetailsWindow", u"Exam - Result", None))
        self.label_3.setText(QCoreApplication.translate("ExamDetailsWindow", u"Term", None))
        self.select_term.setItemText(0, QCoreApplication.translate("ExamDetailsWindow", u"1st Term", None))
        self.select_term.setItemText(1, QCoreApplication.translate("ExamDetailsWindow", u"2nd Term", None))
        self.select_term.setItemText(2, QCoreApplication.translate("ExamDetailsWindow", u"3rd Term", None))

        self.btn_save.setText(QCoreApplication.translate("ExamDetailsWindow", u"Save", None))
        self.btn_cancel.setText(QCoreApplication.translate("ExamDetailsWindow", u"Cancel", None))
    # retranslateUi

