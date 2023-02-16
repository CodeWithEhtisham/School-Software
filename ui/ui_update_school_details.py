# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update_school_details.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_UpdateBusinessWindow(object):
    def setupUi(self, UpdateBusinessWindow):
        if not UpdateBusinessWindow.objectName():
            UpdateBusinessWindow.setObjectName(u"UpdateBusinessWindow")
        UpdateBusinessWindow.resize(600, 300)
        UpdateBusinessWindow.setMinimumSize(QSize(600, 300))
        UpdateBusinessWindow.setMaximumSize(QSize(600, 300))
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        UpdateBusinessWindow.setWindowIcon(icon)
        UpdateBusinessWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(UpdateBusinessWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#txt_business_logo {\n"
"	border-radius: 5px;\n"
"	background-color: #fff;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"#label {\n"
"	background-color: #81d4fa;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#label_5 {\n"
"	color: #fff;\n"
"}\n"
"\n"
"#btn_save {\n"
"	background-color: #29b6f6;\n"
"	border-radius: 5px;\n"
"	padding: 5px 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"#btn_clear {\n"
"	background-color: #80d8ff;\n"
"	border-radius: 5px;\n"
"	padding: 5px 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"#btn_cancel {\n"
"	background-color: #b0bec5;\n"
"	border-radius: 5px;\n"
"	padding: 5px 20px;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-radius: 5px;\n"
"	padding: 5px 5px;\n"
"}\n"
"\n"
"QDateEdit {\n"
"	border-radius: 5px;\n"
"	padding: 5px 5px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border-radius: 5px;\n"
"	padding: 5px 5px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"	border-radius: 10px;\n"
"	padding: 0px 0px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(10)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.main_details_widget = QWidget(self.centralwidget)
        self.main_details_widget.setObjectName(u"main_details_widget")
        self.main_details_widget.setLayoutDirection(Qt.RightToLeft)
        self.horizontalLayout_18 = QHBoxLayout(self.main_details_widget)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.business_logo_frame = QLabel(self.main_details_widget)
        self.business_logo_frame.setObjectName(u"business_logo_frame")
        self.business_logo_frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_17 = QVBoxLayout(self.business_logo_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.txt_business_logo = QLabel(self.business_logo_frame)
        self.txt_business_logo.setObjectName(u"txt_business_logo")
        self.txt_business_logo.setMinimumSize(QSize(120, 120))
        self.txt_business_logo.setMaximumSize(QSize(120, 120))
        font1 = QFont()
        font1.setPointSize(12)
        self.txt_business_logo.setFont(font1)
        self.txt_business_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.txt_business_logo)


        self.horizontalLayout_18.addWidget(self.business_logo_frame)

        self.input_field_frame = QFrame(self.main_details_widget)
        self.input_field_frame.setObjectName(u"input_field_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_field_frame.sizePolicy().hasHeightForWidth())
        self.input_field_frame.setSizePolicy(sizePolicy)
        self.input_field_frame.setFrameShape(QFrame.StyledPanel)
        self.input_field_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.input_field_frame)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.txt_business_name = QLineEdit(self.input_field_frame)
        self.txt_business_name.setObjectName(u"txt_business_name")
        self.txt_business_name.setMinimumSize(QSize(300, 35))
        self.txt_business_name.setMaximumSize(QSize(300, 35))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(14)
        self.txt_business_name.setFont(font2)

        self.verticalLayout_16.addWidget(self.txt_business_name, 0, Qt.AlignRight)

        self.txt_business_contact = QLineEdit(self.input_field_frame)
        self.txt_business_contact.setObjectName(u"txt_business_contact")
        self.txt_business_contact.setMinimumSize(QSize(300, 35))
        self.txt_business_contact.setMaximumSize(QSize(300, 35))
        self.txt_business_contact.setFont(font2)

        self.verticalLayout_16.addWidget(self.txt_business_contact, 0, Qt.AlignRight)

        self.txt_business_address = QLineEdit(self.input_field_frame)
        self.txt_business_address.setObjectName(u"txt_business_address")
        self.txt_business_address.setMinimumSize(QSize(300, 35))
        self.txt_business_address.setMaximumSize(QSize(300, 35))
        self.txt_business_address.setFont(font2)

        self.verticalLayout_16.addWidget(self.txt_business_address, 0, Qt.AlignRight)


        self.horizontalLayout_18.addWidget(self.input_field_frame)

        self.labels_frame = QFrame(self.main_details_widget)
        self.labels_frame.setObjectName(u"labels_frame")
        self.labels_frame.setLayoutDirection(Qt.LeftToRight)
        self.labels_frame.setFrameShape(QFrame.StyledPanel)
        self.labels_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.labels_frame)
        self.verticalLayout_15.setSpacing(20)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.b_name_lbl = QLabel(self.labels_frame)
        self.b_name_lbl.setObjectName(u"b_name_lbl")
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        self.b_name_lbl.setFont(font3)

        self.verticalLayout_15.addWidget(self.b_name_lbl)

        self.b_contact_lbl = QLabel(self.labels_frame)
        self.b_contact_lbl.setObjectName(u"b_contact_lbl")
        self.b_contact_lbl.setFont(font3)

        self.verticalLayout_15.addWidget(self.b_contact_lbl)

        self.b_address_lbl = QLabel(self.labels_frame)
        self.b_address_lbl.setObjectName(u"b_address_lbl")
        self.b_address_lbl.setFont(font3)

        self.verticalLayout_15.addWidget(self.b_address_lbl)


        self.horizontalLayout_18.addWidget(self.labels_frame)


        self.verticalLayout.addWidget(self.main_details_widget, 0, Qt.AlignVCenter)

        self.bottom_frame = QFrame(self.centralwidget)
        self.bottom_frame.setObjectName(u"bottom_frame")
        self.bottom_frame.setMinimumSize(QSize(0, 0))
        self.bottom_frame.setMaximumSize(QSize(16777215, 70))
        self.bottom_frame.setLayoutDirection(Qt.RightToLeft)
        self.bottom_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_cancel = QPushButton(self.bottom_frame)
        self.btn_cancel.setObjectName(u"btn_cancel")
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.btn_cancel.setFont(font4)
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancel.setIcon(icon1)
        self.btn_cancel.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_cancel)

        self.btn_clear = QPushButton(self.bottom_frame)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setFont(font4)
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear.setIcon(icon2)
        self.btn_clear.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_clear)

        self.btn_update = QPushButton(self.bottom_frame)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setFont(font4)
        self.btn_update.setLayoutDirection(Qt.RightToLeft)
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update.setIcon(icon3)
        self.btn_update.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_update)


        self.verticalLayout.addWidget(self.bottom_frame)

        UpdateBusinessWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UpdateBusinessWindow)

        QMetaObject.connectSlotsByName(UpdateBusinessWindow)
    # setupUi

    def retranslateUi(self, UpdateBusinessWindow):
        UpdateBusinessWindow.setWindowTitle(QCoreApplication.translate("UpdateBusinessWindow", u"Update School Details", None))
        self.label.setText(QCoreApplication.translate("UpdateBusinessWindow", u"School Details", None))
        self.txt_business_logo.setText(QCoreApplication.translate("UpdateBusinessWindow", u"Logo", None))
        self.b_name_lbl.setText(QCoreApplication.translate("UpdateBusinessWindow", u"School Name", None))
        self.b_contact_lbl.setText(QCoreApplication.translate("UpdateBusinessWindow", u"Contact", None))
        self.b_address_lbl.setText(QCoreApplication.translate("UpdateBusinessWindow", u"Address", None))
        self.btn_cancel.setText(QCoreApplication.translate("UpdateBusinessWindow", u"Cancel", None))
        self.btn_clear.setText(QCoreApplication.translate("UpdateBusinessWindow", u"Clear", None))
        self.btn_update.setText(QCoreApplication.translate("UpdateBusinessWindow", u"Update", None))
    # retranslateUi

