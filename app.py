import sys
from dbhelper import DBHelper
class Logform:
    def __init__(self):
        self.db=DBHelper()
        self.menu()

    def menu(self):
        user_input=input("""
        1. Enter 1  to register
        2. Enter 2  to login
        3. Anything else to leave
        """
       )

        if user_input=='1':
            self.register()
        elif user_input =='2':
            self.login()
        else:
            sys.exit(1000)

    def register(self):
        name=input("Enter the Name")
        email = input("Enter the Email")
        password = input("Enter the Password")
        response=self.db.register(name,email,password)
        if response:
            print("registration is succesfull")
            self.menu()
        else:
            print("registration failed")

    def login(self):
        email=input("Enter the email")
        password=input("Enter the password")
        data=self.db.search(email,password)
        if data==0:
            print("error on login")
            self.login()
        else:
            print("Hello",data[0][1])
obj=Logform()

