import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="root", database="mydatabase")
    curs = con.cursor()
    curs.execute("select * from student")
    print("|    Roll no  |   Name    |   Marks   |")
    for row in curs:
        print(f"|   {row[0]}    |   {row[1]}    |   {row[2]}")

except:
    print("Connection failed.. please check connection parameters.")