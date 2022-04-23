import mysql.connector
from mysql.connector import Error

'''
Developed by Jackson Johanek for UNT CSCE 4350

START FUNCTION DECLARATIONS

START OF SQL-BASED FUNCTIONS
'''


# io = In/Out
# table_type = Type of Item
# item_id = ID of Item
def check_in_out(io, table_type, item_id):
    print("Checking In/Out Item: ", item_id)
    modify_stmt = ("UPDATE %s"
                   "SET [io_status] = %s"
                   "WHERE [item_id] = %s")
    # UPDATE table_type
    # SET [io_status] = io
    # WHERE [item_id] = item_id
    data = (table_type, io, item_id)

    try:
        cursor.execute(modify_stmt, data)
        connection.commit()
    except Error as modify_err:
        print(modify_err, "\nRolling Back")
        connection.rollback()
    else:
        if io == "In":
            print("Item checked in")
        else:
            print("Item checked out")


'''
END OF SQL-BASED FUNCTIONS

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
              "6.DELETE ACCOUNT\n"
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
            check_acct_adm()
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
            check_acct(g_user, g_pass)
        else:
            print("Unrecognized Command")


# ANON USER INTERFACE
def anon_user_interface():
    while True:
        print("Would you like to:\n"
              "1.CHECK AVAILABILITY\n"
              "2.CREATE ACCOUNT\n"
              "Exit. Exit the program")
        user_choice = input()

        # Switch-Case If/ElIf block
        if user_choice == "Exit":
            print("Exiting..")
            break
        elif user_choice == "1":
            check_avail()
        elif user_choice == "2":
            create_acct()
        else:
            print("Unrecognized Command")


def is_admin(uname, upass):
    # TODO: Test if user is in Admin db
    print("is_admin")
    return True


def is_user(uname, upass):
    # TODO: Test if user is in db
    print("is_user")
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


'''
CHECK IN FUNCTIONS
'''


def check_in():
    u_name = ""
    u_pass = ""
    while not is_user(u_name, u_pass):
        print("Input Patron Username:")
        u_name = input()
        print("Input Patron Password:")
        u_pass = input()

    done = False
    c_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while not done:
        print("What type of Content is being turned in:\n"
              "1.Books\n"
              "2.Magazines\n"
              "3.DVDs\n"
              "4.CDs\n"
              "5.VHS Tapes\n"
              "6.Reference Material\n"
              "7.Instrument\n"
              "8.Console\n"
              "9.Study Room\n"
              "Done.Finished with checking out")
        c_type = input()  # Content Type
        if c_type == "Done":
            done = True
        else:
            print("Provide Content ID:")
            c_id = input()  # Content ID

            if c_type in c_list:
                check_in_out("IN", u_name, c_id)
            else:
                print("Unrecognized Command")


'''
END OF CHECK IN FUNCTIONS
CHECK OUT FUNCTIONS
'''


def check_out():
    u_name = ""
    u_pass = ""
    while not is_user(u_name, u_pass):
        print("Input Patron Username:")
        u_name = input()
        print("Input Patron Password:")
        u_pass = input()

    done = False
    c_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    while not done:
        print("What type of Content is being checked out:\n"
              "1.Books\n"
              "2.Magazines\n"
              "3.DVDs\n"
              "4.CDs\n"
              "5.VHS Tapes\n"
              "6.Reference Material\n"
              "7.Instrument\n"
              "8.Console\n"
              "9.Study Room\n"
              "Done.Finished with checking out")
        c_type = input()  # Content Type
        if c_type == "Done":
            done = True
        else:
            print("Provide Content ID:")
            c_id = input()  # Content ID

            if c_type in c_list:
                check_in_out("OUT", u_name, c_id)
            else:
                print("Unrecognized Command")


'''
END OF CHECK OUT FUNCTIONS
CHECK AVAILABILITY
'''


def check_avail():
    done = False
    content_type_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while not done:
        print("What type of Content would you like to see availability for:\n"
              "1.Books\n"
              "2.Magazines\n"
              "3.DVDs\n"
              "4.CDs\n"
              "5.VHS Tapes\n"
              "6.Reference Material\n"
              "7.Instrument\n"
              "8.Console\n"
              "9.Study Room\n"
              "Done.Finished with checking availability")
        c_type = input()  # Content Type
        if c_type == "Done":
            done = True
        else:
            if c_type in content_type_list:
                print_availability(c_type)
            else:
                print("Unrecognized Command")


def print_availability(c_type):
    print("Availability Requested:", c_type)
    print_stmt = ("SELECT [] "
                  "FROM %s ")
    # SELECT [status]
    # FROM table_type
    data = (c_type,)
    try:
        cursor.execute(print_stmt, data)
        result = cursor.fetchall()
        for x in result:
            print(x)
    except Error as print_err:
        print(print_err, "\nPrinting Error")


'''
END OF CHECK AVAILABILITY
EDIT DATABASE
'''


def edit_db():
    selected = False
    done = False
    selection_list = ["1", "2", "3"]
    content_type_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    selection = ""
    c_type = ""

    while not selected:
        print("What would you like to do?\n"
              "1.Add Item\n"
              "2.Delete Item\n"
              "3.Edit Item")
        selection = input()  # Edit Type
        if selection in selection_list:
            selected = True
        else:
            print("Unrecognized Command")

    while not done:
        print("What type of Content would you like to edit:\n"
              "1.Books\n"
              "2.Magazines\n"
              "3.DVDs\n"
              "4.CDs\n"
              "5.VHS Tapes\n"
              "6.Reference Material\n"
              "7.Instrument\n"
              "8.Console\n"
              "9.Study Room\n"
              "Done.Finished with checking availability")
        c_type = input()  # Content Type
        if c_type == "Done":
            done = True
        else:
            if c_type in content_type_list:
                if selection == "1":
                    add_item(c_type)
                elif selection == "2":
                    delete_item(c_type)
                elif selection == "3":
                    edit_item(c_type)
            else:
                print("Unrecognized Command")


def add_item(content_type):
    print("add")
    # TODO: ADD CONTENT


def delete_item(content_type):
    print("delete")
    # TODO: DELETE CONTENT


def edit_item(content_type):
    print("edit")
    # TODO: EDIT CONTENT


'''
END OF EDIT DATABASE
CHECK ACCOUNT
'''


def check_acct_adm():
    u_name = ""
    u_pass = ""
    while not is_user(u_name, u_pass):
        print("Input Patron Username:")
        u_name = input()
        print("Input Patron Password:")
        u_pass = input()
    # TODO OPTION: edit user info
    check_acct(u_name, u_pass)


def check_acct(u_name, u_pass):
    print("Print user info")
    # TODO: PRINT CHECKED OUT ITEMS
    # TODO: PRINT OVERDUE


'''
END OF CHECK ACCOUNT
CREATE ACCOUNT
'''


def create_acct():
    print("Add_User")
    # TODO: GET USER INFO
    # TODO: UPDATE USER LIST TO INCLUDE NEW ACCOUNT


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
    Anon = False

    # GET USER CREDENTIALS
    print("Please input your username, if you have no account, leave blank")
    user_name = input()
    user_pass = ""
    if user_name == "":
        Anon = True
    else:
        print("Please input your password")
        user_pass = input()

    if is_admin(user_name, user_pass):
        Admin = True
        User = True
    elif is_user(user_name, user_pass):
        User = True
    # END OF GET USER CREDENTIALS

    # ADMIN USER/LIBRARY STAFF
    if Admin:
        admin_interface(user_name, user_pass)
    # GENERIC USER
    elif not Anon:
        user_interface(user_name, user_pass)
    else:
        anon_user_interface()
    # END OF ALL USER CASES

    if connection.is_connected():
        connection.close()
        print("Connection Closed")
    print("Goodbye")
