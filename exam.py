import mysql.connector as c

# user insert the data in database with help of insert method
def insert():
    con = c.connect(host="localhost", user="root", passwd="*******", database="exam")
    cursor = con.cursor()
    name = input("Enter the name: ")
    passs = input("Enter the password: ")
    query = "INSERT INTO st (name, passs) VALUES (%s, %s)"
    cursor.execute(query, (name, passs))
    con.commit()
    print("Data inserted successfully")

#user login with id  and password and Users take quiz and view scores with help og login method
def login():
    con = c.connect(host="localhost", user="root", passwd="*********", database="exam")
    cursor = con.cursor()
    name = input("Enter name: ")
    passs = input("Enter password: ")
    sql = "SELECT * FROM st WHERE name = %s AND passs = %s"
    cursor.execute(sql, (name, passs))
    result = cursor.fetchall()
    if result:
        print("Logged in Successfully!")
        score = 0
        qus = "QUS 1) who developed python?"
        a = "A) Guido van Rossum"
        b = "B) Dennis Ritchie"
        e = "C) James Gosling"
        d = "D) Brendan Eich"
        print(qus)
        print(a)
        print(b)
        print(e)
        print(d)
        ans = input("Your ans: ")
        if ans.lower() == 'a':
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        qus = "QUS 2) who developed c programming language?"
        a = "A) Dennis Ritchie"
        b = "B) Brendan Eich"
        e = "C) Tim Berners-Lee"
        d = "D) Rasmus Lerdorf"
        print(qus)
        print(a)
        print(b)
        print(e)
        print(d)
        ans = input("Your ans: ")
        if ans.lower() == 'a':
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

        qus = "QUS 3) who developed java programming language?"
        a = "A) James Gosling"
        b = "B) Graydon Hoare"
        e = "C) Rasmus Lerdorf"
        d = "D) Dennis Ritchie"
        print(qus)
        print(a)
        print(b)
        print(e)
        print(d)
        ans = input("Your ans: ")
        if ans.lower() == 'a':
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        query = "UPDATE st SET score = %s WHERE name = %s"
        cursor.execute(query, (score, name))
        con.commit()
        print("Your score is:", score)
    else:
        print("Login failed")

#diplay methode show all the recode which stored in  database

def display():
    con=c.connect(host="localhost",user="root",passwd="*********",database="exam")
    cursor=con.cursor()
    query="select *from st"
    cursor.execute(query)
    for row in cursor:
        print("NAME OF USER :",     row[0])
        print("passowrd of user:",row[1])
        print("total score of user",   row[2])
        print(("----------- new user----------------------------"))
    con.commit()


while True:
    n = int(input("Enter your choice (1: insert, 2: login 3: display): "))
    if n == 1:             #if user choise 1 then they insert record
        insert()
    elif n == 2:      # if user choise 2 then they login and after the take quiz
        login()
    elif n==3:      # if user choise 3 then they see all recode  which store in database
        display()
    else:
        print("Invalid choice")
