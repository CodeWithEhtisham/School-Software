# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1386, 948)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"\n"
"QPushButton, QComboBox {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: #fff;\n"
"	border: 1px solid #039be5;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QDateEdit {\n"
"	background-color: #fff;\n"
"	border: 1px solid #039be5;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#upper_widget {\n"
"	background-color: #4dd0e1;\n"
"}")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.upper_widget = QWidget(self.centralwidget)
        self.upper_widget.setObjectName(u"upper_widget")
        self.horizontalLayout_9 = QHBoxLayout(self.upper_widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_home = QPushButton(self.upper_widget)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(120, 40))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_home.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)
        self.btn_home.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.btn_home, 0, Qt.AlignLeft)

        self.btn_students = QPushButton(self.upper_widget)
        self.btn_students.setObjectName(u"btn_students")
        self.btn_students.setMinimumSize(QSize(150, 40))
        self.btn_students.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/customers_blue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_students.setIcon(icon2)
        self.btn_students.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.btn_students)

        self.btn_class = QPushButton(self.upper_widget)
        self.btn_class.setObjectName(u"btn_class")
        self.btn_class.setMinimumSize(QSize(150, 40))
        self.btn_class.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/products.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_class.setIcon(icon3)
        self.btn_class.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.btn_class)

        self.btn_reports = QPushButton(self.upper_widget)
        self.btn_reports.setObjectName(u"btn_reports")
        self.btn_reports.setMinimumSize(QSize(150, 40))
        self.btn_reports.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/icons/reports.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reports.setIcon(icon4)
        self.btn_reports.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.btn_reports)

        self.btn_expense = QPushButton(self.upper_widget)
        self.btn_expense.setObjectName(u"btn_expense")
        self.btn_expense.setMinimumSize(QSize(150, 40))
        self.btn_expense.setFont(font)
        self.btn_expense.setIcon(icon4)
        self.btn_expense.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.btn_expense)

        self.btn_settings = QPushButton(self.upper_widget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(150, 40))
        self.btn_settings.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon5)
        self.btn_settings.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.btn_settings)

        self.btn_logout = QPushButton(self.upper_widget)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(100, 40))
        self.btn_logout.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/icons/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout.setIcon(icon6)
        self.btn_logout.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.btn_logout, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.upper_widget)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"\n"
"#lbl_logo {\n"
"	background-color: #fff;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"* {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                            stop:0 #ffffff, stop:1 #00bcd4);\n"
"}")
        self.verticalLayout_8 = QVBoxLayout(self.home_page)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lbl_home = QLabel(self.home_page)
        self.lbl_home.setObjectName(u"lbl_home")
        self.lbl_home.setMinimumSize(QSize(0, 50))
        self.lbl_home.setMaximumSize(QSize(16777215, 50))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.lbl_home.setFont(font1)
        self.lbl_home.setAlignment(Qt.AlignCenter)
        self.lbl_home.setMargin(10)

        self.verticalLayout_8.addWidget(self.lbl_home)

        self.widget_7 = QWidget(self.home_page)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout = QVBoxLayout(self.widget_7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_logo = QLabel(self.widget_7)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setMinimumSize(QSize(150, 150))
        self.lbl_logo.setMaximumSize(QSize(150, 150))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(20)
        self.lbl_logo.setFont(font2)
        self.lbl_logo.setFrameShape(QFrame.Box)
        self.lbl_logo.setFrameShadow(QFrame.Raised)
        self.lbl_logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_logo, 0, Qt.AlignHCenter)

        self.lbl_school_name = QLabel(self.widget_7)
        self.lbl_school_name.setObjectName(u"lbl_school_name")
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(24)
        font3.setBold(True)
        font3.setWeight(75)
        self.lbl_school_name.setFont(font3)
        self.lbl_school_name.setAlignment(Qt.AlignCenter)
        self.lbl_school_name.setMargin(10)

        self.verticalLayout.addWidget(self.lbl_school_name, 0, Qt.AlignBottom)

        self.lbl_school_address = QLabel(self.widget_7)
        self.lbl_school_address.setObjectName(u"lbl_school_address")
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(18)
        self.lbl_school_address.setFont(font4)
        self.lbl_school_address.setAlignment(Qt.AlignCenter)
        self.lbl_school_address.setMargin(10)

        self.verticalLayout.addWidget(self.lbl_school_address, 0, Qt.AlignVCenter)

        self.lbl_school_contact = QLabel(self.widget_7)
        self.lbl_school_contact.setObjectName(u"lbl_school_contact")
        self.lbl_school_contact.setFont(font4)
        self.lbl_school_contact.setAlignment(Qt.AlignCenter)
        self.lbl_school_contact.setMargin(10)

        self.verticalLayout.addWidget(self.lbl_school_contact, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.widget_7, 0, Qt.AlignVCenter)

        self.home_bottom_widget = QWidget(self.home_page)
        self.home_bottom_widget.setObjectName(u"home_bottom_widget")
        self.home_bottom_widget.setMinimumSize(QSize(0, 50))
        self.home_bottom_widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.home_bottom_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_15 = QLabel(self.home_bottom_widget)
        self.label_15.setObjectName(u"label_15")
        font5 = QFont()
        font5.setFamily(u"Calibri")
        font5.setPointSize(16)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_15.setFont(font5)

        self.horizontalLayout.addWidget(self.label_15, 0, Qt.AlignLeft)

        self.label_16 = QLabel(self.home_bottom_widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font5)

        self.horizontalLayout.addWidget(self.label_16, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.home_bottom_widget, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.home_page)
        self.students_page = QWidget()
        self.students_page.setObjectName(u"students_page")
        self.students_page.setStyleSheet(u"\n"
"#lbl_students {\n"
"	background-color: #81d4fa;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"#student_upper_widget {\n"
"	background-color: #b3e5fc;\n"
"}\n"
"\n"
"#student_bottom_widget {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                            stop:0 #ffffff, stop:1 #00bcd4);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.students_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lbl_students = QLabel(self.students_page)
        self.lbl_students.setObjectName(u"lbl_students")
        self.lbl_students.setFont(font1)
        self.lbl_students.setAlignment(Qt.AlignCenter)
        self.lbl_students.setMargin(0)

        self.verticalLayout_5.addWidget(self.lbl_students)

        self.student_upper_widget = QWidget(self.students_page)
        self.student_upper_widget.setObjectName(u"student_upper_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.student_upper_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btn_add_student = QPushButton(self.student_upper_widget)
        self.btn_add_student.setObjectName(u"btn_add_student")
        self.btn_add_student.setMinimumSize(QSize(150, 35))
        self.btn_add_student.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_student.setIcon(icon7)
        self.btn_add_student.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.btn_add_student, 0, Qt.AlignLeft)

        self.btn_add_fees = QPushButton(self.student_upper_widget)
        self.btn_add_fees.setObjectName(u"btn_add_fees")
        self.btn_add_fees.setMinimumSize(QSize(150, 35))
        self.btn_add_fees.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/icons/fee.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_fees.setIcon(icon8)
        self.btn_add_fees.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.btn_add_fees, 0, Qt.AlignLeft)

        self.btn_add_result = QPushButton(self.student_upper_widget)
        self.btn_add_result.setObjectName(u"btn_add_result")
        self.btn_add_result.setMinimumSize(QSize(150, 35))
        self.btn_add_result.setFont(font)
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/icons/results.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_result.setIcon(icon9)
        self.btn_add_result.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.btn_add_result, 0, Qt.AlignLeft)

        self.select_class = QComboBox(self.student_upper_widget)
        self.select_class.addItem("")
        self.select_class.setObjectName(u"select_class")
        self.select_class.setMinimumSize(QSize(150, 35))
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setWeight(50)
        self.select_class.setFont(font6)

        self.horizontalLayout_6.addWidget(self.select_class)

        self.txt_search_student = QLineEdit(self.student_upper_widget)
        self.txt_search_student.setObjectName(u"txt_search_student")
        self.txt_search_student.setMinimumSize(QSize(400, 35))
        font7 = QFont()
        font7.setFamily(u"Calibri")
        font7.setPointSize(14)
        self.txt_search_student.setFont(font7)

        self.horizontalLayout_6.addWidget(self.txt_search_student, 0, Qt.AlignLeft)

        self.btn_pay_fee = QPushButton(self.student_upper_widget)
        self.btn_pay_fee.setObjectName(u"btn_pay_fee")
        self.btn_pay_fee.setMinimumSize(QSize(120, 35))
        self.btn_pay_fee.setFont(font)
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/icons/sales.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pay_fee.setIcon(icon10)
        self.btn_pay_fee.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.btn_pay_fee)

        self.btn_edit_student = QPushButton(self.student_upper_widget)
        self.btn_edit_student.setObjectName(u"btn_edit_student")
        self.btn_edit_student.setMinimumSize(QSize(35, 35))
        icon11 = QIcon()
        icon11.addFile(u":/icons/assets/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_student.setIcon(icon11)
        self.btn_edit_student.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.btn_edit_student, 0, Qt.AlignRight)

        self.btn_print_student = QPushButton(self.student_upper_widget)
        self.btn_print_student.setObjectName(u"btn_print_student")
        self.btn_print_student.setMinimumSize(QSize(35, 35))
        icon12 = QIcon()
        icon12.addFile(u":/icons/assets/icons/print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_print_student.setIcon(icon12)
        self.btn_print_student.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.btn_print_student, 0, Qt.AlignRight)

        self.btn_refresh_student = QPushButton(self.student_upper_widget)
        self.btn_refresh_student.setObjectName(u"btn_refresh_student")
        self.btn_refresh_student.setMinimumSize(QSize(35, 35))
        icon13 = QIcon()
        icon13.addFile(u":/icons/assets/icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh_student.setIcon(icon13)
        self.btn_refresh_student.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.btn_refresh_student, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.student_upper_widget)

        self.students_table = QTableWidget(self.students_page)
        if (self.students_table.columnCount() < 8):
            self.students_table.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.students_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.students_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.students_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.students_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.students_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.students_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.students_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.students_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        if (self.students_table.rowCount() < 15):
            self.students_table.setRowCount(15)
        self.students_table.setObjectName(u"students_table")
        self.students_table.setFont(font7)
        self.students_table.setFrameShape(QFrame.Box)
        self.students_table.setFrameShadow(QFrame.Raised)
        self.students_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.students_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.students_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.students_table.setRowCount(15)
        self.students_table.horizontalHeader().setDefaultSectionSize(180)
        self.students_table.verticalHeader().setMinimumSectionSize(35)
        self.students_table.verticalHeader().setDefaultSectionSize(35)

        self.verticalLayout_5.addWidget(self.students_table)

        self.student_bottom_widget = QWidget(self.students_page)
        self.student_bottom_widget.setObjectName(u"student_bottom_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.student_bottom_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.student_bottom_widget)
        self.label_4.setObjectName(u"label_4")
        font8 = QFont()
        font8.setFamily(u"Calibri")
        font8.setPointSize(16)
        self.label_4.setFont(font8)

        self.horizontalLayout_5.addWidget(self.label_4, 0, Qt.AlignRight)

        self.lbl_total_students = QLabel(self.student_bottom_widget)
        self.lbl_total_students.setObjectName(u"lbl_total_students")
        self.lbl_total_students.setFont(font5)
        self.lbl_total_students.setFrameShape(QFrame.Box)
        self.lbl_total_students.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.lbl_total_students, 0, Qt.AlignLeft)


        self.verticalLayout_5.addWidget(self.student_bottom_widget)

        self.stackedWidget.addWidget(self.students_page)
        self.expense_page = QWidget()
        self.expense_page.setObjectName(u"expense_page")
        self.expense_page.setStyleSheet(u"\n"
"#lbl_expenses {\n"
"	background-color: #81d4fa;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"#exp_upper_widget {\n"
"	background-color: #b3e5fc;\n"
"}\n"
"\n"
"#exp_bottom_widget {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                            stop:0 #ffffff, stop:1 #00bcd4);\n"
"}\n"
"")
        self.verticalLayout_6 = QVBoxLayout(self.expense_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_expenses = QLabel(self.expense_page)
        self.lbl_expenses.setObjectName(u"lbl_expenses")
        self.lbl_expenses.setFont(font1)
        self.lbl_expenses.setAlignment(Qt.AlignCenter)
        self.lbl_expenses.setMargin(0)

        self.verticalLayout_6.addWidget(self.lbl_expenses)

        self.exp_upper_widget = QWidget(self.expense_page)
        self.exp_upper_widget.setObjectName(u"exp_upper_widget")
        self.horizontalLayout_7 = QHBoxLayout(self.exp_upper_widget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.btn_add_expense = QPushButton(self.exp_upper_widget)
        self.btn_add_expense.setObjectName(u"btn_add_expense")
        self.btn_add_expense.setMinimumSize(QSize(150, 35))
        self.btn_add_expense.setFont(font)
        self.btn_add_expense.setIcon(icon7)
        self.btn_add_expense.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.btn_add_expense, 0, Qt.AlignLeft)

        self.txt_expense_search = QLineEdit(self.exp_upper_widget)
        self.txt_expense_search.setObjectName(u"txt_expense_search")
        self.txt_expense_search.setMinimumSize(QSize(400, 35))
        self.txt_expense_search.setFont(font7)

        self.horizontalLayout_7.addWidget(self.txt_expense_search, 0, Qt.AlignLeft)

        self.btn_expense_type = QPushButton(self.exp_upper_widget)
        self.btn_expense_type.setObjectName(u"btn_expense_type")
        self.btn_expense_type.setMinimumSize(QSize(150, 35))
        self.btn_expense_type.setFont(font7)
        self.btn_expense_type.setIcon(icon10)
        self.btn_expense_type.setIconSize(QSize(30, 30))

        self.horizontalLayout_7.addWidget(self.btn_expense_type, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.exp_upper_widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setSpacing(20)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_expense = QPushButton(self.frame_5)
        self.btn_edit_expense.setObjectName(u"btn_edit_expense")
        self.btn_edit_expense.setMinimumSize(QSize(35, 35))
        self.btn_edit_expense.setIcon(icon11)
        self.btn_edit_expense.setIconSize(QSize(32, 32))

        self.horizontalLayout_13.addWidget(self.btn_edit_expense)

        self.btn_print_expense = QPushButton(self.frame_5)
        self.btn_print_expense.setObjectName(u"btn_print_expense")
        self.btn_print_expense.setMinimumSize(QSize(35, 35))
        self.btn_print_expense.setIcon(icon12)
        self.btn_print_expense.setIconSize(QSize(32, 32))

        self.horizontalLayout_13.addWidget(self.btn_print_expense)

        self.btn_expense_refresh = QPushButton(self.frame_5)
        self.btn_expense_refresh.setObjectName(u"btn_expense_refresh")
        self.btn_expense_refresh.setMinimumSize(QSize(35, 35))
        self.btn_expense_refresh.setIcon(icon13)
        self.btn_expense_refresh.setIconSize(QSize(32, 32))

        self.horizontalLayout_13.addWidget(self.btn_expense_refresh)


        self.horizontalLayout_7.addWidget(self.frame_5, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.exp_upper_widget)

        self.expense_table = QTableWidget(self.expense_page)
        if (self.expense_table.columnCount() < 6):
            self.expense_table.setColumnCount(6)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.expense_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.expense_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.expense_table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.expense_table.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.expense_table.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font);
        self.expense_table.setHorizontalHeaderItem(5, __qtablewidgetitem13)
        if (self.expense_table.rowCount() < 15):
            self.expense_table.setRowCount(15)
        self.expense_table.setObjectName(u"expense_table")
        self.expense_table.setFont(font7)
        self.expense_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.expense_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.expense_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.expense_table.setRowCount(15)
        self.expense_table.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_6.addWidget(self.expense_table)

        self.exp_bottom_widget = QWidget(self.expense_page)
        self.exp_bottom_widget.setObjectName(u"exp_bottom_widget")
        self.horizontalLayout_8 = QHBoxLayout(self.exp_bottom_widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_6 = QLabel(self.exp_bottom_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font8)

        self.horizontalLayout_8.addWidget(self.label_6, 0, Qt.AlignRight)

        self.total_expense = QLabel(self.exp_bottom_widget)
        self.total_expense.setObjectName(u"total_expense")
        self.total_expense.setFont(font5)
        self.total_expense.setFrameShape(QFrame.Box)
        self.total_expense.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.total_expense, 0, Qt.AlignLeft)


        self.verticalLayout_6.addWidget(self.exp_bottom_widget)

        self.stackedWidget.addWidget(self.expense_page)
        self.class_page = QWidget()
        self.class_page.setObjectName(u"class_page")
        self.class_page.setStyleSheet(u"\n"
"#lbl_class {\n"
"	background-color: #81d4fa;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"#class_upper_widget {\n"
"	background-color: #b3e5fc;\n"
"}\n"
"\n"
"#widget_5 {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                            stop:0 #ffffff, stop:1 #00bcd4);\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.class_page)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lbl_class = QLabel(self.class_page)
        self.lbl_class.setObjectName(u"lbl_class")
        self.lbl_class.setFont(font1)
        self.lbl_class.setAlignment(Qt.AlignCenter)
        self.lbl_class.setMargin(0)

        self.verticalLayout_4.addWidget(self.lbl_class)

        self.class_upper_widget = QWidget(self.class_page)
        self.class_upper_widget.setObjectName(u"class_upper_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.class_upper_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_add_class = QPushButton(self.class_upper_widget)
        self.btn_add_class.setObjectName(u"btn_add_class")
        self.btn_add_class.setMinimumSize(QSize(150, 35))
        self.btn_add_class.setFont(font)
        self.btn_add_class.setIcon(icon7)
        self.btn_add_class.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.btn_add_class, 0, Qt.AlignLeft)

        self.btn_edit_class = QPushButton(self.class_upper_widget)
        self.btn_edit_class.setObjectName(u"btn_edit_class")
        self.btn_edit_class.setMinimumSize(QSize(150, 35))
        self.btn_edit_class.setFont(font7)
        self.btn_edit_class.setIcon(icon11)
        self.btn_edit_class.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.btn_edit_class, 0, Qt.AlignLeft)

        self.btn_add_subject = QPushButton(self.class_upper_widget)
        self.btn_add_subject.setObjectName(u"btn_add_subject")
        self.btn_add_subject.setMinimumSize(QSize(170, 35))
        self.btn_add_subject.setFont(font)
        self.btn_add_subject.setIcon(icon7)
        self.btn_add_subject.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.btn_add_subject, 0, Qt.AlignLeft)

        self.btn_edit_subject = QPushButton(self.class_upper_widget)
        self.btn_edit_subject.setObjectName(u"btn_edit_subject")
        self.btn_edit_subject.setMinimumSize(QSize(150, 35))
        self.btn_edit_subject.setFont(font7)
        self.btn_edit_subject.setIcon(icon11)
        self.btn_edit_subject.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.btn_edit_subject, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.class_upper_widget)

        self.widget_6 = QWidget(self.class_page)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget_6)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setMargin(5)

        self.verticalLayout_3.addWidget(self.label_12)

        self.class_table = QTableWidget(self.frame)
        if (self.class_table.columnCount() < 1):
            self.class_table.setColumnCount(1)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font);
        self.class_table.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        if (self.class_table.rowCount() < 10):
            self.class_table.setRowCount(10)
        self.class_table.setObjectName(u"class_table")
        self.class_table.setFont(font7)
        self.class_table.setFrameShape(QFrame.Box)
        self.class_table.setFrameShadow(QFrame.Raised)
        self.class_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.class_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.class_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.class_table.setRowCount(10)
        self.class_table.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_3.addWidget(self.class_table)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.widget_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font5)
        self.label_13.setAlignment(Qt.AlignCenter)
        self.label_13.setMargin(5)

        self.verticalLayout_2.addWidget(self.label_13)

        self.subjects_table = QTableWidget(self.frame_2)
        if (self.subjects_table.columnCount() < 3):
            self.subjects_table.setColumnCount(3)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font);
        self.subjects_table.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font);
        self.subjects_table.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font);
        self.subjects_table.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        if (self.subjects_table.rowCount() < 10):
            self.subjects_table.setRowCount(10)
        self.subjects_table.setObjectName(u"subjects_table")
        self.subjects_table.setFont(font7)
        self.subjects_table.setFrameShape(QFrame.Box)
        self.subjects_table.setFrameShadow(QFrame.Raised)
        self.subjects_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.subjects_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.subjects_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.subjects_table.setRowCount(10)
        self.subjects_table.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_2.addWidget(self.subjects_table)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout_4.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.class_page)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font8)

        self.horizontalLayout_3.addWidget(self.label_8, 0, Qt.AlignRight)

        self.lbl_total_classes = QLabel(self.widget_5)
        self.lbl_total_classes.setObjectName(u"lbl_total_classes")
        self.lbl_total_classes.setFont(font5)
        self.lbl_total_classes.setFrameShape(QFrame.Box)
        self.lbl_total_classes.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.lbl_total_classes, 0, Qt.AlignLeft)

        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font8)

        self.horizontalLayout_3.addWidget(self.label_10, 0, Qt.AlignRight)

        self.lbl_total_subjects = QLabel(self.widget_5)
        self.lbl_total_subjects.setObjectName(u"lbl_total_subjects")
        self.lbl_total_subjects.setFont(font5)
        self.lbl_total_subjects.setFrameShape(QFrame.Box)
        self.lbl_total_subjects.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.lbl_total_subjects, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.widget_5)

        self.stackedWidget.addWidget(self.class_page)
        self.reports_page = QWidget()
        self.reports_page.setObjectName(u"reports_page")
        self.reports_page.setStyleSheet(u"\n"
"#lbl_reports {\n"
"	background-color: #81d4fa;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"#reports_upper_widget {\n"
"	background-color: #b3e5fc;\n"
"}\n"
"\n"
"#reports_bottom_widget, #label_21 {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"                            stop:0 #ffffff, stop:1 #00bcd4);\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.reports_page)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lbl_reports = QLabel(self.reports_page)
        self.lbl_reports.setObjectName(u"lbl_reports")
        self.lbl_reports.setFont(font1)
        self.lbl_reports.setAlignment(Qt.AlignCenter)
        self.lbl_reports.setMargin(0)

        self.verticalLayout_12.addWidget(self.lbl_reports)

        self.reports_upper_widget = QWidget(self.reports_page)
        self.reports_upper_widget.setObjectName(u"reports_upper_widget")
        self.horizontalLayout_12 = QHBoxLayout(self.reports_upper_widget)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.btn_defaulters = QPushButton(self.reports_upper_widget)
        self.btn_defaulters.setObjectName(u"btn_defaulters")
        self.btn_defaulters.setMinimumSize(QSize(220, 35))
        self.btn_defaulters.setFont(font)
        icon14 = QIcon()
        icon14.addFile(u":/icons/assets/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_defaulters.setIcon(icon14)
        self.btn_defaulters.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.btn_defaulters, 0, Qt.AlignLeft)

        self.txt_search_report = QLineEdit(self.reports_upper_widget)
        self.txt_search_report.setObjectName(u"txt_search_report")
        self.txt_search_report.setMinimumSize(QSize(400, 35))
        self.txt_search_report.setFont(font7)

        self.horizontalLayout_12.addWidget(self.txt_search_report, 0, Qt.AlignLeft)

        self.label_5 = QLabel(self.reports_upper_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)

        self.horizontalLayout_12.addWidget(self.label_5)

        self.report_from_date = QDateEdit(self.reports_upper_widget)
        self.report_from_date.setObjectName(u"report_from_date")
        self.report_from_date.setMinimumSize(QSize(150, 35))
        self.report_from_date.setFont(font7)
        self.report_from_date.setCalendarPopup(True)

        self.horizontalLayout_12.addWidget(self.report_from_date)

        self.label_9 = QLabel(self.reports_upper_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font7)

        self.horizontalLayout_12.addWidget(self.label_9)

        self.report_to_date = QDateEdit(self.reports_upper_widget)
        self.report_to_date.setObjectName(u"report_to_date")
        self.report_to_date.setMinimumSize(QSize(150, 35))
        self.report_to_date.setFont(font7)
        self.report_to_date.setCalendarPopup(True)

        self.horizontalLayout_12.addWidget(self.report_to_date)

        self.btn_date_search = QPushButton(self.reports_upper_widget)
        self.btn_date_search.setObjectName(u"btn_date_search")
        self.btn_date_search.setMinimumSize(QSize(35, 35))
        self.btn_date_search.setIcon(icon14)
        self.btn_date_search.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.btn_date_search)

        self.btn_monthly = QPushButton(self.reports_upper_widget)
        self.btn_monthly.setObjectName(u"btn_monthly")
        self.btn_monthly.setMinimumSize(QSize(120, 35))
        self.btn_monthly.setFont(font)
        self.btn_monthly.setIcon(icon14)
        self.btn_monthly.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.btn_monthly)

        self.btn_yearly = QPushButton(self.reports_upper_widget)
        self.btn_yearly.setObjectName(u"btn_yearly")
        self.btn_yearly.setMinimumSize(QSize(120, 35))
        self.btn_yearly.setFont(font)
        self.btn_yearly.setIcon(icon14)
        self.btn_yearly.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.btn_yearly)

        self.btn_reports_print = QPushButton(self.reports_upper_widget)
        self.btn_reports_print.setObjectName(u"btn_reports_print")
        self.btn_reports_print.setMinimumSize(QSize(35, 35))
        self.btn_reports_print.setIcon(icon12)
        self.btn_reports_print.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.btn_reports_print, 0, Qt.AlignRight)

        self.btn_reports_refresh = QPushButton(self.reports_upper_widget)
        self.btn_reports_refresh.setObjectName(u"btn_reports_refresh")
        self.btn_reports_refresh.setMinimumSize(QSize(35, 35))
        self.btn_reports_refresh.setIcon(icon13)
        self.btn_reports_refresh.setIconSize(QSize(32, 32))

        self.horizontalLayout_12.addWidget(self.btn_reports_refresh, 0, Qt.AlignLeft)


        self.verticalLayout_12.addWidget(self.reports_upper_widget)

        self.daily_reports_table = QTableWidget(self.reports_page)
        if (self.daily_reports_table.columnCount() < 7):
            self.daily_reports_table.setColumnCount(7)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font);
        self.daily_reports_table.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font);
        self.daily_reports_table.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font);
        self.daily_reports_table.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font);
        self.daily_reports_table.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font);
        self.daily_reports_table.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font);
        self.daily_reports_table.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font);
        self.daily_reports_table.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        if (self.daily_reports_table.rowCount() < 10):
            self.daily_reports_table.setRowCount(10)
        self.daily_reports_table.setObjectName(u"daily_reports_table")
        self.daily_reports_table.setFont(font7)
        self.daily_reports_table.setFrameShape(QFrame.Box)
        self.daily_reports_table.setFrameShadow(QFrame.Raised)
        self.daily_reports_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.daily_reports_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.daily_reports_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.daily_reports_table.setRowCount(10)
        self.daily_reports_table.horizontalHeader().setDefaultSectionSize(150)
        self.daily_reports_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_12.addWidget(self.daily_reports_table)

        self.label_21 = QLabel(self.reports_page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font5)
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setMargin(5)

        self.verticalLayout_12.addWidget(self.label_21)

        self.reports_bottom_widget = QWidget(self.reports_page)
        self.reports_bottom_widget.setObjectName(u"reports_bottom_widget")
        self.horizontalLayout_11 = QHBoxLayout(self.reports_bottom_widget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(self.reports_bottom_widget)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font5)

        self.horizontalLayout_11.addWidget(self.label)

        self.frame_3 = QFrame(self.reports_bottom_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font7)

        self.verticalLayout_10.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font7)

        self.verticalLayout_10.addWidget(self.label_3)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font7)

        self.verticalLayout_10.addWidget(self.label_7)

        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.verticalLayout_10.addWidget(self.label_14)


        self.horizontalLayout_11.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.reports_bottom_widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lbl_total_amount_received = QLabel(self.frame_4)
        self.lbl_total_amount_received.setObjectName(u"lbl_total_amount_received")
        self.lbl_total_amount_received.setFont(font7)

        self.verticalLayout_11.addWidget(self.lbl_total_amount_received)

        self.lbl_total_amount_remaining = QLabel(self.frame_4)
        self.lbl_total_amount_remaining.setObjectName(u"lbl_total_amount_remaining")
        self.lbl_total_amount_remaining.setFont(font7)

        self.verticalLayout_11.addWidget(self.lbl_total_amount_remaining)

        self.lbl_total_expense = QLabel(self.frame_4)
        self.lbl_total_expense.setObjectName(u"lbl_total_expense")
        self.lbl_total_expense.setFont(font7)

        self.verticalLayout_11.addWidget(self.lbl_total_expense)

        self.lbl_net_balance = QLabel(self.frame_4)
        self.lbl_net_balance.setObjectName(u"lbl_net_balance")
        self.lbl_net_balance.setFont(font)

        self.verticalLayout_11.addWidget(self.lbl_net_balance)


        self.horizontalLayout_11.addWidget(self.frame_4)


        self.verticalLayout_12.addWidget(self.reports_bottom_widget)

        self.stackedWidget.addWidget(self.reports_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setStyleSheet(u"\n"
"\n"
"#lbl_settings {\n"
"	background-color: #81d4fa;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"#settings_upper_widget {\n"
"	background-color: #b3e5fc;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.settings_page)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lbl_settings = QLabel(self.settings_page)
        self.lbl_settings.setObjectName(u"lbl_settings")
        self.lbl_settings.setFont(font1)
        self.lbl_settings.setAlignment(Qt.AlignCenter)
        self.lbl_settings.setMargin(0)

        self.verticalLayout_9.addWidget(self.lbl_settings)

        self.settings_upper_widget = QWidget(self.settings_page)
        self.settings_upper_widget.setObjectName(u"settings_upper_widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.settings_upper_widget.sizePolicy().hasHeightForWidth())
        self.settings_upper_widget.setSizePolicy(sizePolicy2)
        self.horizontalLayout_10 = QHBoxLayout(self.settings_upper_widget)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_add_school_details = QPushButton(self.settings_upper_widget)
        self.btn_add_school_details.setObjectName(u"btn_add_school_details")
        self.btn_add_school_details.setMinimumSize(QSize(250, 35))
        self.btn_add_school_details.setMaximumSize(QSize(16777215, 16777215))
        self.btn_add_school_details.setFont(font)
        self.btn_add_school_details.setIcon(icon7)
        self.btn_add_school_details.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.btn_add_school_details, 0, Qt.AlignLeft)

        self.btn_add_user = QPushButton(self.settings_upper_widget)
        self.btn_add_user.setObjectName(u"btn_add_user")
        self.btn_add_user.setMinimumSize(QSize(250, 35))
        self.btn_add_user.setFont(font)
        icon15 = QIcon()
        icon15.addFile(u":/icons/assets/icons/create_user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_user.setIcon(icon15)
        self.btn_add_user.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.btn_add_user, 0, Qt.AlignLeft)

        self.btn_edit_school_details = QPushButton(self.settings_upper_widget)
        self.btn_edit_school_details.setObjectName(u"btn_edit_school_details")
        self.btn_edit_school_details.setMinimumSize(QSize(230, 35))
        self.btn_edit_school_details.setMaximumSize(QSize(16777215, 16777215))
        self.btn_edit_school_details.setFont(font)
        self.btn_edit_school_details.setIcon(icon11)
        self.btn_edit_school_details.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.btn_edit_school_details, 0, Qt.AlignRight)

        self.btn_edit_user = QPushButton(self.settings_upper_widget)
        self.btn_edit_user.setObjectName(u"btn_edit_user")
        self.btn_edit_user.setMinimumSize(QSize(220, 35))
        self.btn_edit_user.setMaximumSize(QSize(16777215, 16777215))
        self.btn_edit_user.setFont(font)
        self.btn_edit_user.setIcon(icon11)
        self.btn_edit_user.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.btn_edit_user, 0, Qt.AlignRight)

        self.btn_change_password = QPushButton(self.settings_upper_widget)
        self.btn_change_password.setObjectName(u"btn_change_password")
        self.btn_change_password.setMinimumSize(QSize(200, 35))
        self.btn_change_password.setMaximumSize(QSize(16777215, 16777215))
        self.btn_change_password.setFont(font)
        self.btn_change_password.setIcon(icon11)
        self.btn_change_password.setIconSize(QSize(30, 30))

        self.horizontalLayout_10.addWidget(self.btn_change_password, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.settings_upper_widget)

        self.users_table = QTableWidget(self.settings_page)
        if (self.users_table.columnCount() < 5):
            self.users_table.setColumnCount(5)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font);
        self.users_table.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font);
        self.users_table.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font);
        self.users_table.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font);
        self.users_table.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font);
        self.users_table.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        self.users_table.setObjectName(u"users_table")
        self.users_table.setFont(font7)
        self.users_table.setFrameShape(QFrame.Box)
        self.users_table.setFrameShadow(QFrame.Raised)
        self.users_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.users_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.users_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.users_table.horizontalHeader().setDefaultSectionSize(170)

        self.verticalLayout_9.addWidget(self.users_table)

        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_7.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1386, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ComPy Softwares", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_students.setText(QCoreApplication.translate("MainWindow", u"Students", None))
        self.btn_class.setText(QCoreApplication.translate("MainWindow", u"Class", None))
        self.btn_reports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.btn_expense.setText(QCoreApplication.translate("MainWindow", u"Expense", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.lbl_home.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.lbl_logo.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
        self.lbl_school_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.lbl_school_address.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.lbl_school_contact.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Contact: +92 335 2321360", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Powered By: ComPy Softwares Quetta", None))
        self.lbl_students.setText(QCoreApplication.translate("MainWindow", u"Students", None))
        self.btn_add_student.setText(QCoreApplication.translate("MainWindow", u"Add Student", None))
        self.btn_add_fees.setText(QCoreApplication.translate("MainWindow", u"Add Fee", None))
        self.btn_add_result.setText(QCoreApplication.translate("MainWindow", u"Add Result", None))
        self.select_class.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Class", None))

        self.txt_search_student.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Here", None))
        self.btn_pay_fee.setText(QCoreApplication.translate("MainWindow", u"Pay Fee", None))
        self.btn_edit_student.setText("")
        self.btn_print_student.setText("")
        self.btn_refresh_student.setText("")
        ___qtablewidgetitem = self.students_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Adm Date", None));
        ___qtablewidgetitem1 = self.students_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Reg / Adm No.", None));
        ___qtablewidgetitem2 = self.students_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Student Name", None));
        ___qtablewidgetitem3 = self.students_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Father Name", None));
        ___qtablewidgetitem4 = self.students_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem5 = self.students_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Image", None));
        ___qtablewidgetitem6 = self.students_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Remaining Fee", None));
        ___qtablewidgetitem7 = self.students_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total Students:", None))
        self.lbl_total_students.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_expenses.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.btn_add_expense.setText(QCoreApplication.translate("MainWindow", u"Add Expense", None))
        self.txt_expense_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Here", None))
        self.btn_expense_type.setText(QCoreApplication.translate("MainWindow", u"Expense Type", None))
        self.btn_edit_expense.setText("")
        self.btn_print_expense.setText("")
        self.btn_expense_refresh.setText("")
        ___qtablewidgetitem8 = self.expense_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem9 = self.expense_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Head of Account", None));
        ___qtablewidgetitem10 = self.expense_table.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem11 = self.expense_table.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Payment Type", None));
        ___qtablewidgetitem12 = self.expense_table.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Recipient name", None));
        ___qtablewidgetitem13 = self.expense_table.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Comments", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Total Expense:", None))
        self.total_expense.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_class.setText(QCoreApplication.translate("MainWindow", u"Class / Subject", None))
        self.btn_add_class.setText(QCoreApplication.translate("MainWindow", u"Add Class", None))
        self.btn_edit_class.setText(QCoreApplication.translate("MainWindow", u"Edit Class", None))
        self.btn_add_subject.setText(QCoreApplication.translate("MainWindow", u"Add Subject", None))
        self.btn_edit_subject.setText(QCoreApplication.translate("MainWindow", u"Edit Subject", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Classes", None))
        ___qtablewidgetitem14 = self.class_table.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Class Name", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Subjects", None))
        ___qtablewidgetitem15 = self.subjects_table.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Subject Name", None));
        ___qtablewidgetitem16 = self.subjects_table.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Passing Marks", None));
        ___qtablewidgetitem17 = self.subjects_table.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Total Marks", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total Classes:", None))
        self.lbl_total_classes.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Total Subjects:", None))
        self.lbl_total_subjects.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_reports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.btn_defaulters.setText(QCoreApplication.translate("MainWindow", u"Defaulters Record", None))
        self.txt_search_report.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Here", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.btn_monthly.setText(QCoreApplication.translate("MainWindow", u"Monthly", None))
        self.btn_yearly.setText(QCoreApplication.translate("MainWindow", u"Yearly", None))
        self.btn_reports_print.setText("")
        self.btn_reports_refresh.setText("")
        ___qtablewidgetitem18 = self.daily_reports_table.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem19 = self.daily_reports_table.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"F / Name", None));
        ___qtablewidgetitem20 = self.daily_reports_table.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Class", None));
        ___qtablewidgetitem21 = self.daily_reports_table.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Challan No.", None));
        ___qtablewidgetitem22 = self.daily_reports_table.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Paid Amount", None));
        ___qtablewidgetitem23 = self.daily_reports_table.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Remaining", None));
        ___qtablewidgetitem24 = self.daily_reports_table.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Daily Report Summary", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Amount Received", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Amount Remaining", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Expense", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Net Balance", None))
        self.lbl_total_amount_received.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_total_amount_remaining.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_total_expense.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_net_balance.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_add_school_details.setText(QCoreApplication.translate("MainWindow", u"Add School Details", None))
        self.btn_add_user.setText(QCoreApplication.translate("MainWindow", u"Add New User", None))
        self.btn_edit_school_details.setText(QCoreApplication.translate("MainWindow", u"Change School Details", None))
        self.btn_edit_user.setText(QCoreApplication.translate("MainWindow", u"Change User Details", None))
        self.btn_change_password.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        ___qtablewidgetitem25 = self.users_table.horizontalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem26 = self.users_table.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem27 = self.users_table.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Contact", None));
        ___qtablewidgetitem28 = self.users_table.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem29 = self.users_table.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Password", None));
    # retranslateUi

