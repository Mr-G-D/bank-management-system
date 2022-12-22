import os
from db import mycursor, mydb


def check_account(acc_id):
    sql = "SELECT password, balance FROM users WHERE account_id = %s"
    val = [(acc_id)]
    mycursor.execute(sql, val)
    data = mycursor.fetchall()
    if(data):
        return(data[0])
    else:
        print("No Account Found")
        del(data)
        check_balance('Account not found!')

def password_verification(password):
    print("Enter Password: ", end='')
    new_pass = input()
    if(password == new_pass):
        return True
    else:
        check_balance('Invalid Password')


def check_balance(msg = ''):
    os.system('cls')
    print("Check balance")
    print('\n')
    print(msg)
    print("Enter Account ID: ", end="")
    id = int(input())
    [password, balance] = check_account(id)
    if(password_verification(password)):
        print('The account balance is', balance)


