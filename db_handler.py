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

        self.create_table("users", "id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, contact TEXT, username TEXT, password TEXT")
        self.create_table("expenses", "id INTEGER PRIMARY KEY AUTOINCREMENT, hoa TEXT, amount REAL, date TEXT, payment_type TEXT, recipient_name TEXT, comment TEXT DEFAULT 'No Comment'")
        self.create_table("expense_types", "id INTEGER PRIMARY KEY AUTOINCREMENT, head_of_account TEXT")
        self.create_table("classes", "id INTEGER PRIMARY KEY AUTOINCREMENT, class_name TEXT")
        self.create_table("subjects", "id INTEGER PRIMARY KEY AUTOINCREMENT, subject_name TEXT,passing_mark INTEGER,total_mark INTEGER,class_id INTEGER, FOREIGN KEY(class_id) REFERENCES classes(id)")
        self.create_table("students", "id INTEGER PRIMARY KEY AUTOINCREMENT, addmission_date TEXT,addmission_no TEXT,name TEXT,f_name TEXT,dob TEXT,address TEXT,contact TEXT,gender TEXT,section TEXT,last_school TEXT DEFAULT '',student_image TEXT, special_case TEXT DEFAULT '',class_id INTEGER, FOREIGN KEY(class_id) REFERENCES classes(id)")

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


    