import sqlite3
import os

class DBHandler:
    def __init__(self):
        if not os.path.isdir("database"):
            os.mkdir("database")
        self.db_name = "database/db.sqlite"
        if not os.path.isfile(self.db_name):
            # create db
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        else:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()

        self.create_table("users", "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, contact TEXT, username TEXT, password TEXT,is_admin INTEGER DEFAULT 0")
        self.create_table("expenses", "id INTEGER PRIMARY KEY AUTOINCREMENT, hoa TEXT, amount REAL, date DATE, payment_type TEXT, recipient_name TEXT, comment TEXT DEFAULT 'No Comment'")
        self.create_table("expense_types", "id INTEGER PRIMARY KEY AUTOINCREMENT, head_of_account TEXT")
        self.create_table("classes", "id INTEGER PRIMARY KEY AUTOINCREMENT, class_name TEXT")
        self.create_table("subjects", "id INTEGER PRIMARY KEY AUTOINCREMENT, subject_name TEXT,passing_mark INTEGER,total_mark INTEGER,class_id INTEGER, FOREIGN KEY(class_id) REFERENCES classes(id)")
        self.create_table("students", "id INTEGER PRIMARY KEY AUTOINCREMENT, addmission_date DATE,addmission_no TEXT,name TEXT,f_name TEXT,dob TEXT,address TEXT,contact TEXT,gender TEXT,section TEXT,last_school TEXT DEFAULT '',student_image TEXT, special_case TEXT DEFAULT '',remaining_fee REAL DEFAULT 0,status TEXT DEFAULT 'Active',description TEXT DEFAULT '', class_id INTEGER, FOREIGN KEY(class_id) REFERENCES classes(id)")
        self.create_table("fee", "id INTEGER PRIMARY KEY AUTOINCREMENT, addmission_fee REAL,jan_fee REAL,feb_fee REAL,march_fee REAL,april_fee REAL,may_fee REAL,june_fee REAL,july_fee REAL,august_fee REAL,sep_fee REAL,oct_fee REAL,nov_fee REAL,dec_fee REAL,annual_fund REAL,computer_lab_fee REAL,science_lab_fee REAL,date DATE,total REAL,std_id INTEGER, FOREIGN KEY(std_id) REFERENCES students(id)")
        # self.create_table("fee", "id INTEGER PRIMARY KEY AUTOINCREMENT, addmission_fee REAL,monthly_fee REAL,annual_fund REAL,computer_lab_fee REAL,science_lab_fee REAL,date DATE,total REAL,std_id INTEGER, FOREIGN KEY(std_id) REFERENCES students(id)")
        self.create_table("transactions", "id INTEGER PRIMARY KEY AUTOINCREMENT,paid_fee REAL,discount REAL,date DATE,challan_no TEXT,description TEXT,remaining_fee INTERGER, fee_id INTEGER, FOREIGN KEY(fee_id) REFERENCES fee(id)")
        self.create_table("exams", "id INTEGER PRIMARY KEY AUTOINCREMENT, exam_name TEXT, date DATE, class_id INTEGER, student_id INTEGER, FOREIGN KEY(class_id) REFERENCES classes(id), FOREIGN KEY(student_id) REFERENCES students(id)")
        self.create_table("exam_details", "id INTEGER PRIMARY KEY AUTOINCREMENT, exam_id INTEGER, subject_id INTEGER, marks INTEGER, FOREIGN KEY(exam_id) REFERENCES exams(id), FOREIGN KEY(subject_id) REFERENCES subjects(id)")
        self.create_table("school_info", "id INTEGER PRIMARY KEY AUTOINCREMENT, school_name TEXT, contact TEXT, address TEXT, logo TEXT")

        # CREATE TABLE transactions (
#   id INTEGER PRIMARY KEY AUTOINCREMENT, 
#   paid_fee REAL,
#   date DATE,
#   challan_no TEXT,
#   description TEXT,
#   remaining_fee INTEGER, 
#   fee_id INTEGER, 
#   FOREIGN KEY(fee_id) REFERENCES fee(id)
# );
        # SELECT * FROM transactions WHERE substr(date, 7, 4) || '-' || substr(date, 4, 2) || '-' || substr(date, 1, 2) < '2023-02-01';


    def create_table(self, table_name, columns):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
        self.conn.commit()

    def check_table(self, table_name):
        self.cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        if self.cursor.fetchall():
            return True
        return False


    def insert(self, table_name, columns, values):
        self.cursor.execute(f"INSERT INTO {table_name} ({columns}) VALUES ({values})")
        self.conn.commit()

    def select(self, table_name, columns, condition):
        self.cursor.execute(f"SELECT {columns} FROM {table_name} WHERE {condition}")
        return self.cursor.fetchall()

    def select_all(self, table_name, columns):
        self.cursor.execute(f"SELECT {columns} FROM {table_name}")
        return self.cursor.fetchall()

    def update(self, table_name, columns, values, condition):
        self.cursor.execute(f"UPDATE {table_name} SET {columns} = {values} WHERE {condition}")
        self.conn.commit()

    def delete(self, table_name, condition):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {condition}")
        self.conn.commit()

    def close(self):
        self.conn.close()

    def authenticate(self,username, password):
        self.cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
        if self.cursor.fetchall():
            return True
        return False


    