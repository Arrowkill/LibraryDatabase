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
    if table_type == "1":
        table_type = "Books"
        db_id = "BookID"
    elif table_type == "2":
        table_type = "Magazines"
        db_id = "MagazineID"
    elif table_type == "3":
        table_type = "DVD"
        db_id = "DVDID"
    elif table_type == "4":
        table_type = "CD"
        db_id = "CDID"
    elif table_type == "5":
        table_type = "VHS_Tapes"
        db_id = "VHSID"
    elif table_type == "6":
        table_type = "Reference_Material"
        db_id = "ReferenceID"
    elif table_type == "7":
        table_type = "Instruments"
        db_id = "InstrumentID"
    elif table_type == "8":
        table_type = "Consoles"
        db_id = "ConsoleID"
    elif table_type == "9":
        table_type = "Study_Rooms"
        db_id = "RoomID"
    else:
        print("Error 4")
        db_id = ""
        exit(4)

    modify_stmt = ("UPDATE %s "
                   "SET IsOut = %s "
                   "WHERE %s = %s")
    # UPDATE table_type
    # SET IsOut = io(type-casted bool)
    # WHERE db_id = item_id
    if io == "IN":
        data = (table_type, "1", db_id, item_id)
    else:
        data = (table_type, "0", db_id, item_id)

    try:
        cursor.execute(modify_stmt, data)
        connection.commit()
    except Error as modify_err:
        print(modify_err, "\nRolling Back")
        connection.rollback()
    else:
        if io == "IN":
            print("Item checked in")
        else:
            print("Item checked out")


'''
END OF SQL-BASED FUNCTIONS

START OF UI FUNCTIONS
'''


# ADMIN INTERFACE
def admin_interface():
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
    scan_stmt = ("SELECT Library_Staff(StaffID) "
                 "FROM Library_Staff "
                 "WHERE EmployeeFirstName = %s "
                 "AND StaffID = %s")
    # SELECT Library_Staff(StaffID)
    # FROM Library_Staff
    # WHERE EmployeeFirstName = uname
    # AND StaffID = upass
    data = (uname, upass)
    try:
        result = cursor.execute(scan_stmt, data)
        if result == upass:
            return True
        else:
            return False
    except Error as scan_err:
        print(scan_err, "\nUnable to Scan admin_table")


def is_user(uname, upass):
    scan_stmt = ("SELECT Patron(PatronID) "
                 "FROM Patron "
                 "WHERE FirstName = %s "
                 "AND PatronID = %s")
    # SELECT Patron(PatronID)
    # FROM Patron
    # WHERE FirstName = uname
    # AND PatronID = upass
    data = (uname, upass)
    try:
        result = cursor.execute(scan_stmt, data)
        if result == upass:
            return True
        else:
            return False
    except Error as scan_err:
        print(scan_err, "\nUnable to Scan user_table")


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
    if c_type == "1":
        c_type = "Books"
        gather_this = "Books(Title, Author, Genre, ISBN)"
    elif c_type == "2":
        c_type = "Magazines"
        gather_this = "Magazines(Title, Author, Genre, ISSN)"
    elif c_type == "3":
        c_type = "DVD"
        gather_this = "DVD(Title, Studio, Genre)"
    elif c_type == "4":
        c_type = "CD"
        gather_this = "CD(Title, Author, Genre)"
    elif c_type == "5":
        c_type = "VHS_Tapes"
        gather_this = "VHS_Tapes(Title, Studio, Genre)"
    elif c_type == "6":
        c_type = "Reference_Material"
        gather_this = "Reference_Material(Title, Author)"
    elif c_type == "7":
        c_type = "Instruments"
        gather_this = "Instruments(Instrument, InstrumentCondition, Accessories)"
    elif c_type == "8":
        c_type = "Consoles"
        gather_this = "Consoles(ConsoleID, ConsoleDescription)"
    elif c_type == "9":
        c_type = "Study_Rooms"
        gather_this = "Study_Rooms(RoomID, TimeSlot, RoomNumber)"
    else:
        gather_this = ""
        print("Error 5")
        exit(5)
    print("Availability Requested:", c_type)
    print_stmt = ("SELECT %s "
                  "FROM %s "
                  "WHERE IsOut = 1")
    # SELECT gather_this
    # FROM table_type
    # WHERE IsOut = 1
    data = (gather_this, c_type)
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
    # c_type

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


def add_item(table_type):
    if table_type == "1":
        insert_stmt = ("INSERT INTO Books(Title, Author, Genre, ISBN, IsOut, RentalPeriod, BookID) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        print("Please input the following information:\n"
              "Title:")
        b_title = input()
        print("Author:")
        b_author = input()
        print("Genre:")
        b_genre = input()
        print("ISBN:")
        b_isbn = input()
        print("Is the content in stock?:")
        is_out = input()
        print("RentalPeriod:")
        rental_period = input()
        print("BookID")
        b_id = input()
        data = (b_title, b_author, b_genre, b_isbn, is_out, rental_period, b_id)
        try:
            cursor.execute(insert_stmt, data)
        except Error as add_err:
            print(add_err, "\nUnable to add Book")
        else:
            print("Book added successfully")

    elif table_type == "2":
        insert_stmt = ("INSERT INTO Magazines(Title,Author,Genre,ISSN,IsOut,RentalPeriod,MagazineID)"
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        print("Please input the following information:\n"
              "Title:")
        m_title = input()
        print("Author:")
        m_author = input()
        print("Genre:")
        m_genre = input()
        print("ISBN:")
        m_isbn = input()
        print("Is the content in stock?:")
        is_out = input()
        print("RentalPeriod:")
        rental_period = input()
        print("BookID")
        m_id = input()
        data = (m_title, m_author, m_genre, m_isbn, is_out, rental_period, m_id)
        try:
            cursor.execute(insert_stmt, data)
        except Error as add_err:
            print(add_err, "\nUnable to add Magazine")
        else:
            print("Magazine added successfully")

    elif table_type == "3":
        insert_stmt = ("INSERT INTO DVD(Title,Studio,Genre,IsOut,RentalPeriod,DVDID)"
                       "VALUES (%s, %s, %s, %s, %s, %s)")
        print("Please input the following information:\n"
              "Title:")
        d_title = input()
        print("Author:")
        d_studio = input()
        print("Genre:")
        d_genre = input()
        print("Is the content in stock?:")
        is_out = input()
        print("RentalPeriod:")
        rental_period = input()
        print("BookID")
        d_id = input()
        data = (d_title, d_studio, d_genre, is_out, rental_period, d_id)
        try:
            cursor.execute(insert_stmt, data)
        except Error as add_err:
            print(add_err, "\nUnable to add DVD")
        else:
            print("DVD added successfully")

    elif table_type == "4":
        insert_stmt = ("INSERT INTO CD(Title,Author,Genre,IsOut,RentalPeriod,CDID)"
                       "VALUES (%s, %s, %s, %s, %s, %s)")
        print("Please input the following information:\n"
              "Title:")
        c_title = input()
        print("Author:")
        c_author = input()
        print("Genre:")
        c_genre = input()
        print("Is the content in stock?:")
        is_out = input()
        print("RentalPeriod:")
        rental_period = input()
        print("BookID")
        c_id = input()
        data = (c_title, c_author, c_genre, is_out, rental_period, c_id)
        try:
            cursor.execute(insert_stmt, data)
        except Error as add_err:
            print(add_err, "\nUnable to add CD")
        else:
            print("CD added successfully")

    elif table_type == "5":
        insert_stmt = ("INSERT INTO VHS_Tapes(Title,Studio,Genre,IsOut,RentalPeriod,VHSID)"
                       "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        print("Please input the following information:\n"
              "Title:")
        v_title = input()
        print("Author:")
        v_studio = input()
        print("Genre:")
        v_genre = input()
        print("Is the content in stock?:")
        is_out = input()
        print("RentalPeriod:")
        rental_period = input()
        print("BookID")
        v_id = input()
        data = (v_title, v_studio, v_genre, is_out, rental_period, v_id)
        try:
            cursor.execute(insert_stmt, data)
        except Error as add_err:
            print(add_err, "\nUnable to add VHS")
        else:
            print("VHS added successfully")

    elif table_type == "6":
        insert_stmt = ("INSERT INTO Reference_Material(Title,Author,IsOut,RentalPeriod,ReferenceID)"
                       "VALUES (%s, %s, %s, %s, %s)")
        print("Please input the following information:\n"
              "Title:")
        r_title = input()
        print("Author:")
        r_author = input()
        print("Is the content in stock?:")
        is_out = input()
        print("RentalPeriod:")
        rental_period = input()
        print("BookID")
        r_id = input()
        data = (r_title, r_author, is_out, rental_period, r_id)
        try:
            cursor.execute(insert_stmt, data)
        except Error as add_err:
            print(add_err, "\nUnable to add Reference Material")
        else:
            print("Reference Material added successfully")

    elif table_type == "7":
        insert_stmt = ("INSERT INTO Instruments(InstrumentID, Instrument, InstrumentCondition, Accessories, IsOut)"
                       "VALUES (%s, %s, %s, %s, %s)")
        print("Please input the following information:\n"
              "InstrumentID:")
        i_id = input()
        print("Instrument:")
        i_name = input()
        print("InstrumentCondition:")
        i_cond = input()
        print("Accessories:")
        i_acc = input()
        print("Is the content in stock?:")
        is_out = input()
        data = (i_id, i_name, i_cond, i_acc, is_out)
        try:
            cursor.execute(insert_stmt, data)
        except Error as add_err:
            print(add_err, "\nUnable to add Instrument")
        else:
            print("Instrument added successfully")

    elif table_type == "8":
        insert_stmt = ("INSERT INTO Consoles(ConsoleID, ConsoleDescription, IsOut, TimeSlot)"
                       "VALUES (%s, %s, %s, %s)")
        print("Please input the following information:\n"
              "ConsoleID:")
        c_id = input()
        print("Console Description:")
        c_desc = input()
        print("Is the content in stock?:")
        is_out = input()
        print("Time Slot:")
        c_time_slot = input()
        data = (c_id, c_desc, is_out, c_time_slot)
        try:
            cursor.execute(insert_stmt, data)
        except Error as add_err:
            print(add_err, "\nUnable to add Console")
        else:
            print("Console added successfully")

    elif table_type == "9":
        insert_stmt = ("INSERT INTO Study_Rooms(RoomID, TimeSlot, RoomNumber, IsOut)"
                       "VALUES (%s, %s, %s, %s)")
        print("Please input the following information:\n"
              "RoomID:")
        r_id = input()
        print("Time Slot:")
        time_slot = input()
        print("Room Number:")
        room_numb = input()
        print("Is the content in stock?:")
        is_out = input()
        data = (r_id, time_slot, room_numb, is_out)
        try:
            cursor.execute(insert_stmt, data)
        except Error as add_err:
            print(add_err, "\nUnable to add Room")
        else:
            print("Room added successfully")

    else:
        print("Error 5")
        db_id = ""
        exit(5)


def delete_item(table_type):
    print("Please supply the content ID")
    c_id = input()

    if table_type == "1":
        table_type = "Books"
        db_id = "BookID"
    elif table_type == "2":
        table_type = "Magazines"
        db_id = "MagazineID"
    elif table_type == "3":
        table_type = "DVD"
        db_id = "DVDID"
    elif table_type == "4":
        table_type = "CD"
        db_id = "CDID"
    elif table_type == "5":
        table_type = "VHS_Tapes"
        db_id = "VHSID"
    elif table_type == "6":
        table_type = "Reference_Material"
        db_id = "ReferenceID"
    elif table_type == "7":
        table_type = "Instruments"
        db_id = "InstrumentID"
    elif table_type == "8":
        table_type = "Consoles"
        db_id = "ConsoleID"
    elif table_type == "9":
        table_type = "Study_Rooms"
        db_id = "RoomID"
    else:
        print("Error 6")
        db_id = ""
        exit(6)

    delete_stmt = ("DELETE FROM %s "
                   "WHERE %s = %s")
    data = (table_type, db_id, c_id)
    
    try:
        cursor.execute(delete_stmt, data)
        connection.commit()
    except Error as delete_err:
        print(delete_err, "Rolling Back")
        connection.rollback()
    else:
        print("Deletion Successful")


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
        print("Input Patron First Name:")
        u_name = input()
        print("Input PatronID:")
        u_pass = input()
    # TODO OPTION: edit user info
    check_acct(u_name, u_pass)


def check_acct(u_name, u_pass):
    print("Print user info")
    check_stmt = ("SELECT Patron_Account(AccountID, AccountPassword, PastDueItems, CheckedOutItems, Fees) "
                  "FROM Patron_Account "
                  "WHERE Patron(FirstName) = %s "
                  "AND Patron(PatronID) = %s")
    data = (u_name, u_pass)
    try:
        cursor.execute(check_stmt, data)
        print_table(cursor)
    except Error as check_err:
        print(check_err, "\nUnable to Scan user_table")


'''
END OF CHECK ACCOUNT
CREATE ACCOUNT
'''


def create_acct():
    print("Please input the following information when prompted.\n"
          "First Name:")
    first_name = input()
    print("Last Name:")
    last_name = input()
    print("Date Of Birth, formatted YYYY-MM-DD:")
    date_of_birth = input()
    print("Email address, including domain, i.e. @gmail.com, @yahoo.com:")
    email_address = input()
    print("Your Physical Home Address")
    home_address = input()
    print("Your Phone Number formatted as all digits:")
    phone_number = input()
    print("A password for your account:")
    patron_password = input()
    try:
        cursor.execute("SELECT count(*) FROM Patron")
    except Error as count_err:
        print(count_err, "Unable to determine patron ID")
    else:
        result = cursor.fetchall()
        patron_id = result + 1

    print("Your Patron ID is:{0}Please keep this information safe.".format(patron_id))

    insert_stmt = ("INSERT INTO Patron(FirstName, LastName, DateOfBirth, Email, Address, PatronID, PhoneNumber) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s )")
    data = (first_name, last_name, date_of_birth, email_address, home_address, patron_id, phone_number)

    insert_acct_stmt = ("INSERT INTO Patron_Account(AccountID, AccountPassword, PastDueItems, CheckedOutItems, Fees) "
                        "VALUES (%s, %s, %s, %s, %s)")
    acct_data = (patron_id, patron_password, 0, 0, 0)

    try:
        cursor.execute(insert_stmt, data)
        cursor.execute(insert_acct_stmt, acct_data)
        connection.commit()
    except Error as insert_err:
        print(insert_err, "Rolling back")
        connection.rollback()
    else:
        print("Added new account")


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
    Anon = True

    # GET USER CREDENTIALS
    print("Please input your First Name, if you have no account, leave blank")
    user_name = input()
    user_pass = ""
    if user_name == "":
        print("Anonymous User")
    else:
        print("Please input your account ID")
        user_pass = input()

    if is_admin(user_name, user_pass):
        Admin = True
    elif is_user(user_name, user_pass):
        Anon = False
    # END OF GET USER CREDENTIALS

    # ADMIN USER/LIBRARY STAFF
    if Admin:
        admin_interface()
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
