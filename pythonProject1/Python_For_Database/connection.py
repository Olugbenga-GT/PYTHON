# First, import the mySql connector

import mysql.connector

# import the error module from my sql connector
from mysql.connector import Error

# Define the connection function
def connect_and_fetch():
    '''Function to connect and fetch rows in a database'''
    conn = None

    try:
        conn = mysql.connector.connect(host = 'localhost',
                                       #Using the capecodd database
                                       database = 'gastt',
                                       user = 'Gastt',
                                       password = 'Gast2020'
                                       )
        print('connected to the database')
        db_cursor = conn.cursor()
        sql_select(db_cursor)

        #create a varaiable to hold your sql query
        # HumanID, NAME, GENDER , BLOOD GROUP AGE
        sql = "INSERT INTO Human(name, gender, bloodgroup, age) VALUES (%s %s %s)"
        val = [
            ("Hannah", "Female", "B-"),
            ("Richard", "Male", "O+"),
            ("Sandy", "Female", "B+"),
            ("Micheal", "male", "O-"),
            ("Green", "Male", "B-")
        ]

        # Executing many queries
        db_cursor.executemany(sql, val)

        # commit to database
        conn.commit

        print(db_cursor.rowcount, "rows was inserted")
        db_cursor.close()

    except Error as e:
        print("Not connecting due to", e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Database shutdown")

def sql_select(db_cursor):
    sql_select_query = "select * from Human"
    db_cursor.execute(sql_select_query)
    records = db_cursor.fetchall()

    # Print selected output
    print("\n Printing each buyer record")
    for rows in records:
        print("Buyer name:",rows[0])
        print("Department:",rows[0])
        print("Position:",rows[0])
        print("Supervisor:",rows[0])
        print()

connect_and_fetch()