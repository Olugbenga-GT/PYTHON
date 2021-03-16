import  mysql.connector

myConnection = mysql.connector.connect(
    host = 'localhost',
    user = 'Gastt',
    password = 'Gast2020',
    database = 'Fuse'
)

myCursor = myConnection.cursor()
myCursor.execute("CREATE Database Fuse")
myCursor.execute("Show Databases")
for database in myCursor:
        print(database)

myCursor.execute("CREATE TABLE Departments(DeptID integer  not null auto_increment, \n "
                 " DeptCount integer not null, hod varchar (50), \n"
                 " CONSTRAINT Dept_pk PRIMARY KEY(DeptID))")

myCursor.execute("Show Tables")
for table in myCursor:
    print (table)

myCursor.execute("ALTER TABLE Departments ADD Remarks varchar(230) \n "
                 " default ('Please, leave a remark')")
myConnection.commit()
for column in myCursor:
    print (column)
myCursor.execute("SELECT * FROM Departments")
for column in myCursor:
    print(column)


myCursor.execute("ALTER TABLE Departments DROP DeptCount")
myConnection.commit()

sql = "INSERT INTO Departments(hod, remarks, Dept_Name) VALUES (%s, %s, %s)"

val = [("Paslann","For God", "Event Planning"),
        ("Finesse","For God", "Data Analytics"),
        ("Michael","For God", "Choir"),
        ("Lalasky","For God", "Welfare"),
        ("Fola","For God", "Finance"),
        ("Sarah","For God", "Adminsitration"),
        ("Jimmy","For God", "Logistics")]

myCursor.executemany(sql, val)
myConnection.commit()
print(myCursor.rowcount, "records added")
myConnection.close()

myCursor.execute("ALTER TABLE Departments ADD DeptID INT AUTO_INCREMENT PRIMARY KEY")
myConnection.commit()

myCursor.execute("SELECT Dept_Name  \n"
                 "FROM Departments \n"
                 "WHERE hod like '%an%'")
myResult = myCursor.fetchall()

for column in myResult:
    print((column))

# Avoiding SQL Injections
# query1: "select column from table where condition = %s"
# cond: hidden condition

myCursor.execute(query1, cond)

sql = "Delete from Departments where DeptID = 1 "
myCursor.execute(sql)
myConnection.commit()
print(myCursor.rowcount, "record(s) deleted")

sql = "Update Departments Set hod = 'Gastt' where Dept_Name = 'Data Analytics'"
myCursor.execute(sql)
myConnection.commit()
print(myCursor.rowcount, "rows affected")

myCursor.execute("Select * from Departments limit 5 offset 2")
myResult = myCursor.fetchall()
for row in myResult:
    print(row)