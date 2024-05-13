import mysql.connector
import sys
from mysql.connector import Error
class DBHelper:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="practice"
            )
            self.mycursor = self.conn.cursor()
            print("Connected to MySQL database!")
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
        else:
            print("you are done")

    def register(self, name, email, password):
        try:
            sql = "INSERT INTO login (UserName, Email, Password) VALUES (%s, %s, %s)"
            values = (name, email, password)
            self.mycursor.execute(sql, values)
            self.conn.commit()
            return 1
        except Error as e:
            print(f"Error registering user: {e}")
            return -1

    def search(self, email, password):
        try:
            sql = "SELECT * FROM login WHERE Email = %s AND Password = %s"
            self.mycursor.execute(sql, (email, password))
            data = self.mycursor.fetchall()

            return data
        except Error as e:
            print(f"Error searching user: {e}")
            return -1




