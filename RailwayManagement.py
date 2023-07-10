import mysql.connector as a
password = str(input("Enter Database Password - "))
con = a.connect(host="localhost", user = "root", password = password)

# Selecting Database if it exists - 
c = con.cursor()
c.execute("Show Databases")
dl = c.fetchall()
dl2 = []

# Adding all the existing databases name into the list - 
for i in dl:
    dl2.append(i[0])

print(dl2)

# If 'MyRailway' database exists, we will use it or else create a new database -
if 'myrailway' in dl2:
    sql = 'Use myrailway'
    c.execute(sql)
else:
    try:
        sql1 = "CREATE DATABASE MyRailway"
        c.execute(sql1)
        print("Database created successfully!")
    except a.Error as e:
        print(f"Error creating database: {e}")
    
    sql2 = "Use MyRailway"
    c.execute(sql2)

    sql3 = "Create table Train(Name varchar(50), Cost integer, Distance integer, Date varchar(20))"
    c.execute(sql3)

    sql4 = "Create table Customer(Name varchar(30), Train varchar(25), Payment integer, Date varchar(20), PhoneNo varchar(20))"
    c.execute(sql4)

    # sql5 = "Create table Bills(Detail varchar(20), Cost integer, Date varchar(20))"
    # c.execute(sql5)
    
    sql6 = "Create table Worker(Name varchar(100), Work varchar(20), Salary varchar(20))"
    c.execute(sql6)

    con.commit()

# Setting System Login and Password - 
def SignIn():
    sysPass = str(input("\nEnter System Password - "))

    if sysPass == "Hello_001":
        print("---->>>> Welcome to Railconnect App <<<<----")
        Options()
    else:
        SignIn()

def Options():
    print('''\n1. Add Train
2. Book Train
3. Add Worker
4. Display Trains
5. Display Payments
6. Display Workers
7. Logout''')
    
    loggedin = True
    while loggedin:
        choice = int(input("\nChoose the option you wish to execute - "))
        if choice == 1: AddTrain()
        elif choice == 2: BookTrain()
        elif choice == 3: AddWorker()
        elif choice == 4: DisplayTrain()
        elif choice == 5: DisplayPayment()
        elif choice == 6: DisplayWorker()
        elif choice == 7: loggedin = False

        else:
            print("Incorrect Option!! Choose again.")

def AddTrain():
    tName = str(input("Train Name - "))
    tCost = int(input("Ticket Cost (INR) - "))
    tDistance = int(input("Travel Distance (in Km.)- "))
    tDate = str(input("Date - "))
    data = (tName, tCost, tDistance, tDate)

    sql = "insert into Train values(%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Inserted Successfully!!")
    Options()

def BookTrain():
    cusName = str(input("Customer Name - "))
    cusTrain = str(input("Train - "))
    cusPay = int(input("Payment (INR) - "))
    date = str(input("Date - "))
    phone = str(input("Contact Number - "))
    data = (cusName, cusTrain, cusPay, date, phone)
    sql = "insert into Customer values(%s,%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Inserted Successfully!!")
    Options()

def AddWorker():
    worName = str(input("Worker Name - "))
    worWork = str(input("Work - "))
    worSalary = int(input("Salary (INR) - "))
    data = (worName, worWork, worSalary)
    sql = "insert into Worker values(%s,%s,%s)" 
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Inserted Successfully!!")
    Options()

def DisplayTrain():
    sql = "select * from Train"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(f'Train Name - {i[0]}')
        print(f'Ticket Cost - {i[1]}')
        print(f'Travel Distance - {i[2]}')
        print(f'Date - {i[3]}')
        print('---------- x x x x ----------')
    Options()

def DisplayPayment():
    disDate = input("Date : ")
    sql = "select * from Customer"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        if i[3] == disDate:
            print(f'Name - {i[0]}')
            print(f'Train - {i[1]}')
            print(f'Payment - {i[2]}')
            print(f'Date - {i[3]}')
            print(f'Phone - {i[4]}')
            print('---------- x x x x ----------')
    Options()

def DisplayWorker():
    sql = "select * from Worker"
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print(f'Worker Name - {i[0]}')
        print(f'Work - {i[1]}')
        print(f'Salary - {i[2]}')
        print('---------- x x x x ----------')
    Options()


# Main Function - 
SignIn()