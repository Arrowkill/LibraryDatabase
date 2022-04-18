import mysql.connector
from mysql.connector import Error


# FUNCTION DECLARATIONS
# Print whole table of given cursor
def print_table(given_cursor):
    result = given_cursor.fetchall()
    for row in result:
        print(row)


# Body of Code
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

    # TODO: IF USERNAME & PASS IS AN ADMIN USER/PASS
    # Admin = True
    # END OF GET USER CREDENTIALS

    # TODO: EXTRACT ADMIN/GENERIC USER CASES TO A SEPARATE FUNCTION
    # ADMIN USER/LIBRARY STAFF
    while Admin == True:
        # ADMIN Use Cases
        print("Would you like to:\n"
              "1.CHECK IN ITEM\n"
              "2.CHECK OUT ITEM\n"
              "3.CHECK AVAILABILITY\n"
              "4.CHECK ACCOUNT\n"
              "4.EDIT DATABASE\n"
              "Exit: Exit the program")
        user_choice = input()

        # Switch-Case If/ElIf block

        if user_choice == "Exit":
            print("Exiting..")
            break
        else:
            print("Unrecognized Command")

    # GENERIC USER CASE
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

    # END OF ALL USER CASES
    if connection.is_connected():
        connection.close()
    print("Connection Closed")
