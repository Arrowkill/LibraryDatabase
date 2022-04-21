import mysql.connector
from mysql.connector import Error


'''
Developed by Jackson Johanek for UNT CSCE 4350

START FUNCTION DECLARATIONS

START OF UI FUNCTIONS
'''


# ADMIN INTERFACE
def admin_interface(a_user, a_pass):
    while True:
        # ADMIN Use Cases
        print("Would you like to:\n"
              "1.CHECK IN ITEM\n"
              "2.CHECK OUT ITEM\n"
              "3.CHECK AVAILABILITY\n"
              "4.CHECK ACCOUNT\n"
              "5.EDIT DATABASE\n"
              "Exit: Exit the program")
        user_choice = input()

        # Switch-Case If/ElIf block
        if user_choice == "Exit":
            print("Exiting..")
            break
        elif user_choice == "1":
            check_in()
        elif user_choice == "2":
            check_out()
        elif user_choice == "3":
            check_avail()
        elif user_choice == "4":
            check_acct_amd()
        elif user_choice == "5":
            edit_db()
        else:
            print("Unrecognized Command")


# USER INTERFACE
def user_interface(g_user, g_pass):
    while True:
        print("Would you like to:\n"
              "1.CHECK AVAILABILITY\n"
              "2.CHECK ACCOUNT\n"
              "Exit. Exit the program")
        user_choice = input()

        # Switch-Case If/ElIf block
        if user_choice == "Exit":
            print("Exiting..")
            break
        elif user_choice == "1":
            check_avail()
        elif user_choice == "2":
            check_acct()
        else:
            print("Unrecognized Command")


def is_admin():
    # TODO: IF USERNAME & PASS IS AN ADMIN USER/PASS
    print("is_admin")
    return True


'''
END OF UI FUNCTIONS

START OF DATABASE INVOLVED FUNCTIONS
'''


# Print whole table of given cursor
def print_table(given_cursor):
    result = given_cursor.fetchall()
    for row in result:
        print(row)


def check_in():
    # TODO: GET USER INFO
    # TODO: GET TURNED IN ITEM(s) INFO
    # TODO: CHANGE STATUS OF ITEM(s) TO "CHECKED_IN"


def check_out():
    # TODO: GET USER INFO
    # TODO: GET ITEM INFO
    # TODO: CHANGE STATUS OF ITEM(s) TO "CHECKED_OUT"


def check_avail():
    # TODO: ASK WHICH TYPE OF ITEM
    # TODO: PRINT REQUESTED ITEM(s)


def edit_db():
    # TODO: ADD ITEM
    # TODO: DELETE ITEM
    # TODO: EDIT ITEM


def check_acct_adm():
    # TODO: GET USER INFO
    # TODO OPTION: edit user info
    # TODO: CALL check_acct()


def check_acct():
    # TODO: PRINT CHECKED OUT ITEMS
    # TODO: PRINT OVERDUE


'''
END OF DATABASE INVOLVED FUNCTIONS

END OF FUNCTION DECLARATIONS

BODY CODE "Main.py"
'''

try:
    # EDIT BELOW INFORMATION FOR CONNECTING TO DIFFERENT DATABASE/USER/PASSWORD
    connection = mysql.connector.connect(host='localhost',
                                         database='newschema',
                                         user='root',
                                         password='thisisalongpasswordforaspecificreason')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.close()

# Error Exception for SQL database connection
except Error as e:
    print("except")
    print("Error while connecting to MySQL", e)

# Connection success
else:
    cursor = connection.cursor()
    Admin = False

    # GET USER CREDENTIALS
    print("Please input your username, if you have no account, leave blank")
    user_name = input()
    user_pass = ""
    if user_name == "":
        # TODO: ANON USER
        print("Anon User")
    else:
        print("Please input your password")
        user_pass = input()

    if is_admin():
        Admin = True
    # END OF GET USER CREDENTIALS

    # ADMIN USER/LIBRARY STAFF
    if Admin:
        admin_interface(user_name, user_pass)
    # GENERIC USER
    else:
        user_interface(user_name, user_pass)
    # END OF ALL USER CASES

    if connection.is_connected():
        connection.close()
    print("Connection Closed")
