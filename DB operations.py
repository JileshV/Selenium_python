import mysql.connector

try:
    con = mysql.connector.connect(host="localhost", port="3306", user="root", passwd="root", database="mydatabase")
    curs = con.cursor()
    # curs.execute("insert into student values(112, 'Sagar', 76)")
    # con.commit()
    # con.close()

    # curs.execute("update student set marks=70 where sname='Ajay'")
    # con.commit()
    # con.close()

    curs.execute("delete from student where sno=110")
    con.commit()
    con.close()

except:
    print("Connection failed.. please check connection parameters.")

# print("Database updated!")