import os
import uuid
from db import mycursor, mydb

def upload_data(name, email, password):
    print('uploading...')
    id = uuid.uuid4().int%10000
    sql = "INSERT INTO users(name, email, password, account_id) VALUES (%s, %s, %s, %s)"
    val = (name, email, password, id)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()
    print('Account created successfully')
    print("Your Account ID is ", id)

def create_password():
    print('Enter Password: ', end='')
    password = input()
    print('Re-enter Password: ', end="")
    cpassword = input()   
    if(password == cpassword):
        return password
    else:
        password = ""
        print("Passwords does not match")
        create_password() 

def create_user():
    os.system('cls')
    print("Welcome to the Bank")
    print('\n')
    print('Create User')
    print('\n')
    print('Enter Name: ', end="")
    name = input()
    print('Enter E-Mail: ', end="")
    email = input()
    pas = create_password()
    upload_data(name, email, pas)


