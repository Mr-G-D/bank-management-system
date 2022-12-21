import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="", database = 'bank_system')

mycursor = mydb.cursor()

# mycursor.execute("show databases")

# for i in mycursor:
#     print(i)
