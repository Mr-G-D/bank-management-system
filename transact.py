import os
from db import mycursor, mydb
import datetime



def update_data(id, amount):
    sql = 'UPDATE users SET balance=%s WHERE account_id=%s'
    val = (amount, id)
    mycursor.execute(sql, val)
    mydb.commit()

def fetch_data(id):
    sql = "SELECT password, balance FROM users WHERE account_id = %s"
    val = [(id)]
    mycursor.execute(sql, val)
    data = mycursor.fetchall()
    if(data):
        return(data[0])  
    else:
        return False  

def password_verification(id, amount):
    [password, balance] = fetch_data(id)
    print("Enter Password: ", end='')
    new_pass = input()
    if(password == new_pass):
        if(balance>amount):
            return True
        else:
            transact('Balance insufficient')
    else:
        transact('Invalid Password')

def update_balance(sender, receiver, amount):
    [password, balance] = fetch_data(sender)
    balance -= amount
    final = balance
    update_data(sender, balance)
    [password, balance] = fetch_data(receiver)
    balance += amount
    update_data(receiver, balance)
    return(final)

def transact(msg = ''):
    os.system('cls')
    print("Transaction")
    print('\n')
    print(msg)
    print("Enter your account ID: ", end="")
    sender = int(input())
    if(fetch_data(sender) == False):
        transact('Account not found')
    print("Enter receiver's account ID: ", end="")
    receiver = int(input())
    if(fetch_data(receiver) == False):
        transact('Receiver account not found')
    print("Enter Amount: ", end='')
    amount = int(input())
    if(password_verification(sender, amount)):
        print('processing transaction...')
        final = update_balance(sender, receiver, amount)
        sql = 'INSERT INTO transactions(sender, receiver, amount) VALUES (%s, %s, %s)'
        val = (sender, receiver, amount)
        mycursor.execute(sql, val)
        mydb.commit()
        mydb.close()
        print('Transaction successfull')
        print('Current balance: ', final)


